import requests
from send_email import send_email

api_key = '6e126fadbd2540b2a2b7971d78823980'
url = 'https://newsapi.org/v2/everything?q=tesla&' \
      'from=2023-03-28&sortBy=publishedAt&apiKey=6e126fadbd2540b2a2b7971d78823980'

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ''

# Access article title and description
for article in content['articles']:
    if article['title'] is not None:
        body = body + article['title'] + '\n' + article['description'] + 2*'\n'

body =body.encode('utf-8')
send_email(message=body)
