from flask import render_template,request
from ytsearch import app
from isodate import parse_duration
import requests


@app.route('/')
def index():
   search_url='https://www.googleapis.com/youtube/v3/search'
   video_url='https://www.googleapis.com/youtube/v3/videos'
   YOUTUBE_API_KEY='AIzaSyANWuXOl2VW56FzxBR1BxrF6DFrXoznE6s'

   if request.method=='POST':
         
   
        search_params={
            'key': YOUTUBE_API_KEY,
            'q': 'Avicii',
            'part': 'snippet',
                'maxResults':20,
                'type':'video'
        } 

        r= requests.get(search_url,params=search_params)

        results=r.json()['items']
   print(r.text) 
   video_ids=[] 
   for result in results:
       video_ids.append(result['id']['videoId'])



   video_params={
       'key':YOUTUBE_API_KEY,
       'id': ','.join(video_ids),
       'part': 'snippet,contentDetails',
       'maxResults':20
   }

   r=requests.get(video_url,params=video_params) 
   results=r.json()['items']
   videos=[]
   for result in results:
       video_data={
           'id': result['id'],
           'url': 'https://www.youtube.com/watch?v={}'.format(result['id']),
             'thumbnail': result['snippet']['thumbnails']['high']['url'],
             'title': result['snippet']['title'],
             'duration':parse_duration(result['contentDetails']['duration'])
             
       }
       videos.append(video_data)
   return render_template('index.html' ,videos=videos)

