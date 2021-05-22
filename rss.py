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
feed_url7 = ""   # RSS Feed URL of the site.
feed_url8 = ""   # RSS Feed URL of the site.
feed_url9 = ""   # RSS Feed URL of the site.
feed_url10 = ""   # RSS Feed URL of the site.
feed_url11 = ""   # RSS Feed URL of the site.
feed_url12 = ""   # RSS Feed URL of the site.
feed_url13 = ""   # RSS Feed URL of the site.
feed_url14 = ""   # RSS Feed URL of the site.
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
  feed_url7 = os.environ.get("FEED_URL7")
  feed_url8 = os.environ.get("FEED_URL8")
  feed_url9 = os.environ.get("FEED_URL9")
  feed_url10 = os.environ.get("FEED_URL10")
  feed_url11 = os.environ.get("FEED_URL11")
  feed_url12 = os.environ.get("FEED_URL12")
  feed_url13 = os.environ.get("FEED_URL13")
  feed_url14 = os.environ.get("FEED_URL14")
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
      print(f"Checked RSS FEED: {entry.id}")

if db.get_link(feed_url1) == None:
   db.update_link(feed_url1, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed1():
    FEED = feedparser.parse(feed_url1)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url1).link:
                   # ↓ Edit this message as your needs.
      message = f"/mirror {entry.link}"
      try:
        app.send_message(log_channel, message)
        db.update_link(feed_url1, entry.id)
      except FloodWait as e:
        print(f"FloodWait: {e.x} seconds")
        sleep(e.x)
      except Exception as e:
        print(e)
    else:
      print(f"Checked RSS FEED: {entry.id}")

if db.get_link(feed_url2) == None:
   db.update_link(feed_url2, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed2():
    FEED = feedparser.parse(feed_url2)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url2).link:
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
      print(f"Checked RSS FEED: {entry.id}")

if db.get_link(feed_url3) == None:
   db.update_link(feed_url3, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed3():
    FEED = feedparser.parse(feed_url3)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url3).link:
                   # ↓ Edit this message as your needs.
      message = f"/dank {entry.link}"
      try:
        app.send_message(log_channel, message)
        db.update_link(feed_url3, entry.id)
      except FloodWait as e:
        print(f"FloodWait: {e.x} seconds")
        sleep(e.x)
      except Exception as e:
        print(e)
    else:
      print(f"Checked RSS FEED: {entry.id}")    

if db.get_link(feed_url4) == None:
   db.update_link(feed_url4, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed4():
    FEED = feedparser.parse(feed_url4)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url4).link:
                   # ↓ Edit this message as your needs.
      message = f"/dank {entry.link}"
      try:
        app.send_message(log_channel, message)
        db.update_link(feed_url4, entry.id)
      except FloodWait as e:
        print(f"FloodWait: {e.x} seconds")
        sleep(e.x)
      except Exception as e:
        print(e)
    else:
      print(f"Checked RSS FEED: {entry.id}")      

if db.get_link(feed_url5) == None:
   db.update_link(feed_url5, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)     
      
def check_feed5():
    FEED = feedparser.parse(feed_url5)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url5).link:
                   # ↓ Edit this message as your needs.
      message = f"/mirror {entry.link}"
      try:
        app.send_message(log_channel, message)
        db.update_link(feed_url5, entry.id)
      except FloodWait as e:
        print(f"FloodWait: {e.x} seconds")
        sleep(e.x)
      except Exception as e:
        print(e)
    else:
      print(f"Checked RSS FEED: {entry.id}")     

if db.get_link(feed_url6) == None:
   db.update_link(feed_url6, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed6():
    FEED = feedparser.parse(feed_url6)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url6).link:
                   # ↓ Edit this message as your needs.
      message = f"/mirror {entry.link}"
      try:
        app.send_message(log_channel, message)
        db.update_link(feed_url6, entry.id)
      except FloodWait as e:
        print(f"FloodWait: {e.x} seconds")
        sleep(e.x)
      except Exception as e:
        print(e)
    else:
      print(f"Checked RSS FEED: {entry.id}")   

if db.get_link(feed_url7) == None:
   db.update_link(feed_url7, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed7():
    FEED = feedparser.parse(feed_url7)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url7).link:
                   # ↓ Edit this message as your needs.
      message = f"/dank {entry.link}"
      try:
        app.send_message(log_channel, message)
        db.update_link(feed_url7, entry.id)
      except FloodWait as e:
        print(f"FloodWait: {e.x} seconds")
        sleep(e.x)
      except Exception as e:
        print(e)
    else:
      print(f"Checked RSS FEED: {entry.id}")  
      

if db.get_link(feed_url8) == None:
   db.update_link(feed_url8, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed8():
    FEED = feedparser.parse(feed_url8)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url8).link:
                   # ↓ Edit this message as your needs.
      message = f"/dank {entry.link}"
      try:
        app.send_message(log_channel, message)
        db.update_link(feed_url8, entry.id)
      except FloodWait as e:
        print(f"FloodWait: {e.x} seconds")
        sleep(e.x)
      except Exception as e:
        print(e)
    else:
      print(f"Checked RSS FEED: {entry.id}")  
      

if db.get_link(feed_url9) == None:
   db.update_link(feed_url9, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed9():
    FEED = feedparser.parse(feed_url9)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url9).link:
                   # ↓ Edit this message as your needs.
      message = f"/mirror {entry.link}"
      try:
        app.send_message(log_channel, message)
        db.update_link(feed_url9, entry.id)
      except FloodWait as e:
        print(f"FloodWait: {e.x} seconds")
        sleep(e.x)
      except Exception as e:
        print(e)
    else:
      print(f"Checked RSS FEED: {entry.id}")  


if db.get_link(feed_url10) == None:
   db.update_link(feed_url10, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed10():
    FEED = feedparser.parse(feed_url10)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url10).link:
                   # ↓ Edit this message as your needs.
      message = f"/mirror {entry.link}"
      try:
        app.send_message(log_channel, message)
        db.update_link(feed_url10, entry.id)
      except FloodWait as e:
        print(f"FloodWait: {e.x} seconds")
        sleep(e.x)
      except Exception as e:
        print(e)
    else:
      print(f"Checked RSS FEED: {entry.id}")        
      

if db.get_link(feed_url11) == None:
   db.update_link(feed_url11, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed11():
    FEED = feedparser.parse(feed_url11)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url11).link:
                   # ↓ Edit this message as your needs.
      message = f"/dank {entry.link}"
      try:
        app.send_message(log_channel, message)
        db.update_link(feed_url11, entry.id)
      except FloodWait as e:
        print(f"FloodWait: {e.x} seconds")
        sleep(e.x)
      except Exception as e:
        print(e)
    else:
      print(f"Checked RSS FEED: {entry.id}")  
      

if db.get_link(feed_url12) == None:
   db.update_link(feed_url12, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed12():
    FEED = feedparser.parse(feed_url12)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url12).link:
                   # ↓ Edit this message as your needs.
      message = f"/mirror {entry.link}"
      try:
        app.send_message(log_channel, message)
        db.update_link(feed_url12, entry.id)
      except FloodWait as e:
        print(f"FloodWait: {e.x} seconds")
        sleep(e.x)
      except Exception as e:
        print(e)
    else:
      print(f"Checked RSS FEED: {entry.id}")        

if db.get_link(feed_url13) == None:
   db.update_link(feed_url13, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed13():
    FEED = feedparser.parse(feed_url13)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url13).link:
                   # ↓ Edit this message as your needs.
      message = f"/get {entry.links[1]['href']}"
      try:
        app.send_message(log_channel, message)
        db.update_link(feed_url13, entry.id)
      except FloodWait as e:
        print(f"FloodWait: {e.x} seconds")
        sleep(e.x)
      except Exception as e:
        print(e)
    else:
      print(f"Checked RSS FEED: {entry.id}")         
      
if db.get_link(feed_url14) == None:
   db.update_link(feed_url14, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed14():
    FEED = feedparser.parse(feed_url14)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url14).link:
                   # ↓ Edit this message as your needs.
      message = f"/mirror {entry.link}"
      try:
        app.send_message(log_channel, message)
        db.update_link(feed_url14, entry.id)
      except FloodWait as e:
        print(f"FloodWait: {e.x} seconds")
        sleep(e.x)
      except Exception as e:
        print(e)
    else:
      print(f"Checked RSS FEED: {entry.id}")
      
scheduler = BackgroundScheduler()
scheduler.add_job(check_feed, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed1, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed2, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed3, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed4, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed5, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed6, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed7, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed8, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed9, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed10, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed11, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed12, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed13, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed14, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.start()
app.run()
