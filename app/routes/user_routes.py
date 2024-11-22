# app/routes/user_routes.py
from flask import Blueprint, request, jsonify
from app.controllers.user_controller import UserController
from app.schemas.user_schema import UserSchema

user_bp = Blueprint("user_bp", __name__, url_prefix="/users")

user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Route to get all users
@user_bp.route("/", methods=["GET"])
def get_users():
    users = UserController.get_all_users()
    return users_schema.jsonify(users), 200

# Route to get a user by id
@user_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = UserController.get_user_by_id(user_id)
    if user:
        return user_schema.jsonify(user), 200
    return jsonify({"message": "User not found"}), 404

# Route to create a new user
@user_bp.route("/", methods=["POST"])
def add_user():
    data = request.get_json()
    new_user = UserController.create_user(data)
    return user_schema.jsonify(new_user), 201

# Route to update a user
@user_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    updated_user = UserController.update_user(user_id, data)
    if updated_user:
        return user_schema.jsonify(updated_user), 200
    return jsonify({"message": "User not found"}), 404

# Route to delete a user
@user_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    success = UserController.delete_user(user_id)
    if success:
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"message": "User not found"}), 404
