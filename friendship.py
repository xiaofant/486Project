import time
import tweepy
# pip install tweepy


auth = tweepy.OAuthHandler("6himHtojv9Yd4Fkd2xhPBiImb", 'ALAjI12cCnChFFBkN3gfQNc6jr02v5bEcpYQEscnYzgJ7wLbCV' )
auth.set_access_token('820682120-LiZvM5apLmGrryd1vm8AHanmcugfPnxsiTDLVkLv',  'BKn4KygkLTWsLSiTQZRkSI2rvgLNWaAfC1VU62MYGVyio')

api = tweepy.API(auth)

# Return true iff user1 is following user2
def is_following( user1, user2 ):
	relation = api.show_friendship(source_screen_name = user1, target_screen_name = user2)
	#relation = api.ShowFriendship(source_screen_name = user1, target_screen_name = user2)
	return relation[0].following
	#is_followed_by( user2, user1 )

print is_following('tcalkins90', 'CarmineZozzora')

# print "#" * 80
# print is_followed_by( "25073877", "2581703371" )
# print "#" * 80
# print is_followed_by( "2581703371", "25073877")
# print "#" * 80
