# app.py

from flask import Flask
from flask_mongoengine import MongoEngine
import urllib.parse

app = Flask(__name__)

# Replace 'your_database_name' with your actual database name
# Replace 'malik.951' with your actual password
password = "malik.951"
encoded_password = urllib.parse.quote(password)

app.config['MONGODB_SETTINGS'] = {
    'db': 'rooms_and_buildings',
    'host': f'mongodb+srv://david951:{encoded_password}@cluster0.pmjsby7.mongodb.net/?retryWrites=true&w=majority'
}
app.config['SECRET_KEY'] = 'blah'

db = MongoEngine(app)

# ... Other configurations, blueprints, and routes go here ...

def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
