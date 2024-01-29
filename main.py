import requests

api_key = "34bebf4dc50745fd811a8f4acf5abff8"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-12-29&sortBy=publishedAt&apiKey=34bebf4dc50745fd811a8f4acf5abff8"

request = requests.get(url)
content = request.text
print(content)