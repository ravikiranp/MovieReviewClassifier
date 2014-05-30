from sets import Set
from get_bigram import get_bigram
from nltk import *
import re
import os
from math import *

def perplexity(Prob_dist, filename, N):
	fh = open(filename, 'r')
        #lines = fh.read().split()
        #lines = re.sub("[()+.,\']",'',lines)
        #words = nltk.tokenize.word_tokenize(lines)
	bg = bigrams(fh.read().split())	
	prob = float(0)
	for word in bg:
		if Prob_dist.has_key(word):
			prob = prob + log(float(Prob_dist[word] + 0.00004), 2)
		else:
				
			prob = prob +log( 0.00004, 2)

	#perplex = float(-1)*(float(1)/float(v))*prob
	#perplex = 10**perplex
	#print perplex
	return prob

myset = Set([1,2,3,4,5]);
temp = myset
fp = open('results_unigram','w+')
Pos_Dict= dict()
Neg_Dict= dict()
for x in myset:
	temp.remove(x)
        Pos_Dict = get_bigram('pos','dataset',temp)
	# Calculate pos_perplexity
	print len(Pos_Dict)
        Neg_Dict = get_bigram('neg','dataset',temp)
	print len(Neg_Dict)
	# Calculate neg_perplexity
	fpath = 'dataset/'+str(x)
	test_file_p = os.listdir(fpath +'/pos')
	test_file_n = os.listdir(fpath+'/neg') 
	fp.writelines("Test folder:"+str(x)+"\n")
	#test positive folder under test folder
	y_true = list()
	y_pred = list()

	Npos =0
	Nneg = 0

	for i in Pos_Dict.values():
		Npos = Npos + i
	Npos = float(Npos)

	for i in Neg_Dict.values():
		Nneg = Nneg + i
	Nneg = float(Nneg)

	for p in Pos_Dict.keys():
		Pos_Dict[p] = float(Pos_Dict[p])/Npos

	for p in Neg_Dict.keys():
		Neg_Dict[p] = float(Neg_Dict[p])/Nneg 





	for test in test_file_p:
		pos_perp = perplexity(Pos_Dict, fpath+"/pos/"+test, Npos)
		neg_perp = perplexity(Neg_Dict, fpath+"/pos/"+test, Npos)
		if pos_perp > neg_perp:
			y_true.append(1)
			y_pred.append(1)
			#fp.writelines("original pos\t"+test+"\tpred pos\n")
		else:
			y_true.append(1)
			y_pred.append(0)
			#fp.writelines("original pos\t"+test+"\tpred neg\n")
	#test negative folder under test folder
	
	for test in test_file_n:
		
                pos_perp = perplexity(Pos_Dict, fpath+"/neg/"+test, Nneg) 
                neg_perp = perplexity(Neg_Dict, fpath+"/neg/"+test, Nneg) 
        	

		#print neg_perp
	        if pos_perp > neg_perp:
			y_true.append(0)
			y_pred.append(1)
                        #fp.writelines("original neg\t"+test+"\tpred pos\n")
                else:
			y_true.append(0)
			y_pred.append(0)
                        #fp.writelines("original neg\t"+test+"\tpred neg\n")
	
	
	target_names = ['0', '1']
	from sklearn.metrics import classification_report
	print(classification_report(y_true, y_pred, target_names=target_names))


	
 	print "in progress"	
	temp.add(x)

fp.close()	
#print Pos_Dict
