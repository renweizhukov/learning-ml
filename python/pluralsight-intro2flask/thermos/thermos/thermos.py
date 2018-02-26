#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    def initials(self):
        return "{}. {}.".format(self.firstname[0], self.lastname[0])

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', 
                           title='Title passed from view to template', 
                           user=User('Wei', 'Ren'))
                           
@app.route('/add')
def add():
    return render_template('add.html')
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500  
  
if __name__ == '__main__':
    app.run()
