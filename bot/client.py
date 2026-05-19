import os
from dotenv import load_dotenv
from binance import Client
from binance.enums import *

load_dotenv()

api_key = os.getenv('API_KEY')
api_secret = os.getenv('SECRET_KEY')

client = Client(api_key, api_secret, testnet=True)



