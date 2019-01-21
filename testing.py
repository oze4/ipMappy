from ipMappy.ApiContext import *


# instantiate object
ips = IpStack("your_api_key_here")

# ExampleA - getting current ip info also de-serializes the response to our object
ips.get_current_ip_info()
print(ips.location.languages)

# ExampleB - you can also tie it to a var, as a json string
results = ips.get_current_ip_info()
print(results['location']['languages'])

# Both examples above return the same data
ip_stack_test = IpStackTest("83e165094b4d4f05f6aa904c4b6484db")
ans = ip_stack_test.get_curr_ip_data()
j_son = ans.json()
loaded = json.dumps(f'{ans.json()}')
print(j_son)
n = Utils.JSONtoOBJECT(j_son)
print(n.ip)
