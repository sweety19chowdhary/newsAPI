from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)

API_KEY = '4a1c1c15e4e2ea25a97f7a1d11b53862'  # Replace with your actual API key
API_URL = 'https://gnews.io/api/v4/search'

@app.route('/')
def home():
    return render_template('index.html')  # Ensure you have an index.html in your templates folder

@app.route('/search')
def search():
    query = request.args.get('q', 'example')  # Default search term is 'example'
    url = f"{API_URL}?q={query}&lang=en&country=us&max=10&apikey={API_KEY}"
    response = requests.get(url)

    # Debugging output
    print("Request URL:", url)  # Print the URL being requested
    print("Response Status Code:", response.status_code)  # Print the status code
    print("Response Content:", response.text)  # Print the content of the response

    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        return render_template('results.html', articles=articles)
    else:
        return "Failed to fetch news", 500
if __name__ == '__main__':
    app.run(debug=True)
