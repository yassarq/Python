from flask import Flask, render_template, redirect, requrest, session
import random
app = Flask(__name__)

@app.route('/')
def index():
    if 'num' not in session:
        session['sum'] = random.randint(1,101)
    print(session)
    return render_template("index.html")

@app.root("/process", methods=["POST"])
def process():
    print(request.form)
    session['guessed_num'] = request.form ['number']
    if session['guessed_num'] < session['num']:
        session['color'] = "red"
    if session['guessed_num'] > session['num']:
        session['color'] = "red"
    else:
        session['color'] = "green"
    return redirect("/")


@app.route("/reset")
def reset():
    
if __name__ == "__main__":
    app.run(debug=True)