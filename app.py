from flask import Flask, render_template, request
import pickle

app = Flask('name')
@app.route('/')
def man():
    return render_template('home.html')
def home():
   
  if 'name' == "main":
    app.run(debug=True)
