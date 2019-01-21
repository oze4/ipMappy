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

import requests
from ipMappy.ip_info import MappyJSON


class IpStack:
    """Api client for https://ipstack.com
    Methods that get API data always return JSON"""

    __base_url = "http://api.ipstack.com"

    def __init__(self, api_key):
        if not isinstance(api_key, str):
            raise TypeError('api_key is not a string!')
        self.ApiKey = api_key

    def get_current_ip_info(self):
        """:return: MappyJSON object (JSON as dict)"""
        res = requests.get(f'{self.__base_url}/check?access_key={self.ApiKey}')
        return MappyJSON(res.json())

    def get_ip_info(self, ip_or_hostname):
        """:param ip_or_hostname: IP address or hostname of target host - the IpStack API resolves the hostname for us
        :return: MappyJSON object (JSON as dict)"""
        res = requests.get(f'{self.__base_url}/{ip_or_hostname}?access_key={self.ApiKey}')
        return MappyJSON(res.json())
