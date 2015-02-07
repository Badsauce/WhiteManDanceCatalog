import os
import sys
import datetime
import json

from flask import Flask, flash, render_template, redirect, jsonify, url_for, request, Response
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required, roles_required, current_user
from flask.ext.security.signals import user_registered
from wtforms import *

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
  category = SelectField('Category', choices=[
      ('wedding', 'Wedding'),
      ('bar', 'Bar'),
      ('wallflower', 'Wall Flower'),
      ('mschaperone', 'Middle School Chaperone'),
      ('funeralwake', 'Funeral/Wake')
  ])
  difficulty = SelectField('Difficulty', choices=[
      ('wedding', 'Wedding'),
      ('bar', 'Bar'),
      ('wallflower', 'Wall Flower'),
      ('mschaperone', 'Middle School Chaperone')
  ])

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
    dance.category = form.category.data
    dance.difficulty = form.difficulty.data
    db.session.add(dance)
    flash('Successfully added dance!')
    return redirect('/')
  else:
    flash('Error creating dance!')
    return redirect('/')

@app.route('/dance/<id>')
def dance(id):
  steps = ['a', 'b', 'c']
  return render_template('danceydance.html', steps=steps)
