import application.config as config
from flask import Flask, render_template, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


from .views import homepage_view

