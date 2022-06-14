from flask import Flask, request
import json
import pickle
import pandas as pd

with open('Pickle_RL_Model.pkl', 'rb') as file:  
    Pickled_LR_Model = pickle.load(file)


app = Flask(__name__)

@app.route('/', methods = ['POST'])
def sum_of_array():
    	
	data = request.get_json()

	# print(data)

	# ls = data['data']

	# print(ls)

	my_data = pd.DataFrame([data])

	print(my_data)

	my_personality = Pickled_LR_Model.predict(my_data)
	print('My Personality Cluster: ', my_personality)

	col_list = list(my_data)
	ext = col_list[0:10]
	est = col_list[10:20]
	agr = col_list[20:30]
	csn = col_list[30:40]
	opn = col_list[40:50]

	my_sums = pd.DataFrame()
	my_sums['extroversion'] = my_data[ext].sum(axis=1)/10
	my_sums['neurotic'] = my_data[est].sum(axis=1)/10
	my_sums['agreeable'] = my_data[agr].sum(axis=1)/10
	my_sums['conscientious'] = my_data[csn].sum(axis=1)/10
	my_sums['open'] = my_data[opn].sum(axis=1)/10
	my_sums['cluster'] = my_personality

	print(my_sums)

	findings = my_sums.to_json(orient='records')

	print(findings)

	return json.dumps({"result": findings})

if __name__ == "__main__":
	app.run(port=5000)
