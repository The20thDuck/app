#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 09:12:57 2018

@author: Warren
"""

from flask import Flask, render_template
import os
import requests
site = Flask(__name__)
api_url = 'https://api.chess.com/pub/player/The20thDuck'
@site.route('/')
def home():
    api_data = requests.get(api_url).json()
    stat_data = requests.get(api_url + '/stats').json()
    return render_template('Home.html', datas = api_data, stats = stat_data)
if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	site.run(host="0.0.0.0", port=port, threaded=True)