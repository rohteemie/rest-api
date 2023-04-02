from flask import Blueprint, jsonify, request
from user_app import *
from flask_jwt_extended import jwt_required, create_access_token
from .models import User


api = Blueprint('api', __name__, url_prefix='/api')


# Create a JWT access token for the given user
def create_user_token(user: User) -> str:
    access_token = create_access_token(identity=user.id)
    return access_token

# Set the identity of the user for the JWT
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

# Load the user from the JWT identity
@jwt.user_loader_callback_loader
def user_loader_callback(identity):
    return User.query.get(identity)




# Create a new user
@api.route('/users', methods=['POST'])
def create_user() -> str:
    email = request.json['email']
    password = bcrypt.generate_password_hash(
        request.json['password']).decode('utf-8')
    name = request.json['name']

    user = User(email=email, password=password, name=name)
    db.session.add(user)
    db.session.commit()

    token = create_user_token(user)

    return jsonify({"access_token": token}), 201


@api.route('/')
def index():
    return jsonify({'key': 'value'})

