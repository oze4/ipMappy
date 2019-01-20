from ipMappy.ApiContext import IpStack


# instantiate object
ips = IpStack("your_api_key_here")

# ExampleA - getting current ip info also de-serializes the response to our object
ips.get_current_ip_info()
print(ips.location.languages)

# ExampleB - you can also tie it to a var, as a json string
results = ips.get_current_ip_info()
print(results['location']['languages'])

# Both examples above return the same data
