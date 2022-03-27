from flask import Blueprint
from flask import request, jsonify
from werkzeug.security import generate_password_hash
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies,
    jwt_required,
    get_jwt_identity)
from .models import User

bp = Blueprint('auth', __name__, url_prefix="/auth")

@bp.route('/register', methods=('POST',))
def register():
    data = request.get_json()
    name = data['name']
    username = data['username']
    email = data['email']
    password = data['password']

    user = User.query.filter_by(username=username).first()
    if user is None:
        user = User(
            name=name,
            username=username,
            email=email,
            password=generate_password_hash(password)
        )

        created_user = user.add()
        if created_user:
            access_token = create_access_token(identity=user.user_id)
            refresh_token = create_refresh_token(identity=user.user_id)

            response = jsonify({"message": "New user created!"})
            set_access_cookies(response, access_token)
            set_refresh_cookies(response, refresh_token)

            return response, 201
    return jsonify(
        {
            "message": "Unable to create user."
        }
    ), 400


@bp.route('/login', methods=('POST'))
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = User.authenticate(username, password)
    if user:
        access_token = create_access_token(identity=user.user_id)
        refresh_token = create_refresh_token(identity=user.user_id)

        response = jsonify({"message": f"{username} logged in."})
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)
        return response, 201
    return jsonify(
        {
            "message": "Invalid user details!"
        }
    ), 401


@bp.route('/logout', methods=('POST',))
@jwt_required
def logout():
    response = jsonify()
    unset_jwt_cookies(response)
    return response, 200


@bp.route('/refresh', methods=('POST',))
@jwt_required(refresh=True)
def refresh():
    user_id = get_jwt_identity()
    user = User.query.filter_by(user_id=user_id).first()
    access_token = create_access_token(identity=user.user_id)

    response = jsonify()
    set_access_cookies(response, access_token)

    return response, 201
