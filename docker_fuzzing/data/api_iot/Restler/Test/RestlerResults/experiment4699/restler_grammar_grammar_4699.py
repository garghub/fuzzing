""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies
req_collection = requests.RequestCollection([])
# Endpoint: /devices, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/AAYUSHGARGBU/api_iot/1.0.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("devices"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("skip="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: virtserver.swaggerhub.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/devices"
)
req_collection.add_request(request)

# Endpoint: /devices, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/AAYUSHGARGBU/api_iot/1.0.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("devices"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: virtserver.swaggerhub.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "uri":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["http://10.0.0.220:8080"]),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_fuzzable_uuid4("566048da-ed19-4cd3-8e0a-b7e0e1ec4d72", quoted=True, examples=["0729a580-2240-11e6-9eb5-0002a5d5c51b"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/devices"
)
req_collection.add_request(request)

# Endpoint: /lighting/dimmers/{deviceId}/{value}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/AAYUSHGARGBU/api_iot/1.0.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("lighting"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("dimmers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: virtserver.swaggerhub.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/lighting/dimmers/{deviceId}/{value}"
)
req_collection.add_request(request)

# Endpoint: /lighting/dimmers/{deviceId}/{value}/timer/{timeunit}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/AAYUSHGARGBU/api_iot/1.0.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("lighting"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("dimmers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("timer"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("units="),
    primitives.restler_fuzzable_group("units", ['seconds','minutes','milliseconds'] , default_enum="milliseconds" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: virtserver.swaggerhub.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/lighting/dimmers/{deviceId}/{value}/timer/{timeunit}"
)
req_collection.add_request(request)

# Endpoint: /lighting/switches/{deviceId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/AAYUSHGARGBU/api_iot/1.0.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("lighting"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("switches"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: virtserver.swaggerhub.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/lighting/switches/{deviceId}"
)
req_collection.add_request(request)

# Endpoint: /lighting/switches/{deviceId}/{value}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/AAYUSHGARGBU/api_iot/1.0.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("lighting"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("switches"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("value", ['True','False']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: virtserver.swaggerhub.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/lighting/switches/{deviceId}/{value}"
)
req_collection.add_request(request)

# Endpoint: /lighting/switches/{deviceId}/{value}/timer/{minutes}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/AAYUSHGARGBU/api_iot/1.0.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("lighting"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("switches"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("value", ['True','False']  ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("timer"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: virtserver.swaggerhub.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/lighting/switches/{deviceId}/{value}/timer/{minutes}"
)
req_collection.add_request(request)

# Endpoint: /lightingSummary, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/AAYUSHGARGBU/api_iot/1.0.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("lightingSummary"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: virtserver.swaggerhub.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/lightingSummary"
)
req_collection.add_request(request)

# Endpoint: /temperature, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/AAYUSHGARGBU/api_iot/1.0.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("temperature"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: virtserver.swaggerhub.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/temperature"
)
req_collection.add_request(request)

# Endpoint: /temperature/forecast/{days}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/AAYUSHGARGBU/api_iot/1.0.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("temperature"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("forecast"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: virtserver.swaggerhub.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/temperature/forecast/{days}"
)
req_collection.add_request(request)

# Endpoint: /temperature/{zoneId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/AAYUSHGARGBU/api_iot/1.0.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("temperature"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: virtserver.swaggerhub.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/temperature/{zoneId}"
)
req_collection.add_request(request)

# Endpoint: /temperature/{zoneId}/heater, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/AAYUSHGARGBU/api_iot/1.0.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("temperature"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("heater"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: virtserver.swaggerhub.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/temperature/{zoneId}/heater"
)
req_collection.add_request(request)

# Endpoint: /temperature/{zoneId}/heater/{state}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/AAYUSHGARGBU/api_iot/1.0.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("temperature"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("heater"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("state", ['False','True']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: virtserver.swaggerhub.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/temperature/{zoneId}/heater/{state}"
)
req_collection.add_request(request)

# Endpoint: /zones, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/AAYUSHGARGBU/api_iot/1.0.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("zones"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: virtserver.swaggerhub.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/zones"
)
req_collection.add_request(request)

# Endpoint: /zones/{zoneId}/quiet, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/AAYUSHGARGBU/api_iot/1.0.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("zones"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("zoneId", ['basement','first-floor','second-floor']  ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("quiet"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: virtserver.swaggerhub.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/zones/{zoneId}/quiet"
)
req_collection.add_request(request)
