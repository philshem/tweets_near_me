# tweets near me

### Download nearby twitter activity and display tweets on an interactive map

![output map](http://i.imgur.com/BKf7Nt3.png)

**Requirements:**

1. Create authentication parameters for the [Twitter REST API](https://dev.twitter.com/rest/public)
2. Add those parameters to your config.py file
3. Modify the config.py file to include your address, OR your latitude/longitude. Also, add specific search terms if desired.
4. Generate tweets.html file by running 'python tweets_near_me.py'
5. To view HTML page, navigate with command prompt to the folder containing tweets.html, and start simple web server:
  
    python -m SimpleHTTPServer 8000

6. With browser, visit page [http://localhost:8000/tweets.html](http://localhost:8000/tweets.html)

---

**Dependencies:** (not including standard python libraries)

+ [Folium](folium.readthedocs.org/en/latest/) (Leaflet.js for Python)

         pip install folium

+ [Python-twitter](https://pypi.python.org/pypi/python-twitter/)

         pip install python-twitter

---

**To Do:**

+ Add a date filter in the config (only go back 24 hours, etc)
+ Make zoom_start a function of all points
+ Make color of marker have gradient based on time (most recent are darkest, oldest are faintest)
+ Embed tweet in iframe (or something)



