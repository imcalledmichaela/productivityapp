from flask import request, jsonify
from .models import Task, Event, Subcategory, Category, User
from flask import Blueprint
from .app import db
from datetime import datetime, timezone


app_routes = Blueprint('routes', __name__, url_prefix='/')


# sanity check route
@app_routes.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# @app_routes.route('/login', methods=['POST'])
# def login():
#     try:
#         data = request.get_json()
#         name = data['name']
#         username = data['username']
#         password = data['password']
#         print(data)
#         db.session.add(event)
#         db.session.commit()
#     except Exception as e:
#         print(str(e))
#         return jsonify(
#             {
#                 "message": "An error has occured while logging the user in",
#                 "error": str(e)
#             }
#         ), 500
    
    # return jsonify(
    #     {
    #         "data": user.to_dict()
    #     }
    # ), 201

# USERS
# Creating and sending a new user to the database
@app_routes.route("/users", methods=['POST'])
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
@app_routes.route("/users")
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
@app_routes.route("/events", methods=['POST'])
def addEvent():
    try:
        data = request.get_json()
        event = Event(**data)
        print(data)
        created_event = event.add()
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
@app_routes.route("/events")
def getEvents():
    event_list = Event.query.all()
    for event in event_list:
        print(event.start_time)
        print(type(event.start_time))
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
@app_routes.route("/tasks", methods=['POST'])
def addTask():
    try:
        data = request.get_json()
        task = Task(**data)
        # db.session.add(task)
        # db.session.commit()
        task.add()
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
@app_routes.route("/tasks")
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
@app_routes.route("/categories", methods=['POST'])
def addCategory():
    try:
        data = request.get_json()
        category = Category(**category)
        # db.session.add(category)
        # db.session.commit()
        category.add()
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
@app_routes.route("/categories")
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
@app_routes.route("/subcategories", methods=['POST'])
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
@app_routes.route("/subcategories")
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
@app_routes.route("/subcategoriesNameId")
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


@app_routes.route("/eventsWithParams", methods=['POST'])
def getEventsWithParams():
    print(request.data)
    data = request.get_json()
    print(data)
    
    start_time = data['start_time']
    start_date = datetime.fromisoformat(start_time[:-1]).astimezone(timezone.utc).date()
    end_time = data['end_time']
    end_date =  datetime.fromisoformat(end_time[:-1]).astimezone(timezone.utc).date()
    user = data['user']
    events_list = (db.session.query(Event).filter(Event.user_id == user)
                   .filter(Event.date >= start_time)
                   .filter(Event.date <= end_time).all())
    colors = {}
    for event in events_list:
        if event.subcategory_id not in colors:
            subcat = db.session.query(Subcategory).filter(Subcategory.subcategory_id == event.subcategory_id).one()
            colors[event.subcategory_id] = subcat.color
    print(events_list)
    if len(events_list) != 0:
        return jsonify(
            {
                "data": {
                    "events": [
                        {
                            "name": event.name,
                            "start": str(event.date) + "T" + str(event.start_time),
                            "end": str(event.date) + "T" + str(event.end_time), 
                            "color": colors[event.subcategory_id].lower()
                        } for event in events_list
                    ]
                }
            }
        ), 200
    return jsonify(
        {
            "message": "No events found."
        }
    ), 204

# @app_routes.route("/addData")
# def addData():
#     subcat = Subcategory('TestClass', 1, 'Red')
#     subcat.add()
#     return jsonify(), 200
