from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://www.google.com')
'''
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/kellz_ocho/")
soup = BeautifulSoup(driver.page_source,"html.parser")
driver.quit()

for title in soup.select("._h9luf"):
    posts = title.select("._fd86t")[0].text
    follower = title.select("._fd86t")[1]['title']
    following = title.select("._fd86t")[2].text
    print("Posts: {}\nFollower: {}\nFollowing: {}".format(posts,follower,following))
    '''
