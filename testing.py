"""
MIT License
Copyright (c) 2019 Matthew Oestreich
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


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
