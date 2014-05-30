from sets import Set
from get_unigram import get_unigram
from get_bigram import get_bigram
import nltk
import re
import os
from math import *
from nltk.probability import FreqDist
from collections import OrderedDict
from nltk import bigrams
import cPickle as pickle
import operator

def get_bigram_file(path):
	"Function to get the unigram model of the given file"
	
	fh=open(path,"r")
	lines = bigrams(fh.read().strip().split())
	#lines = re.sub("[()+.,\']",'',lines)
	freq_dist_bigram = FreqDist(lines)
	probdict =dict(freq_dist_bigram)
	#print probdict	
	return probdict



def build(master_dict, path, l, fh):
	'''	
	master = ()
	master = sorted(master_dict)

	m_dict = OrderedDict()
	for item in master:
		m_dict[item] = 0
	'''
	print "12"
	temp_dict = get_bigram_file(path)
	temp_dict = OrderedDict(sorted(temp_dict.items()))
	print "13"
	#m_dict.update(temp)
	if l == 'pos':
		lab = '+1'
	else:
		lab = '-1'
	print "14"
	#fh.write(lab)
	temp_str = lab
	for key in temp_dict.iterkeys():
		#print " "+str(key)+":"+str(temp_dict[key])				
		#fh.write(" "+str(master_dict.keys().index(key))+":"+str(temp_dict[key]))
		temp_str += " "+str(master_dict[key])+":"+str(temp_dict[key])	
	fh.write(temp_str+"\n")
	print "15"	
	#fh.write('\n')
	#print l+","+",".join(values)


def build_training_vector(master_dict, train_set, path, label, fold):
	fh = open('training_bi_liblinear_'+str(fold)+'.csv', 'w+')
	print "7"	
	for x in train_set:
		print "8"		
		for l in label:
			print "9"			
			files = os.listdir(path+'/'+str(x)+'/'+l)
			for f in files:
				print "10"				
				build(master_dict, path+'/'+str(x)+'/'+l+'/'+f, l, fh)
				print "11"					
	fh.close()
	'''
	fh = open('test_bi_liblinear_'+str(fold)+'.csv', 'w+')
	for l in label:
		files = os.listdir(path+'/'+str(fold)+'/'+l)
		for f in files:
			build(master_dict, path+'/'+str(fold)+'/'+l+'/'+f, l, fh)
	
	
	fh.close()
	'''


myset = Set([1,2,3,4,5]);
temp = myset
#fp = open('results_unigram','w+')
master_dict= dict()
Pos_Dict = dict()
Neg_Dict= dict()
path = 'dataset'
for x in myset:
	#temp.remove(x)
	
        Pos_Dict = get_bigram('pos', path, temp)
        Neg_Dict = get_bigram('neg', path, temp)
	print "1"
	master_dict.update(Pos_Dict)
	master_dict.update(Neg_Dict)
	print "2"	
	master = ()
	master = sorted(master_dict)
	print "3"
	#print master_dict
	
	master = ()
	master = sorted(master_dict)
	print "4"
	#print master
	
	m_dict = OrderedDict()
	count = 1
	for item in master:
		m_dict[item] = count 
		count += 1	
	print "5"
	#print len(m_dict)
	
	label = set()
	label = ('pos', 'neg')
	
	build_training_vector(m_dict,temp, path, label, x)
	print "6"
	temp.add(x)
	
	
	print x
		

#fh.close()	
#print Pos_Dict
