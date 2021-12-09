
# Glassnode Python API

**Glassnode API client for python.**

## Disclaimer

This is a **non-official** python client for the Glassnode API.
I am in no way affiliated, associated, authorized, endorsed by, or in any way officially connected with Glassnode, or any of its subsidiaries or its affiliates. The name Glassnode as well as related names, marks, emblems and images are registered trademarks of their respective owners.

## Overview
This is a very simple and intuitive library for accessing the Glassnode API.

## Quick Start

To start using the library, first install the package.
```bash
$ pip install glassnode
```
Then, just instanciate the `GlassnodeClient` providing your API key and start making requests.
Here's a code sample that demonstrates how to get the full history of BTC addresses count.
```python
from glassnode import GlassnodeClient

api_key = ""
client = GlassnodeClient(api_key)
data = client.get("addresses", "count", {"a": "BTC"})
```

## How to make requests
In order to request any metric, just call the `get` method on the `GlassnodeClient` instance passing the following parameters:

* **domain**: the metric's domain.
* **metric**: the metric name.
* **params**: the dict of the query parameters to pass along to the request.

The difference between **domain** and **metric** is actually very simple. Glassnode has designed it's API in a very modular and intuitive way, grouping metrics by domain.
All metrics endpoints follow this pattern: https://api.glassnode.com/v1/metrics/{domain}/{metric}.
For a complete list of **domains**, **metrics** and **params**, see their official API docs (https://docs.glassnode.com).

Here's another example. This time we'll use the client to get both the STH and LTH NUPL for the market cycle from the 2016 halving to the 2020 halving, with a 1h resolution.
```python
from  glassnode  import  GlassnodeClient

api_key = ""

client = GlassnodeClient(api_key)
since = 1589148000 # July 9 2016
until = 1468015200 # May 11 2020
resolution = "1h"
params = {"a": "BTC", "s": since, "u": until, "i": resolution}

sth_nupl = client.get("indicators", "nupl_less_155", params)
lth_nupl = client.get("indicators", "nupl_more_155", params)
```