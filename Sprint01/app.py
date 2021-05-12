from flask import Flask, render_template, request, url_for

app = Flask(__name__)


def parse_input(a):
	return list(set(sorted([int(i) for i in a.split(' ')])))



def analysis(your_list):
	your_dict = {}
	for i in your_list:
		if i in your_dict:
			your_dict[i] += 1
		else:
			your_dict[i] = 1
	return your_dict
 

def count_sum(your_dict):
	new_list = list()
	current = 0
	for i in your_dict.values():
		new_list.append(i+current)
		current += i
	print(your_dict)
	return new_list


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/task1", methods=['post', 'get'])
def Task1():
	result = None
	if request.method == 'POST':
		a = request.form.get('feild1')
		b = request.form.get('feild2')
		line_a = parse_input(a)
		line_b = parse_input(b)
		line_c = line_a + line_b
		result = analysis(line_c)
		count_sum(result)
	return render_template('task1.html', result=result)
