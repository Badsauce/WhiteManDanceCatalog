import os
import sys
import datetime
import json
import requests

from flask import Flask, flash, render_template, redirect, jsonify, url_for, request, Response
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required, roles_required, current_user
from flask.ext.security.signals import user_registered
from wtforms import *

# Constants

category_list = [
  ('wedding', 'Wedding'),
  ('bar', 'Bar'),
  ('wallflower', 'Wall Flower'),
  ('mschaperone', 'Middle School Chaperone'),
]

# Config

app = Flask(__name__)
app.config.from_object(__name__)
app.config['DEBUG'] = 'PRODUCTION' not in os.environ
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'development_key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQL_DATABASE_URI', 'sqlite:///dev.db')
app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
app.config['SECURITY_PASSWORD_SALT'] = os.environ.get('PASSWORD_SALT', '$2a$12$skCRnkqE5L01bHEke678Ju')

app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_REGISTER_URL'] = '/register'
app.config['SECURITY_REGISTER_USER_TEMPLATE'] = 'register.html'
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False

app.config['SECURITY_LOGIN_USER_TEMPLATE'] = 'login.html'
app.config['SECURITY_LOGIN_URL'] = '/login'
app.config['SECURITY_CHANGEABLE'] = True

# Database

db = SQLAlchemy(app)

roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
  __tablename__ = 'role'
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(80), unique=True)
  description = db.Column(db.String(255))

class Step(db.Model):
  __tablename__ = 'step'
  id = db.Column(db.Integer(), primary_key = True)
  name = db.Column(db.String(30), nullable=False)
  vine_url = db.Column(db.String(50), nullable=False)
  vine_embedded_html = db.Column(db.String(50), nullable=False)
  dance_id = db.Column(db.Integer, db.ForeignKey('dance.id'))

class Dance(db.Model):
  __tablename__ = 'dance'
  id = db.Column(db.Integer(), primary_key = True)
  name = db.Column(db.String(30), nullable=False)
  category = db.Column(db.String(30), nullable=False)
  difficulty = db.Column(db.Integer(), default=1)
  hotness = db.Column(db.Integer(), default=1)
  youtube_id = db.Column(db.String(50), nullable=False)
  steps = db.relationship('Step')
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
  __tablename__ = 'user'
  id = db.Column(db.Integer(), primary_key=True)
  email = db.Column(db.String(120), index = True, unique = True, nullable = False)
  password = db.Column(db.String(255), nullable = False)
  active = db.Column(db.Boolean())
  confirmed_at = db.Column(db.DateTime())
  roles = db.relationship('Role', secondary=roles_users,
      backref=db.backref('user', lazy='dynamic'))

  def is_admin(self):
    return self.has_role("admin")

  dances = db.relationship('Dance')

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@user_registered.connect_via(app)
def user_registered_sighandler(app, user, confirm_token):
  default_role = user_datastore.find_role("user")
  user_datastore.add_role_to_user(user, default_role)
  db.session.commit()

# Forms

class DanceForm(Form):
  name = TextField('Name', [validators.Length(min=2, max=30)])
  youtube_id = TextField('Youtube ID', [validators.Length(min=2, max=50)])
  category = SelectField('Category', choices=category_list)
  difficulty = RadioField('Difficulty', choices=[
    ('1','Easy'),
    ('2','Medium'),
    ('3','Hard')
  ])
  hotness = RadioField('Hotness', choices=[
    ('1','Mild'),
    ('2','Spicy'),
    ('3','Hot')
  ])

class StepForm(Form):
  name = TextField('Name', [validators.Length(min=2, max=30)])
  vine_url = TextField('Vine URL', [validators.Length(min=2, max=50)])

# Routes

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/register', methods=['GET'])
def register():
  return render_template('register.html')

@app.route('/dance/new', methods=['GET'])
@login_required
def new_dance():
  form = DanceForm(request.form)
  return render_template('new_dance.html', form=form)

@app.route('/dance/create', methods=['POST'])
@login_required
def create_dance():
  form = DanceForm(request.form)
  if form.validate():
    dance = Dance()
    dance.name = form.name.data
    dance.youtube_id = form.youtube_id.data
    dance.category = form.category.data
    dance.difficulty = form.difficulty.data
    dance.hotness = form.hotness.data
    dance.user_id = 1
    db.session.add(dance)
    db.session.commit()
    flash('Successfully added dance!')
    return redirect('/')
  else:
    flash('Error creating dance!')
    return redirect('/')

@app.route('/dances')
def dances():
  dances = Dance.query.all()
  if dances:
    return render_template('dances.html', dances=dances)
  else:
    flash('No dances!')
    return redirect('/')

@app.route('/dance/<id>')
def dance(id):
  d = Dance.query.get(id)
  if d:
    return render_template('dance.html', dance=d)
  else:
    flash('No such dance!')
    return redirect('/')

@app.route('/dance/<dance_id>/step/new', methods=['GET'])
@login_required
def new_step(dance_id):
  form = StepForm(request.form)
  return render_template('new_step.html', form=form, dance_id=dance_id)

@app.route('/dance/<dance_id>/step/create', methods=['POST'])
@login_required
def create_step(dance_id):
  form = StepForm(request.form)
  if form.validate():
    step = Step()
    step.name = form.name.data
    step.vine_url = form.vine_url.data

    # Get Vine embedded HTML from URL
    r = requests.get('https://vine.co/oembed.json?url=' + step.vine_url)
    try:
      html = r.json()['html']
    except:
      flash('Error creating step!')
      return redirect('/')

    step.vine_embedded_html = html

    step.dance_id = dance_id
    db.session.add(step)
    db.session.commit()
    flash('Successfully added step!')
    return redirect('/')
  else:
    flash('Error creating step!')
    return redirect('/')

@app.route('/dance/<dance_id>/steps')
def steps(dance_id):
  steps = db.session.query(Step).filter(Step.dance_id == dance_id)
  if steps:
    return render_template('steps.html', steps=steps)
  else:
    flash('No steps!')
    return redirect('/')

@app.route('/step/<step_id>')
def step(step_id):
  s = Step.query.get(step_id)
  if s:
    return render_template('step.html', step=s)
  else:
    flash('No such step!')
    return redirect('/')

@app.route('/category/<name>')
def category(name):
  dances = db.session.query(Dance).filter(Dance.category == name)
  if dances:
    return render_template('category.html', dances=dances, name=name)
  else:
    flash('No dances for this category!')
    return redirect('/')

@app.route('/categories')
def categories():
  return render_template('categories.html', categories=category_list)

@app.route('/gifapalooza')
def gifapalooza():
  return render_template('gifapalooza.html')

@app.route('/funeral')
def funeral():
  return render_template('funeral.html')
