from flask import Flask, render_template, redirect, request, session
import random


app = Flask(__name__)
app.secret_key = "thisIsSecret"


@app.route("/")
def index():
    if 'num' not in session:
        session['num'] = random.randint(1,101)
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    print(request.form)
    session['guessed_num'] = int(request.form['number'])
    if session['guessed_num'] < session['num']:
        session['color'] = "orange"
        session['message'] = "Too Low!"
    elif session['guessed_num'] > session['num']:
        session['color'] = "red"
        session['message'] = "Too High!"
    else:
        session['color'] = "green"
        session['message'] = str(session["guessed_num"]) + " was the number!"
    return redirect("/")


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)
