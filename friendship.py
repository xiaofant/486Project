import time
import tweepy
# pip install tweepy


auth = tweepy.OAuthHandler("b65N756ehzXq8uRnxILyld9HR", 'FxNhSIgfBQ8JVPOizZBfkX61UPC5lv7oGkowZUeAeHo40LQDrT' )
auth.set_access_token('820682120-tKOcfWOtG1JVwcRPBQNLl1qlrki41D2ZeZ8YElYj',  'F5CPGWwGk1tybivXfGzFiFUXgrAEmtbkfXC90srOvaBZs')

api = tweepy.API(auth)


# get following users' id
def following_users( user ):
	print 'following_users'
	following_user_ids = api.friends_ids(user)
	return following_user_ids

