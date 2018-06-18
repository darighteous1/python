import pymongo
import itertools
import tkinter as tk

# Initialize window
window = tk.Tk()
window.title("Word Cracker")
window.geometry("1200x400")

# Establish db connection
connection = pymongo.MongoClient("mongodb://localhost")
db = connection.word_cracker
dictionary = db.words

# Takes an input string of letters
# and returns a list of all available words
# "powerset([a,b,c]) --> () (a,) (b,) (c,) (a,b) (a,c) (b,c) (a,b,c)"
def generate_available_words():
    letters = list(word_input.get())
    length = length_input.get()

    if length == "" :
        length = len(letters)
    else :
        length = int(length)

    # This will generate only words
    # that use all provided letters
    # later we will choose the lenght of the words
    # up to the maximum of all available letters
    result = itertools.permutations(letters, length)
    
    words = []
    for word_tuple in result :
        word = ''.join(word_tuple)
        word_lookup = dictionary.find_one({"_id" : word})

        if (word_lookup is not None) :
            # word exists, add it to list of probable words
            words.append(word_lookup["_id"])
        # else : 
            # print (word, " does not exist")

    if len(words) == 0 :
        result = "Няма намерени думи с посочените параметри."
    else :
        words = set(words)
        result =  ", ".join(words)
    
    output.delete(0.0, tk.END)
    output.insert(tk.END, result)
    return

# Looks up a word in the dictionary
def lookup_word() :
    word = word_input.get()
    result = dictionary.find_one({"_id" : word})
    
    if result is None :
        result = "В речника няма такава дума."
    else : 
        result = "Вашата дума е: " + result["_id"]

    output.delete(0.0, tk.END)
    output.insert(tk.END, result)
    return

def close_window() :
    window.destroy()
    exit()

# Word input
tk.Label(window, text="Въведи букви:").grid(row=0, column=0, sticky=tk.W)
word_input = tk.Entry(window, width=20)
word_input.grid(row=1, column=0, sticky=tk.W)

# Length input
tk.Label(window, text="Дължина:").grid(row=0, column=1, sticky=tk.W)
length_input = tk.Entry(window, width=10)
length_input.grid(row=1, column=1, sticky=tk.W)

# Submit button
tk.Button(window, text="GO", width=5, command=generate_available_words).grid(row=1, column=2)

# Text
tk.Label(text="Възможни думи с въведените букви:").grid(row=4, column=0)
output = tk.Text(window, width=30, height=6, wrap=tk.WORD)
output.grid(row=5, column=0)

# Exit
tk.Label(text="").grid(row=6, column=0)
tk.Button(window, text="Exit", width=14, command=close_window).grid(row=7, column=0)

window.mainloop()

# res = dictionary.find_one({"word" : word})
# print (res)