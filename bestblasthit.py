#!/usr/bin/env python3
import os
import sys
import fileinput
import argparse
from argparse import RawTextHelpFormatter


def is_valid_file(x):
	if not os.path.exists(x):
		raise argparse.ArgumentTypeError("{0} does not exist".format(x))
	return open(x)

usage = 'bestblasthit.py [-opt1, [-opt2, ...]] infile'
parser = argparse.ArgumentParser(description='a blastn output formatter', formatter_class=RawTextHelpFormatter, usage=usage)
parser.add_argument('-i', '--input',  type=is_valid_file, default=sys.stdin, help='input file in typical blasttab format')
parser.add_argument('-a', '--agg', type=int, action="store", default=0, dest='agg', help='number of the column to aggregate on')
parser.add_argument('-s', '--skip', action="store_true", dest='skip', help='whether to skip ambiguous hits')
args = parser.parse_args()


class ReadHit():
	def __init__(self):
		# index is the column to use as measure for score: 10 is evalue
		self.index = 10
		self.read_line = ''
		self.read_name = None
		self.read_score = float('+Inf')
		self.reads = list()

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
		self.reads = list()
		self.reads.append(line)


taxa_counts = dict()
def print_or_parse(rh):
	counts = dict()
	for read in rh.reads:
		if args.agg:
			column = read.rstrip('\n').split('\t')
			counts[column[args.agg]] = counts.get(column[args.agg], 0) + 1/len(rh.reads)
		else:
			print(read, end='')
	if not args.skip or len(counts)==1:
		for key,value in counts.items():
			taxa_counts[key] = taxa_counts.get(key, 0) + value


read_hit = ReadHit()
for line in args.input:

	# skip comment lines or hits less than 1e-5
	column = line.rstrip('\n').split('\t')
	if line.startswith('#') or float(column[10]) > 0.00001:
		continue

	# add a hit to the read object: returns false if hit belongs to a new read
	if not read_hit.add(line):
		print_or_parse(read_hit)
		read_hit.new(line)

#you have to do it one last time
print_or_parse(read_hit)


if args.agg:
	for key,value in taxa_counts.items():
		print(key, value, sep='\t')
