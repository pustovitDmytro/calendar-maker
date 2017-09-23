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
		self._prepare_folder(dir_results);
		self.link = dir_source + name
		self.name = dir_results+result
		self.now = date.today()

	def read(self,format='csv'):
		if format=='csv':
			self._read_csv();

	def save(self,type='csv'):
		name=self.name
		if type=='json':
			self._save_json(self.dir_results+name, self.elements)
		elif type=='csv':
			self._write_csv()
		elif type=='ics':
			self._write_ics()

	# protected level
	def _set_year(self,month,day):
		if self.now<date(self.now.year,month,day):
			return self.now.year
		return self.now.year+1

	def get_date(self,strdate):
		odate =  datetime.strptime(strdate,'%d.%m')
		year = self._set_year(odate.month,odate.day)
		return date(year,odate.month,odate.day)

	def _read_csv(self):
		with open(self.link) as csvfile:
			reader = csv.DictReader(csvfile,delimiter =";")
			self.events = []
			for row in reader:
				record = {
				'name': row['name'],
				'date': self.get_date(row['date'])
				}
				self.events.append(record)
	def _write_ics(self):
		with open(self.name+'.ics','w') as file:
			file.write("BEGIN:VCALENDAR\n")
			file.write("VERSION:2.0\n")
			file.write("PRODID:1\n")
			for event in self.events:
				file.write("BEGIN:VEVENT\n")
				file.write("UID:"+event['date'].strftime('%d%m%Y')+event['name']+"@birthday\n")
				file.write("DTSTART:"+event['date'].strftime('%Y%m%d')+"\n")
				file.write("DTEND:"+event['date'].strftime('%Y%m%d')+"\n")
				file.write("CATEGORIES:MEETING\n")
				file.write("CLASS:PUBLIC\n")
				file.write("SUMMARY:"+event['name']+"'s birthday\n")
				file.write("END:VEVENT\n")
			file.write("END:VCALENDAR\n")
	def _write_csv(self):
		with open(self.name+'.cvs', 'w') as csvfile:
			fieldnames = ['Subject','Start Date','All Day Event','Private']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter =",")
			writer.writeheader()
			for event in self.events:
				record = {
				'Subject': event['name']+"'s birthday",
				'Start Date': event['date'].strftime('%d/%m/%Y'),
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
page.read();
page.save(type='csv');
page.save(type='ics');