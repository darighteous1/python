import re
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.word_cracker
table = db.words

def strip_line(line) :
    # (1, 'аванпост', 1, NULL, 0),
    line = re.sub(r"[(),']", "", line)
    line = line.split()
    
    word = {
        "_id" : line[1]
    }

    return word
    
fh = open("res\\words.txt", mode = "r", encoding = "utf-8")

words = []
for line in fh :
    words.append(strip_line(line))

fh.close()
table.insert_many(words, ordered=False)