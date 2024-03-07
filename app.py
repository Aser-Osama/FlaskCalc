from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.get('/')
def index(name=None):
    return render_template('index.html', result="")


@app.post('/')
def calculate(name=None):
    try:     
        n1 = request.form["number_1"]
        n2 = request.form["number_2"]
        operation = request.form['operation']
    except Exception:
        return render_template('index.html', result="", error_msg=f"Invalid operation.")
        
    print(f"{n1}, {n2}, {operation}")
    return render_template('index.html', result=111)


if __name__ == '__main__':
    app.run(debug=True)