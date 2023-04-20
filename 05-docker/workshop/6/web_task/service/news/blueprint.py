from distutils.command.config import config

from flask import Blueprint
from flask import render_template
news = Blueprint('news',__name__,template_folder='templates')
from flask import request
import pymysql


@news.route('/')
def index():
    query = request.args.get('search')
    print(query)
    connection = pymysql.connect(
        host="mariadb",
        user="root",
        passwd="5up3r53cr37p45w0rd",
        db='test1'
    )
    cursor = connection.cursor()
    if ( (query == None)or (query == '') ):
        data = cursor.execute("select title,content from news")
    else:
        q = f"select title,content from news where content like '%{query}%'"
        #print (q)
        data = cursor.execute(q)
    #data = cursor.execute("select * from news")
    #print(data)
    connection.close()

    return render_template('news/index.html',news = cursor)

