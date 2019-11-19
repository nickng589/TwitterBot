import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from keys import *
from youtube_ids import *

youtube = googleapiclient.discovery.build('youtube','v3',developerKey=yt_api_key)
def getSubs(channelID):
    request = youtube.channels().list(
        part="statistics",
        id=channelID
    )
    response = request.execute()
    return format(int(response.get("items")[0].get("statistics").get("subscriberCount")) , ",d")

def getViews(videoID):
    request = youtube.videos().list(
        part="statistics",
        id=videoID
    )
    response = request.execute()
    return format(int(response.get("items")[0].get("statistics").get('viewCount')), ",d")

if __name__ == '__main__' :
    print(getSubs(iZoneChannelID) + " subs for izone")
    print(getViews(violetaVideoID) + " views on violeta")

