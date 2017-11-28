#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
from flask import Flask, render_template
import json

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

@app.route('/')
def index():
    helloshiyanlou = json.loads('/home/shiyanlou/files/helloshiyanlou.json')
@app.route('/files/<filename>')
def file(filename):

