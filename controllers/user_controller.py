# users_controller.py

from flask import Flask, render_template, request, redirect, Blueprint
from models.user import User
import repositories.users_repository as user_repository

users_blueprint = Blueprint("users", __name__)

# INDEX
# GET '/users'
@users_blueprint.route("/users")
def users():
    users = user_repository.select_all()
    return render_template("users/index.html", users=users)

# NEW
# GET '/users/new'
@users_blueprint.route("/users/new", methods=['GET'])
def new_user():
    return render_template("users/new.html")

# CREATE
# POST '/users'
@users_blueprint.route("/users", methods=['POST'])
def create_user():
    name = request.form['name']
    email = request.form['email']
    user = User(name, email)
    user_repository.save(user)
    return redirect('/users')

# SHOW
# GET '/users/<id>'
@users_blueprint.route("/users/<id>")
def show_user(id):
    user = user_repository.select(id)
    events = user_repository.select_all_with_events(id)
    return render_template("users/show.html", user=user, events=events)

# DELETE
# DELETE '/users/<id>'
@users_blueprint.route("/users/<id>/delete", methods=['POST'])
def delete_user(id):
    user_repository.delete(id)
    return redirect('/users')

