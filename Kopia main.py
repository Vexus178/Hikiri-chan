import inspect
import os, sys
from imgurpython import ImgurClient
import webbrowser
import praw
import random

client_id = 'imgur id'
client_secret = 'imgur secret'
access_token = 'imgur token'
refresh_token = 'imgur refresh'
imgur_dictionary = None
with open("count.txt", "r") as coun:
	count = coun.read()
	coun.close()

client = ImgurClient(client_id, client_secret, access_token, refresh_token)
r = praw.Reddit('Hikiri', user_agent="Hikiri-chan by /u/Vexus178") 

def upload(client):
	lista = []
	filez = None
	filez = random.choice(os.listdir("photos"))
	with open("was_uploaded.txt", "r") as fi:
		lines = fi.readlines()
		for line in lines:
			lista.append(line.strip("\n"))
		fi.close()
	if filez in lista:
		print "Item was uploaded Before"
		return None
	else:
		with open("was_uploaded.txt", "a") as fi:
			fi.write(filez+"\n")
		fi.close()
	up = client.upload_from_path("photos/%s"% filez)
	print "Uploaded to "+up['link']
	return up

def submit(imgur_dictionary, r, count):
	count = unicode(int(count) + 1)
	subreddit = r.subreddit("reddit_api_test")
	title  = "Daily Photo #"+count
	post = subreddit.submit(title, url=imgur_dictionary['link'])
	post.reply("This Message is Generated by [Hikiri-chan](https://github.com/Vexus178/Hikiri-chan) written By /u/Vexus178")
	with open("count.txt", "w") as coun:
		coun.write(count.encode("utf-8"))
		coun.close()
	return True

if __name__ == '__main__':
	while not isinstance(imgur_dictionary, dict):
		imgur_dictionary = upload(client)
	submit(imgur_dictionary, r, count)
exit()
