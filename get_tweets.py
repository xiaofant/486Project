import random

import twitter
import pandas as pd
# pip install python-twitter
# pip install pandas


API = twitter.Api(consumer_key='6himHtojv9Yd4Fkd2xhPBiImb',
                      consumer_secret='ALAjI12cCnChFFBkN3gfQNc6jr02v5bEcpYQEscnYzgJ7wLbCV',
                      access_token_key='820682120-LiZvM5apLmGrryd1vm8AHanmcugfPnxsiTDLVkLv',
                      access_token_secret='BKn4KygkLTWsLSiTQZRkSI2rvgLNWaAfC1VU62MYGVyio')

date_since ="2016-09-05"
date_until = "2016-10-09"


# The city dataset is downloaded from:
# http://simplemaps.com/data/us-zips 
def find_cities_by_state( state, num ):
	fname = "city_dataset/" + state + "_Features_20170201.txt"
	fname = "uszips.csv"
	df = pd.read_csv( fname )

	df = df.ix[ df[ "state"] == state ]

	# get only one row for one city
	df = df.drop_duplicates( subset = "city" )


	# get random sample
	coords = df.sample( n = num )
	coords = coords.ix[ : , [ "city", "lat", "lng"] ]

	return coords


def find_tweets_by_coord( keyword, city ):
	return API.GetSearch( term = keyword, geocode=[ city["lat"], city["lng"], "15mi"], since = date_since, until = date_until )


def find_tweets_by_state( keyword, state = "MI", num = 15):
	coords = find_cities_by_state( state, num )
	print coords


	o = open( "tweets_" + state + ".txt", "a+" )


	df = pd.DataFrame( {"city":{}, "screen_name" : {}, "text":{} } )
	j = 0

	for i in coords.index:
		tweets = find_tweets_by_coord( keyword, coords.ix[ i, : ] )

		print tweets

		for js in tweets:
			try: 
				text = js.text 
				text = " <br> ".join( text.splitlines() ) # change new line to <br>
				o.write(  js.user.screen_name + ", " +  text + "\n" )
			except Exception as e:
				print "Error:", e

			df.loc[j] = [ coords.ix[i, "city"], 
					js.user.screen_name,
					text ]
			j+=1


	o.close()
	df.to_csv( "tweets_" + state + "_" + keyword.replace( " ", "_" ) + ".csv" )



def trump_and_hillary_tweets_for_state( state, num_cities ):
	find_tweets_by_state( "Trump", state, num_cities )
	find_tweets_by_state( "Hillary", state, num_cities )
	find_tweets_by_state( "Trump Hillary", state, num_cities )


# change state to get different state's data
trump_and_hillary_tweets_for_state( "MI", 10 )








