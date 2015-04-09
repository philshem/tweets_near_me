#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Plots nearby tweets on an HTML map

To start a simple web server, navigate with command prompt to folder containing HTML file, and run:
> python -m SimpleHTTPServer 8000

Then with the browser, go to http://localhost/tweets.html
'''

import json, time
import twitter # https://github.com/bear/python-twitter
import folium # leaflet mapping library

import config # parameters

def get_twit(tweet_file, searchlist, geo, loops):

	with open(tweet_file,'wb') as outfile:
		
		for searchterm in searchlist:
			maxid = 100000000000000000000
			for i in xrange(loops):
				print searchterm, 'maxid',maxid,', twitter loop',i

				if i==0:
					results = api.GetSearch(searchterm,count=100,result_type='recent',geocode=geo)
				else:
					results = api.GetSearch(searchterm,count=100,result_type='recent',max_id=maxid,geocode=geo)

				tmpid = maxid
				for tweet in results:
					tweet = json.loads(str(tweet))
					maxid = tweet['id']
					json.dump(tweet,outfile)
					outfile.write('\n')

				if tmpid == maxid: # check that maxid has been updated
					print 'break'
					break
				time.sleep(10) # don't piss off twitter

def test_twit(tweet_file):

	with open(tweet_file,'rb') as infile: # read json file

		total = 0
		for line in infile:
			actual = json.loads(line)
			total += 1
			tweetid = int(actual[u'id'])

			created_at = actual[u'created_at']
			tmp_created= created_at.split()
			created_at = str(tmp_created[1]+' '+tmp_created[2]+', '+tmp_created[5]+' '+tmp_created[3])
			if total <= 1:
				print 'first tweet: ',created_at,'   tweetid =',tweetid

			screen_name = str(actual[u'user'][u'screen_name'])

			text = str(actual[u'text'].encode('utf8'))

	if total > 0:
		print 'last tweet: ',created_at,'   tweetid =',tweetid

	print total,'Total tweets'
	return total

def get_coords(my_address):

	from geopy.geocoders import Nominatim
	geolocator = Nominatim()
	location = geolocator.geocode(my_address)
	
	try:
		return (location.latitude, location.longitude)
	except:
		return None

def make_html(tweet_file, map_file, geo):
	
	my_coords = list(geo[0:2])
	my_range = geo[2]

	map_1 = folium.Map(location=my_coords, zoom_start=14)

	inserted = 0
	with open(tweet_file,'rb') as infile: # read json file

		for line in infile:

			actual = json.loads(line)

			tweet_id = int(actual[u'id'])

			tweet_latitude = None
			tweet_longitude = None

			for coordinates in actual.get(u'geo',''):
				if coordinates != 'type':
					tweet_latlong = []
					tweet_latlong = actual[u'coordinates'][u'coordinates']
					for item in tweet_latlong:
						tweet_longitude = tweet_latlong[0]
						tweet_latitude = tweet_latlong[1]

			if tweet_longitude is None or tweet_latitude is None:
				continue # go to next tweet, we are only interested in geo-enabled tweets

			# tweet data
			# it is against the Twitter API terms of service to share the tweet text
			tweet_created_at = actual[u'created_at']
			tmp_created= tweet_created_at.split()
			tweet_created_at = str(tmp_created[1]+' '+tmp_created[2]+', '+tmp_created[5]+' '+tmp_created[3])

			# user data
			user_screen_name = str(actual[u'user'][u'screen_name'])
			user_id = actual[u'user'][u'id']

			# construct an HTML doc for the popup
			url_base = 'https://twitter.com/'+user_screen_name+'/'

			html_packet =  '<a href="'+url_base+'">@'+str(user_screen_name)+'</a> <br>'
			html_packet +=  '<a href="'+url_base+'status/'+str(tweet_id)+'">Open tweet in browser</a> <br>'
			html_packet += tweet_created_at

			# working on embedding the tweet in an iframe
			# does not work
			#html_packet = '<html><body><iframe src="http://twitframe.com/show?url='+url_base+'"></iframe></body></html>' #<p>Your browser does not support iframes.</p></iframe></body></html>'
			# works
			#html_packet = '<html><body><iframe src="http://www.google.com/custom?q=&btnG=Search"></iframe></body></html><p>Your browser does not support iframes.</p></iframe></body></html>'

			# Add a simple_marker
			# simple_marker(self, location=None, popup='Pop Text', popup_on=True, marker_color='blue', marker_icon='info-sign', clustered_marker=False, icon_angle=0, width=300):
			map_1.simple_marker([tweet_latitude, tweet_longitude], popup=html_packet,marker_color='blue')

			inserted += 1

	if inserted > 0:
		map_1.simple_marker(my_coords, popup='That\'s me',marker_color='red') # drop a red marker on the origin
		#map_1.lat_lng_popover() # turn on lat/long click selection
		
		map_1.create_map(path=map_file)
		print 'Created map based on',inserted,'tweets within',my_range,'to :',my_coords
	else:
		print 'No tweets to display. No map created'

if __name__ == "__main__":

	api = twitter.Api(consumer_key=config.my_auth.get('consumer_key')
					,consumer_secret=config.my_auth.get('consumer_secret')
					,access_token_key=config.my_auth.get('access_token_key')
					,access_token_secret=config.my_auth.get('access_token_secret'))

	try:
		latlong = config.my_latlong
	except:
		latlong = get_coords(config.my_address)
	
	if latlong is None:
		print 'Did not geolocate the address you provided. Exiting.'
		exit(0)

	geo = list(latlong) + [config.dist_range]
	
	# download nearby tweets
	get_twit(config.tweet_file,config.searchlist,geo,config.loops)

	# count tweets
	tweets = test_twit(config.tweet_file)

	# make html map file
	if tweets > 0: 
		make_html(config.tweet_file, config.map_file, geo)
	else:
		print 'No tweets. No map.'

	# to do - add a date filter in the config (only go back 24 hours, etc)
	# to do - make zoom_start a function of all points
	# to do - make color of marker have gradient based on time


