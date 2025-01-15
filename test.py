# Imports
from coinbase.wallet.client import Client
from dotenv import load_dotenv
import os

"""
Just a test to make sure my API is working
"""

# Initialize the client
load_dotenv()
key = os.getenv("API_KEY")
secret = os.getenv("API_SECRET")
client = Client(key, secret)

# Get the current spot price for Bitcoin (BTC) in USD
price = client.get_spot_price(currency_pair='BTC-USD')

# Print BTC price
print(f"Current BTC Price in USD: {price['amount']}")

