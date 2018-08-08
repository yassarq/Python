from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')
def show_user():
  return render_template('user.html', name='Jay', email='kpatel@codingdojo.com')

if __name__=="__main__":   
    app.run(debug=True)    