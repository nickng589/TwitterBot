import tweepy
from keys import *
from youtubeData import *

# Authenticate to Twitter
def main():
    auth = tweepy.OAuthHandler(twitter_APIkey,
        twitter_APISecretKey)
    auth.set_access_token(twitter_AccessToken,
        twitter_AccessTokenSecret)

    api = tweepy.API(auth)

    subs = getSubs(iZoneChannelID) + " subs for izone"
    violetaviews = u'\U0001F48E' + "Violeta views: " + getViews(violetaVideoID)
    lverviews = u'\U0001F339' + "La Vie en Rose views: " + getViews(lverID)
    print(subs + "\n" + violetaviews)
    #api.update_status(subs + "\n" + violetaviews + "\n" + lverviews)
    #api.update_status(u'\U0001F600' + " emoji test")
    for status in api.user_timeline():
        print(status.id)

if __name__ == '__main__':
    main()
