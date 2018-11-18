# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import Flask, request, render_template, send_from_directory, jsonify, session
import logging, requests, json
from simpleflake import simpleflake
from .forms import *
from config import INTERNAL_TOKEN, SECRET_KEY
from flask_wtf.csrf import CsrfProtect
from datetime import datetime
from dateutil.relativedelta import relativedelta

logger = logging.getLogger(__name__)
app = Flask(__name__, template_folder="templates", static_folder="statics")
app.secret_key = SECRET_KEY
api_key = "EUsakcfGzBRZhPg3nV1X8AxnFsjS-0it"

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('index.html', **locals())


@app.route("/discount", methods=['POST', 'GET'])
def discount():
    domain = request.args.get("domain", "")
    url = "https://api.accesstrade.vn/v1/offers_informations?domain={0}&status=1".format(domain)
    header = {'Content-Type': 'application/json',
              'Authorization': 'Token {0}'.format(api_key)}
    res = requests.get(url=url, headers=header)
    res_json = res.json()
    data = res_json["data"]
    return render_template('discount.html', **locals())


@app.route("/top_products", methods=['POST', 'GET'])
def top_products():
    date_to = datetime.now()
    date_from = date_to - relativedelta(days=5)
    url = "https://api.accesstrade.vn/v1/top_products?date_from={0}&date_to={1}".format(date_from.strftime("%d-%m-%Y"), date_to.strftime("%d-%m-%Y"))
    header = {'Content-Type': 'application/json',
              'Authorization': 'Token {0}'.format(api_key)}
    res = requests.get(url=url, headers=header)
    res_json = res.json()
    data = res_json["data"]
    return render_template('top_products.html', **locals())


@app.route("/datafeed", methods=['POST', 'GET'])
def datafeed():
    domain = request.args.get("domain", "")
    url = "https://api.accesstrade.vn/v1/datafeeds?domain={0}".format(domain)
    header = {'Content-Type': 'application/json',
              'Authorization': 'Token {0}'.format(api_key)}
    res = requests.get(url=url, headers=header)
    res_json = res.json()
    data = res_json["data"]

    return render_template('datafeed.html', **locals())

