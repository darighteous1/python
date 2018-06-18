import bottle
import pymongo

@bottle.route("/")
def index():
    connection = pymongo.MongoClient("localhost", 27017)
    db = connection.local
    students = db.students
    student = students.find_one()

    return "<b>Hello %s!</b>" % student["name"]

bottle.run(host="localhost", port=8082)