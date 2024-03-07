from flask import Flask, render_template, request


app = Flask(__name__)


@app.get('/')
def index(name=None):
    return render_template('index.html')


@app.post('/')
def calculate(name=None):
    result = ""
    try:     
        num_1 = request.form["number_1"]
        num_2 = request.form["number_2"]
        operation = request.form['operation']

        num_1 = float(num_1)
        num_2 = float(num_2)
        
        if operation == "a":
            result = num_1 + num_2
        elif operation == "s":
            result = num_1 - num_2
        elif operation == "m":
            result = num_1 * num_2
        elif operation == "d":
            result = num_1 / num_2

        return render_template('index.html', result=result)

    except Exception as e:
        return render_template('index.html',
                               error_msg=f"Invalid operation: {e}")


if __name__ == '__main__':
    app.run(debug=False)