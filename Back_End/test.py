# -*- coding: utf-8 -*
import os
import json
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
from src.DealData.DealData import saveAccident, getMonthIn4, getDetail, getAllAccident
'''
app = Flask(__name__)

@app.route('/getall', methods=['POST'])
def getAll():
	data = request.form.to_dict()
	result = getAllAccident()
	stri = '{"data": [[201600000022, 5084579, 226407]]}'
	return result

@app.route('/upload', methods=['POST'])
def upload():
	data = request.form.to_dict()
	result = saveAccident(data)
	return result

@app.route('/month', methods=['POST'])
def month():
	date = request.form.to_dict()['date']
	result = getMonthIn4(date)
	return result

@app.route('/detail', methods=['POST'])
def detail():
	acc = request.form.to_dict()['accNum']
	result = getDetail(acc)
	return result

if __name__ == '__main__':
	app.run(port=2000,debug=True)
'''
print(getAllAccident())