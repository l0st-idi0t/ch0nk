from flask import *
from no_die import *

no_die()

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')
