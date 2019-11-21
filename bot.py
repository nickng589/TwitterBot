import tweepy
from keys import *
from youtubeData import *
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

#set up today's date and time to be used
today = datetime.now()
date = today.strftime("%x")
time = today.strftime("%X")


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
    for status in api.user_timeline():
        print(status.id)
    data = open("data.txt", "a")
    writeData(data,"violetaViews",[violetaviews])
    data1, data2, data3, data4 = np.random.randn(4, 100)
    fig, ax = plt.subplots(1, 1)
    ax.set_facecolor("#3C3C3C")
    fig.set_facecolor("#C3B0DE")
    createGraph(ax, data1, data2, {'color': '#B6E3BC'})
    plt.show()

#format data as date, time, numbers


def writeData(file, tag, data):
    file.write("*"+tag + "\n")
    file.write(date + "\n")
    file.write(time + "\n")
    file.write("*end" + "\n")

def createGraph(ax, x, y, param_dict):
    out = ax.plot(x, y, **param_dict)
    return out

if __name__ == '__main__':
    main()
