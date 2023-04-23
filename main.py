import requests

api_key = '6e126fadbd2540b2a2b7971d78823980'
url = 'https://newsapi.org/v2/everything?q=tesla&' \
      'from=2023-03-23&sortBy=publishedAt&apiKey=6e126fadbd2540b2a2b7971d78823980'

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access article title and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])
