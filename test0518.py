from flask import Flask, render_template, request, session, redirect
import requests, re
from bs4 import BeautifulSoup
from datetime import date, timedelta
import pymysql
from konlpy.tag import Kkma

app = Flask(__name__, template_folder='templatestest')
app.env = 'development'
app.debug = True
app.secret_key = 'junoh'

@app.route('/')
def index():
    return "test0518"

@app.route('/news/ranking', methods=['get','post'])
def newsranking():
    if request.method == "GET":
        return render_template("daumnewstest.html")

    def get_news_title(day=''):
        url = 'https://media.daum.net/ranking/'
        query = {'regDate': day}
        res = requests.get(url, params=query)
        soup = BeautifulSoup(res.content, 'html.parser')

        extracts = [dict(
        title=re.sub('\s+', ' ', a.get_text().replace('\n', '')),
        link=a['href']   
        ) for a in soup.select('a.link_txt')]
        return extracts
    
    day = request.form.get('day')
    
    # day = [date.today()-timedelta(day=i+1) 
    #         for i in range(int(day))]  
    # print(day)
    
    extracts = get_news_title(day)


    return render_template("daumnewstest.html", soup=extracts)

@app.route('/news/words')
def get_news(article_number=''):
    print(request.args.get('url'))
    url = request.args.get('url')
    words=[]
    
   
    return render_template('word_count_test.html', words=words)

app.run()

