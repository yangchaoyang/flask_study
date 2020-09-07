from flask import Flask, Blueprint

post_page = Blueprint('post_page', __name__)

@post_page.route('/')
def post_list():
    return 'post-list'

@post_page.route('/postdetail')
def post_details():
    return 'post-detail'