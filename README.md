# Twitter-feed-analysis
This script allows you to track tweets containing specific keywords and save the data to a CSV file. It uses the Twitter API and the Tweepy library to stream tweets in real-time and search for previous tweets from the same user containing the same keyword.

# Installation
1. Clone the repository: git clone `https://github.com/mz33-babu/twitter-feed-analysis.git`
2. Navigate to the directory: `cd twitter-analysis`
3. Install the required packages: `pip install -r requirements.txt`

# Configuration
Before running the script, you need to set up the following environment variables with your Twitter API credentials:

* `TWITTER_CONSUMER_KEY`
* `TWITTER_CONSUMER_SECRET`
* `TWITTER_ACCESS_TOKEN`
* `TWITTER_ACCESS_SECRET`

# Usage
To start tracking tweets containing specific keywords, run the following command:

```css
python main.py
```
By default, the script tracks the following keywords:

* 'Beispieltext'
* 'sample text'
* 'texte dexemple'

To track different keywords, modify the keywords list in the script to include the desired keywords.

The script will print the tweet details and search for previous tweets from the same user containing the same keyword. It will also save the data to a CSV file named `twitter_data.csv.`

To stop the script, press `Ctrl+C.`

