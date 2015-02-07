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

      # Dance 1
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

      # Dance 2
      dance = Dance()
      dance.name = 'Raise the Roof'
      dance.youtube_id = '8Br-WlHBQfA'
      dance.category = 'Middle School Chaperone'
      dance.difficulty = 2
      dance.hotness = 2
      dance.user_id = user.id
      db.session.add(dance)
      db.session.commit()

      step = Step()
      step.name = 'Step 1'
      step.vine_url = 'OUz2ezqPOVH'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 2'
      step.vine_url = 'OUz2wlVxhZv'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 3'
      step.vine_url = 'OUz2FWI6MFr'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      # Dance 3
      dance = Dance()
      dance.name = 'Shopping Cart'
      dance.youtube_id = 'Mj7dB7e32ls'
      dance.category = 'Middle School Chaperone'
      dance.difficulty = 2
      dance.hotness = 2
      dance.user_id = user.id
      db.session.add(dance)
      db.session.commit()

      step = Step()
      step.name = 'Step 1'
      step.vine_url = 'OUW9Uhj0pKt'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 2'
      step.vine_url = 'OUW93plg27e'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 3'
      step.vine_url = 'OUWVmA0BAb5'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      # Dance 4
      dance = Dance()
      dance.name = 'The Gambler'
      dance.youtube_id = 'noDsaW373jc'
      dance.category = 'Middle School Chaperone'
      dance.difficulty = 2
      dance.hotness = 2
      dance.user_id = user.id
      db.session.add(dance)
      db.session.commit()

      step = Step()
      step.name = 'Step 1'
      step.vine_url = 'OUWVFxdKqi6'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 2'
      step.vine_url = 'OUWVVqZBxF0'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 3'
      step.vine_url = 'OUWYWgL6YnH'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      # Dance 5
      dance = Dance()
      dance.name = 'Sprinkler'
      dance.youtube_id = 'vU9upFSbb64'
      dance.category = 'Middle School Chaperone'
      dance.difficulty = 2
      dance.hotness = 2
      dance.user_id = user.id
      db.session.add(dance)
      db.session.commit()

      step = Step()
      step.name = 'Step 1'
      step.vine_url = 'OUWVOIevWlK'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 2'
      step.vine_url = 'OUWVvUarnnU'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 3'
      step.vine_url = 'OUWVpdg3EYg'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      # Dance 6
      dance = Dance()
      dance.name = 'Hands in the Air'
      dance.youtube_id = 'br4jzbTEb9o'
      dance.category = 'Middle School Chaperone'
      dance.difficulty = 2
      dance.hotness = 2
      dance.user_id = user.id
      db.session.add(dance)
      db.session.commit()

      step = Step()
      step.name = 'Step 1'
      step.vine_url = 'OUzQAbDih1n'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 2'
      step.vine_url = 'OUzQXiDidXX'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 3'
      step.vine_url = 'OUzQTngxUPA'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      # Dance 7
      dance = Dance()
      dance.name = 'Hands Out, Guns Out, I\'m Out'
      dance.youtube_id = 'S8WUd45uXao'
      dance.category = 'Middle School Chaperone'
      dance.difficulty = 2
      dance.hotness = 2
      dance.user_id = user.id
      db.session.add(dance)
      db.session.commit()

      step = Step()
      step.name = 'Step 1'
      step.vine_url = 'OU7tU6EI25A'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 2'
      step.vine_url = 'OU7t0gaWwXw'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 3'
      step.vine_url = 'OU7FZTHPBXm'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      # Dance 8
      dance = Dance()
      dance.name = 'The Rhythmless Jig'
      dance.youtube_id = 'A_3cww0O-vc'
      dance.category = 'Middle School Chaperone'
      dance.difficulty = 2
      dance.hotness = 2
      dance.user_id = user.id
      db.session.add(dance)
      db.session.commit()

      step = Step()
      step.name = 'Step 1'
      step.vine_url = 'OU7tKDDJwPT'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 2'
      step.vine_url = 'OU7ti0dlnqn'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 3'
      step.vine_url = 'OU7tXLdxUXB'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      # Dance 9
      dance = Dance()
      dance.name = 'The Intense Cotton Eye Joe'
      dance.youtube_id = 'h6As8dTocqI'
      dance.category = 'Middle School Chaperone'
      dance.difficulty = 2
      dance.hotness = 2
      dance.user_id = user.id
      db.session.add(dance)
      db.session.commit()

      step = Step()
      step.name = 'Step 1'
      step.vine_url = 'OU7T6Bnej62'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 2'
      step.vine_url = 'OU7TjTKAqDj'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 3'
      step.vine_url = 'OU7TQFdInBO'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      # Dance 10
      dance = Dance()
      dance.name = 'Eager Student'
      dance.youtube_id = 'c7XX2iZ83ig'
      dance.category = 'Middle School Chaperone'
      dance.difficulty = 2
      dance.hotness = 2
      dance.user_id = user.id
      db.session.add(dance)
      db.session.commit()

      step = Step()
      step.name = 'Step 1'
      step.vine_url = 'OUZLqOWUz9h'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 2'
      step.vine_url = 'OUZLOn1ZZI2'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 3'
      step.vine_url = 'OUZLnWVbuW7'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      # Dance 11
      dance = Dance()
      dance.name = 'Sizzler'
      dance.youtube_id = 'Rxfm9qELqP0'
      dance.category = 'Middle School Chaperone'
      dance.difficulty = 2
      dance.hotness = 2
      dance.user_id = user.id
      db.session.add(dance)
      db.session.commit()

      step = Step()
      step.name = 'Step 1'
      step.vine_url = 'OUZEaw56iDq'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 2'
      step.vine_url = 'OUZExma7T5Q'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 3'
      step.vine_url = 'OUZ9uQ3XMpW'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      # Dance 12
      dance = Dance()
      dance.name = 'Saturday Night Fever'
      dance.youtube_id = 'PmezzsBmOh8'
      dance.category = 'Middle School Chaperone'
      dance.difficulty = 2
      dance.hotness = 2
      dance.user_id = user.id
      db.session.add(dance)
      db.session.commit()

      step = Step()
      step.name = 'Step 1'
      step.vine_url = 'OUZ227KpXlP'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 2'
      step.vine_url = 'OUZ0eF7PPwa'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 3'
      step.vine_url = 'OUZ0FBOiqXw'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 4'
      step.vine_url = 'OUZ0VJt1Wwp'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      # Dance 13
      dance = Dance()
      dance.name = 'Roxbury'
      dance.youtube_id = 'XptYC0iWL7s'
      dance.category = 'Middle School Chaperone'
      dance.difficulty = 2
      dance.hotness = 2
      dance.user_id = user.id
      db.session.add(dance)
      db.session.commit()

      step = Step()
      step.name = 'Step 1'
      step.vine_url = 'OUZQ3TBu1tV'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 2'
      step.vine_url = 'OUZ2a6lhIjb'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 3'
      step.vine_url = 'OUZ2AlqwmZP'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      # Dance 14
      dance = Dance()
      dance.name = 'Shoulder Rock'
      dance.youtube_id = 'D9hbzzu3oTY'
      dance.category = 'Middle School Chaperone'
      dance.difficulty = 2
      dance.hotness = 2
      dance.user_id = user.id
      db.session.add(dance)
      db.session.commit()

      step = Step()
      step.name = 'Step 1'
      step.vine_url = 'OUZQ665nVj1'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 2'
      step.vine_url = 'OUZQP5vIv2X'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      # Dance 15
      dance = Dance()
      dance.name = 'Point and Twist'
      dance.youtube_id = 'LB-aHh-tHw8'
      dance.category = 'Middle School Chaperone'
      dance.difficulty = 2
      dance.hotness = 2
      dance.user_id = user.id
      db.session.add(dance)
      db.session.commit()

      step = Step()
      step.name = 'Step 1'
      step.vine_url = 'OUZxeWLPnPz'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 2'
      step.vine_url = 'OUZQzJ9UWDV'
      step.vine_embedded_html = get_html(step.vine_url)
      step.dance_id = dance.id
      db.session.add(step)
      db.session.commit()

      step = Step()
      step.name = 'Step 3'
      step.vine_url = 'OUZQmA2060I'
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
