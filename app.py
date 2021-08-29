import flask
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import sqlalchemy,SQLAlchemy
import getData
import matplotlib


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
#Decorator
@app.route('/' , methods = ['GET'])
def index_page():
    data = getData.getApiData()
    return render_template('test.html', data=None)


if __name__  ==  "__main__":
    app.run(debug=False)
