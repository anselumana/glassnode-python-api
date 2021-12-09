import requests
from glassnode.consts import API_METRICS_URL
from glassnode.exceptions import GlassnodeClientException

class GlassnodeClient():
    """
    Glassnode API client.
    """

    def __init__(self, api_key):
        self.__api_key = api_key
    
    def get(self, domain: str, metric: str, params: dict = {}) -> dict:
        """
        Returns data for the given metric.\n
        The domain-metric pattern is the following:\n
            https://api.glassnode.com/v1/metrics/{domain}/{metric}\n
        Example:\n
            An asset's addresses count is under the following endpoint:\n
                 https://api.glassnode.com/v1/metrics/addresses/count\n
            domain: addresses\n
            metric: count\n
        See https://docs.glassnode.com for all the metrics available.
        """
        try:
            url = self.__get_url(domain, metric)
            self.__enrich_params(params)
            res = requests.get(url, params=params)
            if res.status_code != 200:
                self.__raise_exception(res)
            return res.json()
        except Exception as e:
            raise GlassnodeClientException(e) from None
    
    def __get_url(self, domain: str, metric: str) -> str:
        return f"{API_METRICS_URL}/{domain}/{metric}"
    
    def __enrich_params(self, params: dict):
        params["api_key"] = self.__api_key
    
    def __raise_exception(self, res: requests.Response):
        code = res.status_code
        text = res.text
        if code == 401:
            raise Exception(f"API responsed with a {code} status code (Unauthorized).")
        elif code == 404:
            raise Exception(f"API responsed with a {code} status code (Not found).")
        else:
            raise Exception(f"API responsed with a {code} status code.\n{text}")