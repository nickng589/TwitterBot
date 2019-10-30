api_key = "AIzaSyDWkCQP2wT8rXzNDFR-T9Ru-PEVfLJzBc0"
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

youtube = googleapiclient.discovery.build('youtube','v3',developerKey=api_key)
req = youtube.channels().list(part="statistics",id="UCOJplhB0wGQWv9OuRmMT-4g")
res = req.execute()
print(res.get("items")[0].get("statistics").get('viewCount'))
request = youtube.videos().list(
        part="statistics",
        id="XEOCbFJjRw0"
    )
response = request.execute()
print(response.get("items")[0].get("statistics").get('viewCount'))

