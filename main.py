import requests
from send_email import send_email

topic = "tesla"

api_key = "34bebf4dc50745fd811a8f4acf5abff8"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2023-12-29&sortBy=publishedAt&apiKey=34bebf4dc50745fd811a8f4acf5abff8&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with dara
content = request.json()

# Access the article titles and description
body = "Subject: Zaeds news"+"\n"
for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        body = body + article["title"] + "\n" + article["description"]\
              + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(mesg=body)

### Downloading image from web

# url = "www.wikipedia/cat.png"
# response = requests.get(url)
# with open("image.jpg", "wb") as file:
#     file.write(response.content)