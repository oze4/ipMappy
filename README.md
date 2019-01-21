### -IN PROGRESS!-

Python package to gather metadata about public IP addresses, and then plot them using Florium (eventually)

The core API module relies on https://ipstack.com - so you will need an API key from there (for now)

###### Example:

```python
from ipMappy.ApiContext import IpStack

my_api_key = "abcdefg"

# main ipMappy object
ipstack = IpStack(my_api_key)

# Grab public info about IP or host
# The IpStack API will resolve hostnames for us
google_info = ipstack.get_ip_info('google.com')
print(google_info['ip'])
print(google_info['latitude'])
print(google_info['longitude'])
# The above will tie IP info to the 'google_info' variable in JSON string format
# The above command also de-serializes the JSON into our object
# Therefore, this is also valid
print(ipstack.ip)
print(ipstack.latitude)
print(ipstack.longitude)

# grab public IP info about the network -
# you are sending the request from
current_ip_info = ipstack.get_current_ip_info()
# Same as above, this method returns a JSON string as well as -
# de-serializing the JSON into our instance attributes
```

