from sets import Set
from get_unigram import get_unigram
import nltk
import re
import os
from math import *
from nltk.probability import FreqDist
from collections import OrderedDict
import operator

def get_unigram_file(path):
	"Function to get the unigram model of the given file"
	
	fh=open(path,"r")
	lines = fh.read()
	#lines = re.sub("[()+.,\']",'',lines)
	words = nltk.tokenize.word_tokenize(lines)
	freq_dist_unigram = FreqDist(words)
	probdict =dict(freq_dist_unigram)
	#print probdict	
	return probdict



def build(master_dict, path, l, fh):
	print "12"
	temp_dict = get_unigram_file(path)
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
	fh = open('training_uni_lib_'+str(fold)+'.csv', 'w+')
	for x in train_set:
		for l in label:
			files = os.listdir(path+'/'+str(x)+'/'+l)
			for f in files:
				
				build(master_dict, path+'/'+str(x)+'/'+l+'/'+f, l, fh)
				
				
		
	fh.close()
	'''	
	fh = open('test_uni_'+str(fold)+'.csv', 'w+')
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

        Pos_Dict = get_unigram('pos', path, temp)
        Neg_Dict = get_unigram('neg', path, temp)
	
	master_dict.update(Pos_Dict)
	master_dict.update(Neg_Dict)
	sorted_x = sorted(master_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
	#print master_dict
	master_dict = dict()
	master_dict = {y:x for y,x in sorted_x[:]}
	
	master = ()
	master = sorted(master_dict)
	
	#print master

	m_dict = OrderedDict()
	count = 1
	for item in master:
		m_dict[item] = count	
		count += 1
	#print m_dict
	
	label = set()
	label = ('pos', 'neg')
	
	build_training_vector(m_dict, temp, path, label, x)

	temp.add(x)
	
	print x
		

#fh.close()	
#print Pos_Dict
