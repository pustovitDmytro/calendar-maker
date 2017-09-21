# -*- encoding: utf-8 -*-
from abc import ABCMeta
import re
import os
from json import JSONEncoder
import csv
from datetime import date,datetime

class Page():
	__metaclass__ = ABCMeta
	def __init__(self, name, result='out', dir_source="source/", dir_results="results/"):
		self.dir_source = dir_source
		self._prepare_folder(self.dir_source)
		self.link = dir_source + name
		self.name = result
		self.now = date.today()

	def read(self,format='csv'):
		if format=='csv':
			pass

	def save(self,type='csv'):
		name=save.name
		if type=='json':
			self._save_json(self.dir_results+name,elements)

	# protected level
	def _set_year(self,month,day):
		if self.now>date(self.now.year,month,day):
			return self.now.year
		return self.now.year+1
	def get_date(self,strdate):
		date =  datetime.strptime(strdate,'%d.%m');
		print(date);
		return date;
	def _read_csv(self):
		with open(self.link) as csvfile:
			reader = csv.DictReader(csvfile,delimiter =";")
			self.events = []
			for row in reader:
				print(row);
				record = {
				'name': row['name']+"'s birthday",
				'date': self.get_date(row['date'])
				}
				self.events.append(record)
		print(self.events)

	def _write_csv(self):
		with open(self, 'w') as csvfile:
			fieldnames = ['Subject','Start Date','All Day Event','Private']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter =",",newline='')
			writer.writeheader()
			for event in self.data:
				record = {
				'Subject': event['name']+"'s birthday",
				'Start Date': event['date'],
				'All Day Event': True,
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