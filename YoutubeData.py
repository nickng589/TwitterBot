import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from keys import *

youtube = googleapiclient.discovery.build('youtube','v3',developerKey=yt_api_key)
req = youtube.channels().list(part="statistics",id="UCOJplhB0wGQWv9OuRmMT-4g")
res = req.execute()
print(res.get("items")[0].get("statistics").get('viewCount'))
request = youtube.videos().list(
        part="statistics",
        id="XEOCbFJjRw0"
    )
response = request.execute()
print(response.get("items")[0].get("statistics").get('viewCount'))

def getSubs(channelID):
    request = youtube.channels().list(
        part="statistics",
        id=channelID
    )
    response = request.execute()
    print(response.get("items")[0].get("statistics").get("subscriberCount"))

iZoneChannelID = "UCe_oTYByLWQYCUmgmOMU_xw"
getSubs(iZoneChannelID)

