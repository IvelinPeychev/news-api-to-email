import requests
from send_email import send_email

topic = 'tesla'

api_key = '6e126fadbd2540b2a2b7971d78823980'
url = 'https://newsapi.org/v2/everything?' \
      f'q={topic}&' \
      'from=2023-03-29&' \
      'sortBy=publishedAt&' \
      'apiKey=6e126fadbd2540b2a2b7971d78823980&' \
      'language=en'

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ''

# Access article title and description of the first 20 results
for article in content['articles'][:20]:
    if article['title'] is not None:
        body = 'Subject: The news today' + '\n' + body + article['title'] + '\n' + article['description'] + '\n' + article['url'] + 2*'\n'


body = body.encode('utf-8')
send_email(message=body)
