from flask import Flask, render_template, request
import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("search.html")
@app.route('/', methods= ['POST'])
def getvalue():
    name = request.form['name']
    print(name)
    url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+name+'&ct=201326592&v=flip'
    result = requests.get(url)
    html = result.text
    pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
    i = 0

    for i in range(1, 5):
        print(pic_url[i])
        continue

        string = 'pictures'+name+'_'+str(i) + '.jpg'
        fp = open(string,'wb')
        fp.write(pic.content)
        fp.close()
        i += 1

    return render_template("search.html", p_url=pic_url)

def download_google(word):
    url = 'https://www.google.com/search?q=' + name + '&client=opera&hs=cTQ&source=lnms&tbm=isch&sa=X&ved=0ahUKEwig3LOx4PzKAhWGFywKHZyZAAgQ_AUIBygB&biw=1920&bih=982'
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')

    for raw_img in soup.find_all('img'):
           link = raw_img.get('src')
           os.system("wget " + link)

if __name__=='__main__':
    app.run(debug=True)
