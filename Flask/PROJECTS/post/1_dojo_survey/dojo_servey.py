from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def dojo_survey():
    return render_template("dojo_survey.html")

@app.route('/result', methods=['POST','GET'])
def create_result():
    print('Submitted Info')
    print(request.form)
    name = request.form['input']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['user_comment']
    print(name, location, language, comment)
    return render_template('success.html')

if __name__=="__main__":
    app.run(debug=True)