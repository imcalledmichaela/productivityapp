from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://vaviwhocxsnomz:c274c35a9cb7d6c8bd8418ffbcda4431d407ffafca6d5e59ef2018e37aec61ef@ec2-34-230-110-100.compute-1.amazonaws.com:5432/d3ug8s7afnkd2o'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100, 'pool_recycle': 280}

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

class ProductivityApp(db.Model):
    

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()