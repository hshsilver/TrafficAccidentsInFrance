# -*- coding: utf-8 -*
import os
import json
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
from src.DealData.DealData import saveAccident, getMonthIn4, getDetail, getAllAccident, getPredictDeaths, getPredictProbability
app = Flask(__name__)

@app.route('/getall', methods=['POST'])
def getAll():
	data = request.form.to_dict()
	result = getAllAccident()
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
	print(request.form.to_dict())
	acc = request.form.to_dict()['Num_Acc']
	result = getDetail(acc)
	return result

@app.route('/deaths', methods=['POST'])
def predictDeaths():
	data = request.form.to_dict()
	result = getPredictDeaths(data)
	return result

@app.route('/probability', methods=['POST'])
def predictProbability():
	data = request.form.to_dict()
	result = getPredictProbability(data)
	return result

if __name__ == '__main__':
	app.run(port=2000,debug=True)