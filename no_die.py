from flask import *
from threading import Thread

app = Flask('')

def run():
  app.run(host='0.0.0.0', port=8080)

def no_die():
    t = Thread(target=run)
    t.start()
