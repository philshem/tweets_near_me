# tweets near me

### Download nearby twitter activity and display tweets on an interactive map

![output map](http://i.imgur.com/BKf7Nt3.png)

**Requirements:**

1. Create authentication parameters for the [Twitter REST API](https://dev.twitter.com/rest/public) and add them to your *config.py* file
2. Modify the *config.py* file to include your address

        my_address = 'Technoparkstrasse 1, 8005 Zürich, Switzerland'   
  
  Or your latitude/longitude
  
       my_latlong = [47.3901151,8.5151409]

3. Add specific search terms to *config.py*. Only geo-enabled tweets will be returned
 
         searchlist = ['dataviz','opendata'] 
 
4. Generate tweets.html file by running `python tweets_near_me.py`
5. To view HTML page, navigate with command prompt to the folder containing tweets.html, and start simple web server:
  
          python -m SimpleHTTPServer 8000

6. With browser, visit page [http://localhost:8000/tweets.html](http://localhost:8000/tweets.html)

---

**Dependencies:** (not including standard python libraries)

+ [Folium](folium.readthedocs.org/en/latest/) (Leaflet.js for Python)

         pip install folium

+ [Python-twitter](https://pypi.python.org/pypi/python-twitter/)

         pip install python-twitter

+ [geopy](https://pypi.python.org/pypi/geopy/)

        pip install geopy

---

**To Do:**

+ Add a date filter in the config (only go back 24 hours, etc)
+ Make zoom_start a function of all points
+ Make color of marker have gradient based on time (most recent are darkest, oldest are faintest)
+ Embed tweet in iframe (or something)



