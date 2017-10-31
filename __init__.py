from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
from flaskext.markdown import Markdown

app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)

# migrations
migrate = Migrate(app, db)

# markdown
md = Markdown(app, extensions=['fenced_code', 'tables'])

from address import views