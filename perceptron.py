import nltk
from numpy import dot,random

# Movie review result: +1 for pos, -1 for neg
numIter = [1]*100
learning_rate = 0.37

def WeightUpdate(weights,train_data,err):
	" Update the weights"
	for i in range(0,len(train_data)):
		
		weights[i] += (float)(err)*(train_data[i])*(float(learning_rate)) 

	return weights

def Perceptron():
	"Perceptron Model"
	vector = list()
	flag = 0
	for iterm in range(0,100):
		print iterm
		with open('trainfinal_1.csv','r') as fh:
			for lines in fh:
				
				vector = list(lines.split(','))
				
				vector[-1] = vector[-1].rstrip()
				
				if vector[0] == 'pos':
					expected_res = 1
				else:
					expected_res = -1

				training_data = vector[1:]
		
				training_data = [float(i) for i in training_data]
								
				
				if flag == 0:
					weights = random.rand(len(training_data));					
						
					
					flag = 1
				
				result = dot(weights,training_data);
				if result >= 0:
					res = 1
				else:
					res = -1
				
				if res != expected_res:
					err = expected_res - res	
				
					weights = WeightUpdate(weights,training_data,err)
				
	
	true_label = list()
	pred_label = list()
	with open('trainfinal_2.csv','r') as fhandle:
		for lines in fhandle:
			vector = list(lines.split(','))
		        vector[-1] = vector[-1].rstrip()
			if vector[0] == 'pos':
		        	true_label.append(1)
			else:
				true_label.append(0)
			test_data = vector[1:]
					
		        test_data = [float(i) for i in test_data]

			result = dot(weights,test_data)
			if result >= 0:
				pred_label.append(1)
			else:
				pred_label.append(0)
				

	target_names = ['1', '0']
	from sklearn.metrics import classification_report
	print(classification_report(true_label, pred_label, target_names=target_names))

		

if __name__ == "__main__":

    Perceptron()

