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
import folium


class IpStack:
    """Api client for https://ipstack.com
    Methods that get API data always return JSON"""

    # private class attribute
    __base_url = "http://api.ipstack.com"

    # constructor
    def __init__(self, api_key):
        if not isinstance(api_key, str):
            raise TypeError('api_key is not a string!')
        self.ApiKey = api_key

    # private instance method
    def __deserialize_api_response(self, response):
        """Takes API response (it is in JSON string format) and de-serializes it to our object
        :param response: The web response from IpStack API"""
        if not isinstance(response, requests.models.Response):
            raise TypeError('response is not of type requests.models.Response!')
        r = response.json()
        self.ip = r['ip']
        self.type = r['type']
        self.continent_code = r['continent_code']
        self.continent_name = r['continent_name']
        self.country_code = r['country_code']
        self.country_name = r['country_name']
        self.region_code = r['region_code']
        self.region_name = r['region_name']
        self.city = r['city']
        self.zip = r['zip']
        self.latitude = r['latitude']
        self.longitude = r['longitude']
        self.location = IpStackLocation(r['location']['geoname_id'], r['location']['capital'],
                                        r['location']['country_flag'], r['location']['country_flag_emoji'],
                                        r['location']['country_flag_emoji_unicode'], r['location']['calling_code'],
                                        r['location']['is_eu'], r['location']['languages'])

    def get_current_ip_info(self):
        """:return: json string"""
        res = requests.get(f'{self.__base_url}/check?access_key={self.ApiKey}')
        self.__deserialize_api_response(res)
        return res.json()

    def get_ip_info(self, ip_or_hostname):
        """:param ip_or_hostname: IP address or hostname of target host - the IpStack API resolves the hostname for us
        :return: json string"""
        res = requests.get(f'{self.__base_url}/{ip_or_hostname}?access_key={self.ApiKey}')
        self.__deserialize_api_response(res)
        return res.json()

    def do_map_ip(self):
        """uses Folium to map lat/long of gathered IP"""
        if self.latitude is None or self.longitude is None:
            raise NotImplementedError("Attribute latitude OR longitude is None!")
        mappy = folium.Map(location=[self.latitude, self.longitude])


class IpStackLocation:
    """To help with data structure of api response"""
    def __init__(self, geoname_id: str, capital: str, country_flag: str, country_flag_emoji: str,
                 country_flag_emoji_unicode: str, calling_code: str, is_eu: str, languages: list):
        self.geoname_id = geoname_id
        self.capital = capital
        self.country_flag = country_flag
        self.country_flag_emoji = country_flag_emoji
        self.country_flag_emoji_unicode = country_flag_emoji_unicode
        self.calling_code = calling_code
        self.is_eu = is_eu
        self.languages = languages
