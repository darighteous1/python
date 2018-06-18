import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.students
grades = db.grades

query = {"type" : "homework"}
projection = {"_id" : 0, "type" : 0}

filteredScores = {}

scores = grades.find(query, projection).sort([("student_id", pymongo.ASCENDING), ("score", pymongo.DESCENDING)])

index = 0
for score in scores:
    if index % 2 == 1 :
        print("deleting")
        grades.remove(score)
    index = index + 1
    # student_id = score['student_id']

    # if score['student_id'] in filteredScores :
    #     if score['score'] > filteredScores[student_id] :
    #         filteredScores[student_id] = score['score']
    #         grades.remove({})
    
    # else :
    #     filteredScores[student_id] = score['score']