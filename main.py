from dotenv import dotenv_values
from glassnode import GlassnodeClient, GlassnodeClientException

def get_api_key():
    """
    Returns the Glassnode api key found in the .env file in the root directory.
    """
    config = dotenv_values()
    api_key = config.get("API_KEY")
    if not api_key:
        raise Exception("API key not found. Either no .env was found in the root directory or no API_KEY=value was found within it")
    return api_key


api_key = get_api_key()

client = GlassnodeClient(api_key)

client = GlassnodeClient(api_key)
since = 1468015200 # July 9 2016
until = 1589148000 # May 11 2020
resolution = "24h"
params = {
    "a": "BTC",
    "s": since,
    "u": until,
    "i": resolution
}

sth_nupl = client.get("indicators", "nupl_less_155", params)
lth_nupl = client.get("indicators", "nupl_more_155", params)