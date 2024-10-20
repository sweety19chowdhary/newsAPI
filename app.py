from flask import Flask, render_template, request
import json
import requests
from datetime import datetime
import pytz
from collections import defaultdict

app = Flask(__name__)

API_KEY = '4a1c1c15e4e2ea25a97f7a1d11b53862'  
API_URL = 'https://gnews.io/api/v4/search'

@app.route('/')
def home():
    return render_template('index.html')  

@app.route('/search')
def search():
    query = request.args.get('q', 'example') 
    url = f"{API_URL}?q={query}&lang=en&country=us&max=10&apikey={API_KEY}"
    response = requests.get(url)

    
    print("Request URL:", url)  
    print("Response Status Code:", response.status_code)  
    print("Response Content:", response.text)  

    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])

 
        timezone = pytz.timezone('Asia/Kolkata')
        sorted_articles = sorted(articles, key=lambda x: x['publishedAt'], reverse=True)


        grouped_articles = defaultdict(list)
        for article in sorted_articles:
  
            utc_time = datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
            ist_time = utc_time.replace(tzinfo=pytz.utc).astimezone(timezone)

 
            date_str = ist_time.strftime('%Y-%m-%d')
            article['publishedAt'] = ist_time.strftime('%Y-%m-%d %H:%M:%S') 
            grouped_articles[date_str].append(article)


        final_articles = []
        for date, articles in grouped_articles.items():

            final_articles.extend(articles[:2])

        return render_template('results.html', articles=final_articles)
    else:
        return "Failed to fetch news", 500

if __name__ == '__main__':
    app.run(debug=True)
