#!/usr/bin/python
# -*- coding: utf-8 -*-

# generate these keys/tokens at https://dev.twitter.com/
my_auth = {
	'consumer_key' : 'REMOVED' 
	,'consumer_secret' : 'REMOVED'
	,'access_token_key' : 'REMOVED'
	,'access_token_secret' : 'REMOVED'
	}

loops = 1000

tweet_file = 'tweets.json'
map_file = 'tweets.html'

searchlist = [''] # all geo-enabled results
my_latlong = [47.3901151,8.5151409]
#my_address = 'Technoparkstrasse 1, 8005 Zürich, Switzerland'

dist_range = '1km' # 1 kilometer, or use '1mi'
