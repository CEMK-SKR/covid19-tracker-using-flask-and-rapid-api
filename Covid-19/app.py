from flask import Flask, render_template, request, redirect,url_for
from api import getApi
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/',methods = ['POST', 'GET'])
def getCountryName():
   if request.method == 'POST':
      user = request.form['input_name']
      print(user)
      A = getApi.Api()
      user_data=A.get_report(user=user)
      print(user_data)
      return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)