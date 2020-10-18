from flask import Flask, render_template, url_for, request, redirect

app= Flask(__name__)

@app.route('/',methods=['GET','POST'])

@app.route('/home')
def homepage():
    return render_template('hi.html')



