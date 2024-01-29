import requests
from send_email import send_email

api_key = "34bebf4dc50745fd811a8f4acf5abff8"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-12-29&sortBy=publishedAt&apiKey=34bebf4dc50745fd811a8f4acf5abff8"

# Make request
request = requests.get(url)

# Get a dictionary with dara
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None and article["description"] is not None:
        body = body + article["title"] + "\n" + article["description"]\
              + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(mesg=body)