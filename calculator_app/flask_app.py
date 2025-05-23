
from flask import Flask, render_template, request

from helper import perform_calculation, convert_to_float

app = Flask(__name__)  # create the instance of the flask class

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])  # associating the POST method with this route
def calculate():

    # using the request method from flask to request the values that were sent to the server through the POST method
    value1 = request.form['value1']
    value2 = request.form['value2']
    operation = str(request.form['operation'])

    # make sure the input is one of the allowed inputs (not absolutely necessary in the drop-down case)
    if operation not in ['add', 'subtract', 'divide', 'multiply']:
        return render_template('index.html',
                               printed_result='Operation must be one of "add", "subtract", "divide", or "multiply".')

    try:
        value1, value2 = convert_to_float(value1=value1, value2=value2)
    except ValueError:
        return render_template('index.html', printed_result="Cannot perform operation with this input")

    try:
        result = perform_calculation(value1=value1, value2=value2, operation=operation)
        return render_template('index.html', printed_result=str(result))

    except ZeroDivisionError:
        return render_template('index.html', printed_result="You cannot divide by zero")
