### -IN PROGRESS!-

Python package to gather metadata about public IP addresses, and then plot them using Folium (eventually)

The core API module relies on https://ipstack.com - so you will need an API key from there (for now)

###### Example:

```python

from ipMappy.api import *

my_api_key = "abcdefg"

# main ipMappy object
ipstack = IpStack(my_api_key)

# Grab public info about IP or host - the IpStack API will resolve host names for us
google_info = ipstack.get_ip_info('google.com')
print(google_info.ip)
print(google_info.latitude)
print(google_info.longitude)

# Grab public IP info about the network which the request was sent from
current_ip_info = ipstack.get_current_ip_info()
print(current_ip_info)

```

