from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
print("API key loaded:", API_KEY)
print("SECRET loaded:", SECRET_KEY)

client = Client(API_KEY, SECRET_KEY)
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
client.timestamp_offset= -2000

def get_client():
    return client