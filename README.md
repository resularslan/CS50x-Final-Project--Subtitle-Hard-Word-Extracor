# Subtitles Hard Word Extractor
#### Video Demo:  https://www.youtube.com/watch?v=ozCD7tsdUb8&t=9s
#### Description: 
Subtitles hard word extractor is a web-based application using Python, Flask, HTML, CSS and JavaScript. 
It is a free website for users to upload their subtitles and learn hard words from it. 
Users don't need to register this website and they can use it with an internet connection. 
This project contains app.py, helpers.py, templates folder, commonwords folder and static folder. 
First helpers.py contains two functions named cleanString and get_wiktionary_definition. 
get_wiktionary_definition function gets word, part of speech and definitons of word that is given. 
And cleanString function cleans that word's definitions from <span> texts. 
Then app.py is running the flask server. And it has two functions named upload and index. 
index function renders the home page of the website. upload function if method is post, 
reads common words csv file, which I uploaded words from Oxford 3000 words and Learn English Team, 
and reads subtitle file that is uploaded by user if subtitle file is not str it renders an error code. 
After it read subtitle data it stores words from it in a set. Then it defines a set named hard words 
which is subtitle words subtracted to common words. With using concurrent.features and get_wiktionary_definiton 
it makes multiple calls to wiktionary api, which makes it faster, and it stores definition of hard words in a list
named definitions. And it stores every single words' name, part of speeches and definition in a list named words 
and renders page of uploaded words. If method is get, it gets current page and if no file uploaded getting it as 0.
Then it defines a number of words that a page will contain. Then it defines starting element of words, it defines 
ending element of page which will be start added to word in page, it defines total pages which will be the lenght of
words list divided by word in page, it renders current uploaded page if it is zero it means no file uploaded. 
Templates folder contains three html files named layout.html, index.html and upload.html. layout.html is very similar
to CS50 Finance's layout.html file. I got most of the things from it and I integrated it to my own website. 
The diffrences are my icon, navbar and as expected title. index.html is home page of Subtitles Hard Word Extractor.
It is introducing it to users and describing what it is, how to use and so on and so forth. 
Lastly upload.html contains a form that allows users to select their subtitle and below that there is a text that
saying which api is used to get definitions. There is a message and error code which tell user that they made an unwanted
attempt. There is table that contains words, their part of speeches and definitions. Lastly there is buttons to let user 
to go a specific page. Because there will be too many hard words I divided them into sections. Each page has 30 words. 
Static folder has 3 file. First of them is shwe.ico which is icon of my website. Second of them is shwe.webp which logo
of my website. Lastly styles.css contains adjustments of navbar and table. And the last folder is commonwords. 
As I said before it contains words from Oxford 3000 words and Learn English Team. This was my final project and this was CS50.