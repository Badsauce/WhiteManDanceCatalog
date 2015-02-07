#!/usr/bin/env python

import os
import argparse
import code

from app import app, db, user_datastore, Role, User, Dance, Step
from flask_security.utils import encrypt_password
import requests

def get_html(url):
  return '<iframe src="https://vine.co/v/'+url+'/embed/simple?audio=1" width="600" height="600" frameborder="0"></iframe><script src="https://platform.vine.co/static/scripts/embed.js"></script>'

def build():
  with app.app_context():
    db.create_all()
    if not User.query.first():
      user_datastore.create_user(
        email='coach@howtodance.website',
        password=encrypt_password('password'))
      db.session.commit()
      user = User.query.first()

      dance = Dance()
      dance.name = 'The Bus Driver'
      dance.youtube_id = 'KqIT64P1BOU'
      dance.category = 'Middle School Chaperone'
      dance.difficulty = 2
      dance.hotness = 2
      dance.user_id = user.id
      db.session.add(dance)
      db.session.commit()

      step = Step()
      step.name = 'Step 1'
      step.vine_url = 'OUzUuPjmleM'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 2'
      step.vine_url = 'OUzU2V1JZHe'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 3'
      step.vine_url = 'OUzxZHDl7Dv'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Advanced'
      step.vine_url = 'OUz2zqOBJj0'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      


def console():
  context = locals()
  context['app'] = app
  context['db'] = db
  context['user_datastore'] = user_datastore
  context['Role'] = Role
  context['User'] = User
  code.interact(local=locals())

def run():
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port, debug=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action')
    args = parser.parse_args()

    if args.action == 'build':
        build()
    elif args.action == 'console':
        console()
    elif args.action == 'run':
        run()
