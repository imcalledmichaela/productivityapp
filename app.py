from platform import platform
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

db = SQLAlchemy(app)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

class Event(db.Model):
    __tablename__ = 'event'

    event_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), nullable = False)
    subcategory_id = db.Column(db.Integer, db.ForeignKey("subcategory.subcategory.id"), nullable = False)
    date = db.Column(db.Date, nullable = False)
    start_time = db.Column(db.Integer, nullable = False)
    end_time = db.Column(db.Integer, nullable = False)
    location = db.Column(db.String(254), nullable = False)
    details = db.Column(db.String(254), nullable = False)

    def __init__(self, name, subcategory_id, date, start_time, end_time, location, details):
        self.name = name
        self.subcategory_id = subcategory_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.details = details

    def to_dict(self):
        return {
            "event_id": self.event_id,
            "name": self.name,
            "subcategory_id": self.subcategory_id,
            "date": self.date,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "location": self.location,
            "details": self.details
        }

class Task(db.Model):
    __tablename__ = 'task'

    task_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), nullable = False)
    subcategory_id = db.Column(db.Integer, db.ForeignKey("subcategory.subcategory_id"), nullable = False)
    date = db.Column(db.Date, nullable = False)
    duration = db.Column(db.Date, nullable = False)
    end_time = db.Column(db.Integer, nullable = False)
    details = db.Column(db.String(254), nullable = False)

    def __init__(self, name, subcategory_id, date, duration, end_time, details):
        self.name = name
        self.subcategory_id = subcategory_id
        self.date = date
        self.duration = duration
        self.end_time = end_time
        self.details = details

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "name": self.name,
            "subcategory_id": self.subcategory_id,
            "date": self.date,
            "duration": self.duration,
            "end_time": self.end_time,
            "details": self.details
        }
        
class Category(db.Model):
    __tablename__ = 'category'

    category_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), nullable = False)

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {
            "category_id": self.category_id,
            "name": self.name,
        }
        
class Subcategory(db.Model):
    __tablename__ = 'subcategory'

    subcategory_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), nullable = False)
    cateogry_id = db.Column(db.Integer, db.ForeignKey("category.category_id"), nullable = False)
    color = db.Column(db.String(64))

    def __init__(self, name, category_id, color):
        self.name = name
        self.cateogry_id = category_id
        self.color = color

    def to_dict(self):
        return {
            "subcategory_id": self.subcategory_id,
            "name": self.name,
            "category_id": self.cateogry_id,
            "color": self.color
        }
    
    

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()
