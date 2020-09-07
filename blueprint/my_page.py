from flask import Flask, Blueprint

my_page = Blueprint('my_page', __name__)

@my_page.route('/')
def hello():
    return 'welcome'

@my_page.route('/mypage')
def my():
    return 'my-page'