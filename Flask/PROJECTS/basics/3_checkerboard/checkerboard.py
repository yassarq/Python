from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("/index.html", num=4)

@app.route('/<num1>/<num2>')
def index_x(num1, num2):
    return render_template("/index.html", num1=int(num1), num2=int(num2))
    
app.run(debug = True)