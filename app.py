from platform import platform
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from json import dumps
import auth

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:productive@productive.ck04jav5vuqu.us-east-1.rds.amazonaws.com/productive'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100, 'pool_recycle': 280}

db = SQLAlchemy(app)
app.register_blueprint(auth.bp)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
class User(db.Model):

    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), nullable = False)
    username = db.Column(db.String(64), nullable = False, unique=True)
    email = db.Column(db.String(254), nullable = False, unique=True)
    password = db.Column(db.String(254), nullable = False)

    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }

    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception:
            return "Unable to create friendship."
        return self

class Friendship(db.Model):
    friendship_id = db.Column(db.Integer, primary_key = True)
    user1_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable = False)
    user2_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable = False)

    def __init__(self, user1_id, user2_id):
        self.user1_id = user1_id
        self.user2_id = user2_id

    def to_dict(self):
        return {
            "friendship_id": self.friendship_id,
            "user1_id": self.user1_id,
            "user2_id": self.user2_id
        }

    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception:
            return "Unable to create friendship."
        return self

class Event(db.Model):
    __tablename__ = 'event'

    event_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable = False)
    name = db.Column(db.String(64), nullable = False)
    subcategory_id = db.Column(db.Integer, db.ForeignKey("subcategory.subcategory_id"), nullable = False)
    date = db.Column(db.Date, nullable = False)
    start_time = db.Column(db.Time, nullable = False)
    end_time = db.Column(db.Time, nullable = False)
    location = db.Column(db.String(254), nullable = False)
    details = db.Column(db.String(254), nullable = False)

    def __init__(self, user_id, name, subcategory_id, date, start_time, end_time, location, details):
        self.name = name
        self.user_id = user_id
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
            "user_id": self.user_id,
            "subcategory_id": self.subcategory_id,
            "date": str(self.date),
            "start_time": str(self.start_time),
            "end_time": str(self.end_time),
            "location": self.location,
            "details": self.details
        }
    
    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception:
            return "Unable to create event."
        return self

class Task(db.Model):
    __tablename__ = 'task'

    task_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable = False)
    name = db.Column(db.String(64), nullable = False)
    subcategory_id = db.Column(db.Integer, db.ForeignKey("subcategory.subcategory_id"), nullable = False)
    date = db.Column(db.Date, nullable = False)
    duration = db.Column(db.Integer, nullable = False)
    start_time = db.Column(db.Time, nullable = False)
    details = db.Column(db.String(254), nullable = False)

    def __init__(self, task_id, user_id, name, subcategory_id, date, duration, start_time, details):
        self.task_id = task_id
        self.user_id = user_id
        self.name = name
        self.subcategory_id = subcategory_id
        self.date = date
        self.duration = duration
        self.start_time = start_time
        self.details = details

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "user_id": self.user_id,
            "name": self.name,
            "subcategory_id": self.subcategory_id,
            "date": str(self.date),
            "duration": self.duration,
            "start_time": str(self.start_time),
            "details": self.details
        }
    
    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception:
            return "Unable to create task."
        return self
        
class Category(db.Model):
    __tablename__ = 'category'

    category_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable = False)
    name = db.Column(db.String(64), nullable = False)

    def __init__(self, user_id, name):
        self.name = name
        self.user_id = user_id

    def to_dict(self):
        return {
            "category_id": self.category_id,
            "user_id": self.user_id,
            "name": self.name
        }
    
    def add(self):
        db.session.add(self)
        db.session.commit()

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

    def add(self):
        db.session.add(self)
        db.session.commit()


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# LOGIN
# logging user in
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        name = data['name']
        username = data['username']
        password = data['password']
        print(data)
        db.session.add(event)
        db.session.commit()
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "message": "An error has occured while logging the user in",
                "error": str(e)
            }
        ), 500
    
    return jsonify(
        {
            "data": user.to_dict()
        }
    ), 201

# CREATE USER
# Creating and sending a new user to the database
@app.route("/users", methods=['POST'])
def addUser():
    try:
        data = request.get_json()
        user = User(**data)
        print(data)
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "message": "An error has occured while creating a new user",
                "error": str(e)
            }
        ), 500
    
    return jsonify(
        {
            "data": user.to_dict()
        }
    ), 201

# Retreiving users from the database
@app.route("/users")
def getUsers():
    user_list = User.query.all()
    if len(user_list) != 0:
        return jsonify(
            {
                "data": {
                    "users": [user.to_dict() for user in user_list]
                }
            }
        ), 200
    return jsonify(
        {
            "message": "No users found."
        }
    )


# EVENTS
# Creating and sending an event to the database
@app.route("/events", methods=['POST'])
def addEvent():
    try:
        data = request.get_json()
        event = Event(**data)
        print(data)
        db.session.add(event)
        db.session.commit()
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "message": "An error has occured while creating an event",
                "error": str(e)
            }
        ), 500
    
    return jsonify(
        {
            "data": event.to_dict()
        }
    ), 201

# Retreiving events from the database
@app.route("/events")
def getEvents():
    event_list = Event.query.all()
    if len(event_list) != 0:
        return jsonify(
            {
                "data": {
                    "events": [event.to_dict() for event in event_list]
                }
            }
        ), 200
    return jsonify(
        {
            "message": "No events found."
        }
    )

# TASKS
# Creating and sending a task to the database
@app.route("/tasks", methods=['POST'])
def addTask():
    try:
        data = request.get_json()
        task = Task(**data)
        db.session.add(task)
        db.session.commit()
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "message": "An error has occured while creating an task",
                "error": str(e)
            }
        ), 500
    
    return jsonify(
        {
            "data": task.to_dict()
        }
    ), 201

# Retreiving tasks from the database
@app.route("/tasks")
def getTasks():
    task_list = Task.query.all()
    if len(task_list) != 0:
        return jsonify(
            {
                "data": {
                    "tasks": [task.to_dict() for task in task_list]
                }
            }
        ), 200
    return jsonify(
        {
            "message": "No tasks found."
        }
    )


# CATEGORIES
# Creating and sending a category to the database
@app.route("/categories", methods=['POST'])
def addCategory():
    try:
        data = request.get_json()
        category = Category(**category)
        db.session.add(category)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "message": "An error has occured while creating a category",
                "error": str(e)
            }
        ), 500
    
    return jsonify(
        {
            "data": category.to_dict()
        }
    ), 201

# Retreiving categories from the database
@app.route("/categories")
def getCategories():
    category_list = Category.query.all()
    if len(category_list) != 0:
        return jsonify(
            {
                "data": {
                    "categories": [category.to_dict() for category in category_list]
                }
            }
        ), 200
    return jsonify(
        {
            "message": "No categories found."
        }
    )


# SUBCATEGORIES
# Creating and sending a subcategory to the database
@app.route("/subcategories", methods=['POST'])
def addSubcategory():
    try:
        data = request.get_json()
        subcategory = Subcategory(**subcategory)
        db.session.add(subcategory)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "message": "An error has occured while creating a subcategory",
                "error": str(e)
            }
        ), 500
    
    return jsonify(
        {
            "data": subcategory.to_dict()
        }
    ), 201

# Retreiving subcategories from the database
@app.route("/subcategories")
def getSubcategories():
    subcategory_list = Subcategory.query.all()
    if len(subcategory_list) != 0:
        return jsonify(
            {
                "data": {
                    "subcategories": [subcategory.to_dict() for subcategory in subcategory_list]
                }
            }
        ), 200
    return jsonify(
        {
            "message": "No subcategories found."
        }
    )

# Retreiving dictionary of subcategories names to id from the database
@app.route("/subcategoriesNameId")
def getSubcategoriesNameId():
    subcategory_list = Subcategory.query.all()
    if len(subcategory_list) != 0:
        return jsonify(
            {
                "data": {
                    "subcategories": [{"text": subcategory.name, "value" : subcategory.subcategory_id} for subcategory in subcategory_list]
                }
            }
        ), 200
    return jsonify(
        {
            "message": "No subcategories found."
        }
    )

if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    app.run()
