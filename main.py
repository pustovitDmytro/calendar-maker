# -*- encoding: utf-8 -*-
from abc import ABCMeta
import re
import os
from json import JSONEncoder
import csv
from datetime import date

class Page():
	__metaclass__ = ABCMeta
	def __init__(self, name, result='out' dir_source="source/", dir_results="results/"):
		self.dir_source = dir_source
		self._prepare_folder(self.dir_source)
		self.link = dir_source + name
		self.name = result

	def read(self,format='csv'):
		if format=='csv':
			pass

	def save(self,type='csv',name=self.name):
		if type=='json':
			self._save_json(self.dir_results+name,elements)

	# protected level
	def _read_csv(self):
		with open(self.link) as csvfile:
			reader = csv.DictReader(csvfile,delimiter =";")
			for row in reader:
				print(row['name'],row['date'])
	def _write_csv(self):
		with open(self, 'w',newline='') as csvfile:
		fieldnames = ['Subject','Start Date','All Day Event','Private']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter =",")
		writer.writeheader()
		for event in self.data:
			record = {
			'Subject': event['name']+"'s birthday",
			'Start Date': event['date']
			'All Day Event': True
			'Private': True
			}
			writer.writerow(record)
	
	def _save_json(self,name,elements):
		jsonString = JSONEncoder(ensure_ascii = False).encode(elements)
		f = open(name+'.json', 'w', encoding='utf8')
		f.write(jsonString)

	def _prepare_folder(self,path):
		if not os.path.isdir(path):
			os.makedirs(path)

page = Page('family.txt')
page._read_csv();