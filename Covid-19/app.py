from flask import Flask, render_template, request
from api import getApi
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/',methods = ['POST', 'GET'])
def getCountryName():
   if request.method == 'POST':
      user = request.form['input_name']
      try:
        if(user != None):
          print(user)
          A = getApi.Api()
          user_data=A.get_report(user=user)
          print(user_data[0])
          return render_template('index.html', user_data=user_data[0])
      except:
          return render_template('index.html')
      

if __name__ == "__main__":
    app.run(debug=True)
