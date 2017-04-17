import sys
import random
import unicodedata
import time
import twitter
import pandas as pd
# pip install python-twitter
# pip install pandas

API = twitter.Api(consumer_key='b65N756ehzXq8uRnxILyld9HR',
                      consumer_secret='FxNhSIgfBQ8JVPOizZBfkX61UPC5lv7oGkowZUeAeHo40LQDrT',
                      access_token_key='820682120-tKOcfWOtG1JVwcRPBQNLl1qlrki41D2ZeZ8YElYj',
                      access_token_secret='F5CPGWwGk1tybivXfGzFiFUXgrAEmtbkfXC90srOvaBZs')

radius = "15mi"
date_since ="2016-09-06"
date_until = "2016-10-10"


# The city dataset is downloaded from:
# http://simplemaps.com/data/us-zips
def find_cities_by_state( state, num ):
	fname = "uszips.csv"
	df = pd.read_csv( fname )



	df = df.ix[ df[ "state"] == state ]

	# get only one row for one city
	df = df.drop_duplicates( subset = "city" )


	# get random sample
	nrow = df.shape[0]
	num = min( nrow, num)
	coords = df.sample( n = num )
	coords = coords.ix[ : , [ "city", "lat", "lng"] ]

	return coords




def countdown(t):
	while t:
		mins, secs = divmod(t, 60)
		timeformat = '{:02d}:{:02d}'.format(mins, secs)
		sys.stdout.write( timeformat + "\r" )
		# sys.stdout.flush()
		time.sleep(1)
		t -= 1
	print 'Wait Done!\n'




def find_tweets_by_coord( keyword, city ):
	# find latitudes of city
	lat = str( city["lat"] )
	lng = str( city["lng"] )
	# query tweets
	query = "l=&q=" + keyword + "&geocode=" + lat + "%2C" + lng + "%2C" + radius + "&since%3A" + date_since + "%20until%3A" + date_until

	print query

	# wait for rate limit to go away
	while True:
		try:
			return API.GetSearch( raw_query = query )
		except Exception as e:
			print "Error Encounterd!", "#" * 60
			print e
			countdown( 15 * 60  )

def find_tweets_by_state( keyword, state, num, coords, o):

	for i in coords.index:
		tweets = find_tweets_by_coord( keyword, coords.ix[ i, : ] )

		print tweets

		for js in tweets:
			try:
				text = js.text
				text = " <br> ".join( text.splitlines() ) # change new line to <br>
				text = unicodedata.normalize( "NFKD", text).encode( "ascii", "replace" )
				o.write(  js.user.screen_name + ", " +  text + "\n" )
			except Exception as e:
				print "Error:", e




def trump_and_hillary_tweets_for_state( state = "MI", num_cities = 50 ):
	coords = find_cities_by_state( state, num_cities )

	o = open( "dataset/tweets_" + state + ".txt", "w" )
	# find tweets with specified keywords
	find_tweets_by_state( "Trump", state, num_cities, coords, o)
	find_tweets_by_state( "Hillary", state, num_cities, coords, o)
	find_tweets_by_state( "Trump Hillary", state, num_cities, coords, o)

	o.close()
if __name__ == '__main__':
	states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
	state = sys.argv[1]
	if state in states:
		trump_and_hillary_tweets_for_state(state, 50)
	else:
		print('Error: state is not valid')


