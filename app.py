import os

from flask import Flask, render_template, request
import concurrent.futures
from helpers import get_wiktionary_definition

app = Flask(__name__)

# A list to store hard words and their definitions
words = []

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        # Clears words if it has any words in it
        words.clear()
        # Read commonwords 
        with open("commonwords/commonwords.csv") as file:
            commonwords = set(file.read().lower().split())
        # Reads subtitle file data 
        subtitle_file = request.files['subtitle']
        if subtitle_file.filename.endswith(".srt"):
            subtitle_data = subtitle_file.read().decode('utf-8')
        else:
            # Returns an error if user didn't upload a subtitle data
            return render_template("upload.html", message="Your subtitle file must be .str", code="400")

        # Gets words from subtitle file data
        subtitle_words = {
            word.translate({ord(i): None for i in '/.,?!:->"'}).replace("<i", "").lower()
            for word in subtitle_data.split()
            if word.isalpha()
        }
        
        # Gets hard words in subtitle words
        hard_words = subtitle_words - commonwords
        
        # A list to store definitions of hard words
        definitions = []
        # I got help to create this code it is making 15 API calls at the same time and gets definitions faster
        with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
            results = executor.map(get_wiktionary_definition, hard_words)
        # Adds definitions into the definitions list
        for result in results:
            definitions.append(result)

        # Adds words, part of speech and definition of words into the words list
        for definition in definitions:
            for w, pos, defi in definition:
                if len(defi) > 2:
                    words.append([w, pos, defi])
        
        # Renders first page of uploaded words 
        return render_template("upload.html", words=words[0:30], length=range(len(words) // 30), curpage=1, totalpages=len(words) // 30)
    else:
        # Getting current page. If no file uploaded getting it as 0
        curpage = request.args.get('curpage', 0, type=int)
        # Defines the number of words that a page will contain
        wordinpage = 30
        # Defines starting element of words
        start = (curpage - 1) * wordinpage
        # Defines ending element of words
        end = start + wordinpage
        # Defines total pages
        totalpages = len(words) // wordinpage
        # Renders page of upload words and if words already uploaded it renders the selected page  
        return render_template("upload.html", words=words[start:end], length=range(totalpages), curpage=curpage, totalpages=totalpages)

# Renders home page
@app.route("/")
def index():
    return render_template("index.html")
# Runs website
if __name__ == '__main__':
    app.run(debug=True)