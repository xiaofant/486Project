import tweepy
# API authentication
auth = tweepy.OAuthHandler("b65N756ehzXq8uRnxILyld9HR", 'FxNhSIgfBQ8JVPOizZBfkX61UPC5lv7oGkowZUeAeHo40LQDrT' )
auth.set_access_token('820682120-tKOcfWOtG1JVwcRPBQNLl1qlrki41D2ZeZ8YElYj',  'F5CPGWwGk1tybivXfGzFiFUXgrAEmtbkfXC90srOvaBZs')

api = tweepy.API(auth)
# return user ids of a bunch of usernames
def get_user_ids(useranmes):
    print 'get_user_ids'
    user_ids= []
    for i in range(len(useranmes)):
        user_object = api.get_user(useranmes[i])
        user_ids.append(user_object.id)
    return user_ids