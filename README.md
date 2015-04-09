# tweets near me

Download nearby twitter activity and display tweets on a map

![output map](https://raw.github.com/username/projectname/branch/path/to/img.png)

Requirements:

1. Create authentication parameters for the [Twitter REST API](https://dev.twitter.com/rest/public)
2. Add those parameters to your config.py file
3. Modify the config.py file to include your address, OR your latitude/longitude. Also, add specific search terms if desired.
4. Generate tweets.html file by running 'python tweets_near_me.py'
5. To view HTML page, navigate with command prompt to the folder containing tweets.html, and start simple web server:
  
    python -m SimpleHTTPServer 8000

6. With browser, visit page http://localhost:8000/tweets.html

Dependencies:

    pip install folium
    pip install python-twitter

