from base import db
from models.user import User
from flask import jsonify, request, render_template, Blueprint
from lib.utils import *

index_controller = Blueprint('index_controller', __name__)

@index_controller.route('/')
def index():
    return render_template('index.html', message = 'from controller')

@index_controller.route('/health')
def health():
    return ('', 200)

@index_controller.route('/sign_up')
def sign_up():
    if not check_params_exist(request, ['username', 'password']):
        return api_error('INVALID_REQUEST')

    uname = request.args.get('username')
    password = request.args.get('password')
    user = User.query.filter_by(username = uname).first()
    if (User.query.filter_by(username = uname).first()):
        return api_error('THIS_USER_HAS_BEEN_REGISTERED')
    db.session.add(User(uname, password))
    db.session.commit()
    return 'OK'

@index_controller.route('/sign_in')
def sign_in():
    if not check_params_exist(request, ['username', 'password']):
        return api_error('INVALID_REQUEST')

    uname = request.args.get('username')
    password = request.args.get('password')
    if uname is None or password is None:
        return api_error('INVALID_REQUEST')

    user = User.query.filter_by(username = uname).first()
    if user is None:
        return api_error('USER_NOT_FOUND')
    if not user.match(password):
        return api_error('WRONG_PASSWORD')
    return 'OK'
