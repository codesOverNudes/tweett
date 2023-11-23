from flask import Flask, render_template, request, jsonify
import requests
from textblob import TextBlob
import json
from collections import Counter

app = Flask(__name__)

tweets_api_url = "http://localhost:5001/tweets"

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/analyze1', methods=['POST'])
def analyze1():
    if request.method == 'POST':
        querynumbr = int(request.form['querynumber'])
        try:
            response = requests.post(tweets_api_url, json={"querynumbr": querynumbr})
            response.raise_for_status()
            tweets = response.json().get('tweets', [])

            sentiment_counts = Counter()
            analyzed_tweets = []
            for tweet in tweets:
                analysis = TextBlob(tweet)
                sentiment = "Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral"
                sentiment_counts[sentiment] += 1
                analyzed_tweets.append({"text": tweet, "sentiment": sentiment})

            total_tweets = len(analyzed_tweets)
            positive_percentage = (sentiment_counts["Positive"] / total_tweets) * 100
            neutral_percentage = (sentiment_counts["Neutral"] / total_tweets) * 100
            negative_percentage = (sentiment_counts["Negative"] / total_tweets) * 100
            return render_template('result.html', results=analyzed_tweets,
                                   positive_percentage=positive_percentage,
                                   neutral_percentage=neutral_percentage,
                                   negative_percentage=negative_percentage)

        except requests.exceptions.HTTPError as errh:
            return f"HTTP Error: {errh}"

@app.route('/analyze2', methods=['POST'])
def analyze2():
    if request.method == 'POST':
        query = request.form['query']
        analysis = TextBlob(query)
        sentiment = "Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral"
        return render_template('result2.html', query=query, sentiment=sentiment)

if __name__ == '__main__':
    app.run(host='localhost',port=5000,debug=True)