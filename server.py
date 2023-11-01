# !C:/Users/nikit/AppData/Local/Programs/Python/Python312/python.exe

from bottle import run, route, template, static_file, request, get
from database import mycursor,db
from datetime import date


@route('/')
@route('/index')
def index():
    return template('index.html')

@route('/kuda')
def kuda():
    return template('kuda.html')

def index():
    return template('index.html')

@route("/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="./")

@route("/fonts/<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>")
def font(filepath):
    return static_file(filepath, root="fonts")
 
@route("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg|JPG)>")
def img(filepath):
    return static_file(filepath, root="images")

@route("/index", method='POST')
def save_data():
    name = request.forms.get("get_name")
    result = request.forms.get("goslin")
    time = date.today()
    mycursor.execute("INSERT INTO gosling_lit (name, result) VALUES (%s,%s,%s)", (name, result , time) ), db.commit()


@route("/data", method="POST")
def data():
    name = request.forms.get("get_name")
    result = request.forms.get("goslin")
    time = date.today()
    # для sqlite
    mycursor.execute("INSERT INTO gosling_lit (name, result, time) VALUES (?,?,?)", (name, result, time) )
    # для mysql
    # mycursor.execute("INSERT INTO gosling_lit (name, result) VALUES (%s,%s)", (name, result) )
    db.commit()

    # здесь я просто перевел из бд в список кортежей типа (имя, тип, id)
    mycursor.execute("SELECT * FROM gosling_lit")
    data = [x for x in mycursor]

    # в моем шаблоне вот эта инфа из бд будет доступна под названием goslings
    return template("data.html", goslings=data)

# @route("/data")
@get("/data") # @get - это сокращение для @route(..., method="GET")
def show_base():
    # все тоже самое, только без добавления в бдs

    mycursor.execute("SELECT * FROM gosling_lit")
    data = [x for x in mycursor]
    return template("data.html", goslings=data)


run(reloader=True, debug=True)