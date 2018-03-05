#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from thermos import create_app, db
# Although Bookmark is not referenced in this file, it is needed to imported so that 
# it can be detected by the database migrator.
from thermos.models import User, Bookmark, Tag

from flask_script import Manager, prompt_bool
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('THERMOS_ENV') or 'dev')
manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
        
if __name__ == '__main__':
    manager.run()
