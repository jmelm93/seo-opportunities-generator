# encoding: utf-8

from api.google_search_console import GscClient

# from api.scrape import extract_url_data

from api.google import authenticate
from api.config import config

client = authenticate(config)
gscservice = GscClient(client)
