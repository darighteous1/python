
import pymongo

from pymongo import MongoClient


# connect to database
connection = MongoClient('localhost', 27017)

db = connection.local

# handle to names collection
names = db.students

item = names.find_one()

print (item['name'])

