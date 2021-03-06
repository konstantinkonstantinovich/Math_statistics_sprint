from flask import Flask, render_template, request, url_for

app = Flask(__name__)


def parse_input(a):
	return list(set(sorted([int(i) for i in a.split(' ')])))



def analysis(your_list):
	your_dict = {}
	for i in your_list:
		if i in your_dict:	
			your_dict[i][0] += 1
		else:
			your_dict[i] = [1]
	return your_dict
 

def comulative_relative_frequency(your_dict):
	current = 0
	for i in your_dict.values():
		i.append(i[2]+current)
		current += i[2]
		i[3] = round(i[3], 5)
	return your_dict


def relative_frequency(your_dict):
	for i in your_dict.values():
		i.append(i[0]/len(your_dict.keys()))
		i[2] = round(i[2], 5)
	return your_dict


def accumulative_frequency(your_dict):
	current = 0
	for i in your_dict.values():
		i.append(i[0]+current)
		current += i[0]
	return your_dict

@app.route("/")
def main():
    return render_template('index.html')


@app.route("/task1", methods=['post', 'get'])
def Task1():
	result = None
	if request.method == 'POST':
		a = request.form.get('feild1')
		b = request.form.get('feild2')
		c = request.form.get('feild3')
		line_a = parse_input(a)
		line_b = parse_input(b)
		line_c = parse_input(c)
		line_d = line_a + line_b + line_c
		result = analysis(sorted(line_d))
		print(accumulative_frequency(result))
		print(relative_frequency(result))
		print(comulative_relative_frequency(result))
	return render_template('task1.html', result=result)


