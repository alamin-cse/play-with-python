from flask import Flask

from myvsearch2 import search4letters
app = Flask(__name__)
@app.route('/')
def hello() -> str:
  return 'Hello world from Flask!'
@app.route('/search4')
def do_search() -> str:
  return str(search4letters('life, the universe, and the everything', 'eiru,!'))
app.run()