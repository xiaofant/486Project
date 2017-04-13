import time
import tweepy
import MyStreamListener
# pip install tweepy


auth = tweepy.OAuthHandler("b65N756ehzXq8uRnxILyld9HR", 'FxNhSIgfBQ8JVPOizZBfkX61UPC5lv7oGkowZUeAeHo40LQDrT' )
auth.set_access_token('820682120-tKOcfWOtG1JVwcRPBQNLl1qlrki41D2ZeZ8YElYj',  'F5CPGWwGk1tybivXfGzFiFUXgrAEmtbkfXC90srOvaBZs')

api = tweepy.API(auth)


# Return true iff user1 is following user2
def following_users( user ):
	following_user_ids = api.friends_ids(user)
	#relation = api.ShowFriendship(source_screen_name = user1, target_screen_name = user2)
	return following_user_ids
	#is_followed_by( user2, user1 )

