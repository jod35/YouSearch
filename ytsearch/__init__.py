from flask import Flask
from ytsearch.config import Devconfig

app=Flask(__name__)
app.config.from_object(Devconfig)
from ytsearch import routes
