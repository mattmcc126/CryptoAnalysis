# Imports
# from coinbase.wallet.client import Client
from coinbase.rest import RESTClient
from dotenv import load_dotenv
import os

"""
    * Set up / loading util of CbAPI infomration with testing
"""
# Function to set up API with error handling
def init_API() -> tuple:
    # Initialize the client
    load_dotenv()
    key = os.getenv("API_ENV_KEY")
    secret = os.getenv("API_SECRET_ENV_KEY")

    try: 
        # pass keys in as args to restclient
        client = RESTClient(api_key=key, api_secret=secret)
        print("client connected")
        return True, client
    
    except Exception as e:
        # print error if not connected
        print(f"Not connected: {str(e)}")
        return False, None
    

# Test BTC price retrival functionality for RESTClient
def check_func(client) -> None:
    prod = client.get_product("BTC-USD")
    print(prod.price)
    return None


"""
    * Main function, test setup, calling main
"""

# Driver function
def main():
    # Fetch client and test
    test, client = init_API()

    # Check to see if client is initalized
    if not test:
        print("\n\n Client failed to initalize... \n Check API information and passing... \n")
        return 
    
    # If client is successfully initalized
    check_func(client)


# Calling main
if __name__ == "__main__":
    main()

