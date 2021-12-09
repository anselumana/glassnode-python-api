from dotenv import dotenv_values

def get_api_key():
    """
    Returns the Glassnode api key found in the .env file in the root directory.
    """
    config = dotenv_values()
    api_key = config.get("API_KEY")
    if not api_key:
        raise Exception("API key not found. Either no .env was found in the root directory or no API_KEY=value was found within it")
    return api_key
