import os
import feedparser
from sql import db
from time import sleep, time
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from apscheduler.schedulers.background import BackgroundScheduler


api_id = ""   # Get it from my.telegram.org
api_hash = ""   # Get it from my.telegram.org
feed_url = ""   # RSS Feed URL of the site.
feed_url1 = ""   # RSS Feed URL of the site.
feed_url2 = ""   # RSS Feed URL of the site.
feed_url3 = ""   # RSS Feed URL of the site.
feed_url4 = ""   # RSS Feed URL of the site.
feed_url5 = ""   # RSS Feed URL of the site.
feed_url6 = ""   # RSS Feed URL of the site.
bot_token = ""   # Get it by creating a bot on https://t.me/botfather
log_channel = ""   # Telegram Channel ID where the bot is added and have write permission. You can use group ID too.
check_interval = 5   # Check Interval in seconds.  
max_instances = 5   # Max parallel instance to be used.
if os.environ.get("ENV"):   # Add a ENV in Environment Variables if you wanna configure the bot via env vars.
  api_id = os.environ.get("APP_ID")
  api_hash = os.environ.get("API_HASH")
  feed_url = os.environ.get("FEED_URL")
  feed_url1 = os.environ.get("FEED_URL1")
  feed_url2 = os.environ.get("FEED_URL2")
  feed_url3 = os.environ.get("FEED_URL3")
  feed_url4 = os.environ.get("FEED_URL4")
  feed_url5 = os.environ.get("FEED_URL5")
  feed_url6 = os.environ.get("FEED_URL6")
  bot_token = os.environ.get("BOT_TOKEN")
  log_channel = int(os.environ.get("LOG_CHANNEL", None))
  check_interval = int(os.environ.get("INTERVAL", 5))
  max_instances = int(os.environ.get("MAX_INSTANCES", 5))


if db.get_link(feed_url) == None:
   db.update_link(feed_url, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

def check_feed():
    FEED = feedparser.parse(feed_url)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url).link:
        if '720p' in entry.title or 'hdtv' in entry.title.lower() or 'galaxyrg' in entry.title.lower() or 'ddr' in entry.title.lower() or '480p' in entry.title.lower() or 'xvid' in entry.title.lower() or 'BRAZINO777' in entry.title  or 'armor' in entry.title.lower() or 'meguil' in entry.title.lower()  or 'mp4' in entry.title  or 'melbet' in entry.title.lower():
            message = f"{entry.link}"
        else:
                   # ↓ Edit this message as your needs.
            message = f"/mirror {entry.link}"
        try:
          app.send_message(log_channel, message)
          db.update_link(feed_url, entry.id)
        except FloodWait as e:
          print(f"FloodWait: {e.x} seconds")
          sleep(e.x)
        except Exception as e:
          print(e)
    else:
      print(f"Checked RSS FEED - TGx Movies")
      

if db.get_link(feed_url1) == None:
   db.update_link(feed_url1, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed1():
    FEED = feedparser.parse(feed_url1)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url1).link:
      if '720p' in entry.title or 'hdtv' in entry.title.lower() or 'galaxyrg' in entry.title.lower() or '480p' in entry.title.lower() or 'xvid' in entry.title.lower() or 'mvgroup' in entry.title.lower() or 'tgx' in entry.title.lower():
        message = f"{entry.link}"
      else:
                   # ↓ Edit this message as your needs.
        message = f"/dank {entry.link}"
      try:
        app.send_message(log_channel, message)
        db.update_link(feed_url1, entry.id)
      except FloodWait as e:
        print(f"FloodWait: {e.x} seconds")
        sleep(e.x)
      except Exception as e:
        print(e)
    else:
      print(f"Checked RSS FEED1 - TGx TV")    

if db.get_link(feed_url2) == None:
   db.update_link(feed_url2, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed2():
    FEED = feedparser.parse(feed_url2)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url2).link:
      if '720p' in entry.title or 'hdtv' in entry.title.lower() or 'galaxyrg' in entry.title.lower() or '480p' in entry.title.lower() or 'xvid' in entry.title.lower() or 'mvgroup' in entry.title.lower():
        message = f"{entry.link}"
      else:
                   # ↓ Edit this message as your needs.
        message = f"/dank {entry.link}"
      try:
        app.send_message(log_channel, message)
        db.update_link(feed_url2, entry.id)
      except FloodWait as e:
        print(f"FloodWait: {e.x} seconds")
        sleep(e.x)
      except Exception as e:
        print(e)
    else:
      print(f"Checked RSS FEED2 - TV Pack")  
     

if db.get_link(feed_url3) == None:
   db.update_link(feed_url3, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed3():
    FEED = feedparser.parse(feed_url3)
    entry = FEED.entries[0]
    if entry.link != db.get_link(feed_url3).link:
      if 'remux' in entry.title.lower():
        message = f"/kink {entry.enclosures[0]['href']}"
                   # ↓ Edit this message as your needs.
      else:
        message = f"/get {entry.enclosures[0]['href']}"
      try:
        app.send_message(log_channel, message)
        db.update_link(feed_url3, entry.link)
      except FloodWait as e:
        print(f"FloodWait: {e.x} seconds")
        sleep(e.x)
      except Exception as e:
        print(e)
    else:
      print(f"Checked RSS FEED3 - LHD REMUX")         
      

if db.get_link(feed_url4) == None:
   db.update_link(feed_url4, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed4():
    FEED = feedparser.parse(feed_url4)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url4).link:
        if '720p' in entry.title or 'hdtv' in entry.title.lower() or 'BRAZINO777' in entry.title or 'yts' in entry.title.lower() or 'avi' in entry.title.lower() or 'xvid' in entry.title.lower() or 'mp4' in entry.title or 'galaxyrg' in entry.title.lower()  or '480p' in entry.title.lower()  or 'armor' in entry.title.lower()  or 'domino' in entry.title.lower():
            message = f"Unwanted"
        else:
                   # ↓ Edit this message as your needs.
            message = f"/mirror {entry.enclosures[0]['href']}"
        try:
          app.send_message(log_channel, message)
          db.update_link(feed_url4, entry.id)
        except FloodWait as e:
          print(f"FloodWait: {e.x} seconds")
          sleep(e.x)
        except Exception as e:
          print(e)
    else:
      print(f"Checked RSS FEED4 - TorrentFunk Movies")        
      
if db.get_link(feed_url5) == None:
   db.update_link(feed_url5, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed5():
    FEED = feedparser.parse(feed_url5)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url5).link:
      if '720p' in entry.title or 'hdtv' in entry.title.lower() or 'avi' in entry.title.lower() or 'xvid' in entry.title.lower() or 'mp4' in entry.title or '480p' in entry.title.lower()  or 'xvid' in entry.title.lower():
                   # ↓ Edit this message as your needs.
        message = f"{entry.enclosures[0]['href']}"
      else:
        message = f"/dank {entry.enclosures[0]['href']}"
        try:
          app.send_message(log_channel, message)
          db.update_link(feed_url5, entry.id)
        except FloodWait as e:
          print(f"FloodWait: {e.x} seconds")
          sleep(e.x)
        except Exception as e:
          print(e)
    else:
      print(f"Checked RSS FEED5 - MeGusta")
      
        
if db.get_link(feed_url6) == None:
   db.update_link(feed_url6, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed6():
    FEED = feedparser.parse(feed_url6)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url6).link:
      if '1080p' in entry.title and 'erai' in entry.title.lower() or '1080p' in entry.title and 'asw' in entry.title.lower() and 'batch' in entry.title.lower() or '1080p' in entry.title and 'ssa' in entry.title.lower() and 'batch' in entry.title.lower() or '720p' in entry.title and 'ssa' in entry.title.lower() and 'batch' in entry.title.lower():
                   # ↓ Edit this message as your needs.
        message = f"/nani {entry.link}"
      else:
        message = f"noshit"
        try:
          app.send_message(log_channel, message)
          db.update_link(feed_url6, entry.id)
        except FloodWait as e:
          print(f"FloodWait: {e.x} seconds")
          sleep(e.x)
        except Exception as e:
          print(e)
    else:
      print(f"Checked RSS FEED6 - Nyaa")
        
            
scheduler = BackgroundScheduler()
scheduler.add_job(check_feed, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed1, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed2, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed3, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed4, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed5, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed6, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.start()
app.run()
