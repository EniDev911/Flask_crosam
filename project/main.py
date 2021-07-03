from flask import Blueprint, render_template
from . import db
import requests

main = Blueprint('main', __name__)

@main.route('/')
def index():
	print("ending")
	return render_template('index.html')

@main.route('/profile')
def profile():
	return render_template('profile.html')


