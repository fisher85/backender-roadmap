from flask import Flask
from config import Configuration
from news.blueprint import news
global mysql
app = Flask(__name__)
app.config.from_object(Configuration)


app.register_blueprint(news,url_prefix='/news')

