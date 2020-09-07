from flask import Flask
from my_page import my_page
from post_page import post_page

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

app.register_blueprint(my_page, url_prefix='/my')
app.register_blueprint(post_page, url_prefix='/post')




if __name__ == '__main__':
    app.run()