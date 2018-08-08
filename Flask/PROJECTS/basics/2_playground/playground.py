from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("/index.html")

@app.route('/play')
def index1():
    return render_template("/index.html", num=3)


@app.route('/play/<num>')
def play(num):
    return render_template("/index.html", num=int(num))


@app.route('/play/<num>/<color>')
# The "@" symbol designates a "decorator" which attaches the
# following function to the '/' route. This means that
# whenever we send a request to localhost:5000/ we will run
# the following "hello_world" function.
def play_color(num, color):
    # RENDERING THE TEMPLATE AND RETURNING IT!
    return render_template("/index.html", num=int(num), color=color)


app.run(debug=True)
