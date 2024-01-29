import requests

api_key = "34bebf4dc50745fd811a8f4acf5abff8"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-12-29&sortBy=publishedAt&apiKey=34bebf4dc50745fd811a8f4acf5abff8"

# Make request
request = requests.get(url)

# Get a dictionary with dara
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])