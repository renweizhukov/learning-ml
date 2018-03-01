#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask.ext.script import Manager, prompt_bool

from thermos import app, db
from thermos.models import User

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username='reindert', email='reindert@example.com'))
    db.session.add(User(username='arjen', email='arjen@example.com'))
    db.session.commit()
    print('Initialized the database')
    
@manager.command
def dropdb():
    if prompt_bool(
        'Are you sure you want to lose all your data'):
        db.drop_all()
        print('Dropped the database')
        
if __name__ == '__main__':
    manager.run()
