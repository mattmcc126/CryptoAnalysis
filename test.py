# Imports
from coinbase.wallet.client import Client
from dotenv import load_dotenv
import os

"""
    * Set up / loading util of CbAPI infomration with testing
"""
# Function to set up API with error handling
def init_API() -> tuple:
    # Initialize the client
    load_dotenv()
    key = os.getenv("API_KEY")
    secret = os.getenv("API_SECRET")
    client = Client(key, secret)
    if(client): 
        print("Init API success")
        return True, client
    else: 
        print("Init API failure")
        return False, client

# fetch price for testing to make sure bot can acess 
def fetch_price_test(client) -> None:
    # Get the current spot price for Bitcoin (BTC) in USD
    price = client.get_spot_price(currency_pair='BTC-USD')
    # Print BTC price
    print(f"Current BTC Price in USD: {price['amount']}")

"""
    * Main function, test setup """

# Driver function
def main():
    test, client = init_API()
    if(test):
        fetch_price_test(client)


if __name__ == "__main__":
    main()

