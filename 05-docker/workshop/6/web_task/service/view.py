from app import app
from flask import  render_template, make_response
from flask import request
import pymysql
import news
from crypt import MakeCookie
def check(login,password):
    connection = pymysql.connect(
        host="mariadb",
        user="root",
        passwd="5up3r53cr37p45w0rd",
        db='test1'
    )
    cursor = connection.cursor()
    q = f"select * from users where username='{login}' and password='{password}'"
    data = cursor.execute(q)
    print(data)
    return data


    return 0
@app.route('/')
@app.route('/index')
def index():
    search = request.args.get('search')
    #print(search)
    if (search):
        return news.blueprint.index()
    #name = 'Ilia'
    return render_template('index.html')


@app.route('/about')
def about():
    search = request.args.get('search')
    
    if (search):
        return news.blueprint.index()
    return render_template('index.html')

@app.route('/contactus')
def contact():
    search = request.args.get('search')
    # print(search)
    if (search):
        return news.blueprint.index()
    return render_template('contactus.html')

@app.route('/admin',methods = ['GET','POST'])
def admin():
    search = request.args.get('search')
    # print(search)
    if (search):
        return news.blueprint.index()
    if (request.method == "GET"):
        return render_template('auth.html')
    login = request.form.get('username')
    password = request.form.get('password')
    login = login.replace(" ","")
    password = password.replace(" ","")
    print('login is {} password is {}'.format(login,password))
    if check(login,password):
        return render_template('admin.html',flag=open('flag_admin_sql.txt').read())
    else:
        return render_template('admin.html')

@app.route('/robots.txt')
def robots():
    return render_template('robots.txt')

@app.route('/develop',methods = ['GET','POST'])
def develop():
    search = request.args.get('search')
    # print(search)
    if (search):
        return news.blueprint.index()
    if (request.method == 'GET'):
        return render_template('develop.html')

    login = request.form.get('username')
    #print(login)
    #request.set
    resp = make_response(render_template('develop.html'))
    resp.set_cookie('test',MakeCookie(login))
    return resp

