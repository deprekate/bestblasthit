#!/usr/bin/env python3

import sys
import fileinput


class ReadHit():
	def __init__(self):
		self.read_line = ''
		self.read_name = None
		self.read_score = float('+Inf')
		self.reads = list(' ')
		self.index = 10

	def __str__(self):
		return next(iter(self.reads or []), None)
		#return ''.join(self.reads)
			

	def add(self, line):
		column = line.rstrip('\n').split('\t')
		if column[0] != self.read_name:
			return False
		if float(column[self.index]) < self.read_score:
			self.new(line)
		elif float(column[self.index]) == self.read_score:
			self.reads.append(line)
		return True

	#@classmethod
	def new(self, line):
		column = line.rstrip('\n').split('\t')
		self.read_line = line.rstrip('\n')
		self.read_name = column[0]
		self.read_score = float(column[self.index])
		self.names = list()



read_hit = ReadHit()

for line in fileinput.input():
	column = line.rstrip('\n').split('\t')
	if float(column[10]) > 0.00001:
		continue
	if not read_hit.add(line):
		print(read_hit)
		read_hit.new(line)


