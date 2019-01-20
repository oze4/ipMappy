import requests


class IpStack:
    """
    Api client for https://ipstack.com
    Methods that get API data always return JSON
    """

    # private class attribute
    __base_url = "http://api.ipstack.com"

    def __init__(self, api_key):
        if not isinstance(api_key, str):
            raise TypeError("api_key is not a string!")
        self.ApiKey = api_key

    def __deserialize_api_response(self, response):
        """
        Takes API response (it is in JSON string format) and de-serializes it to our object
        :param response: The web response from IpStack API
        """
        self.ip = response['ip']
        self.type = response['type']
        self.continent_code = response['continent_code']
        self.continent_name = response['continent_name']
        self.country_code = response['country_code']
        self.country_name = response['country_name']
        self.region_code = response['region_code']
        self.region_name = response['region_name']
        self.city = response['city']
        self.zip = response['zip']
        self.latitude = response['latitude']
        self.longitude = response['longitude']
        self.location = IpStackLocation(response['location']['geoname_id'], response['location']['capital'],
                                        response['location']['country_flag'], response['location']['country_flag_emoji'],
                                        response['location']['country_flag_emoji_unicode'],
                                        response['location']['calling_code'], response['location']['is_eu'],
                                        response['location']['languages'])

    def get_current_ip_info(self):
        """
        The 'check' part in the URL below grabs the current IP
        :return: json string
        """
        res = requests.get(f'{self.__base_url}/check?access_key={self.ApiKey}').json()
        self.__deserialize_api_response(res)
        return res

    def get_ip_info(self, ip_or_hostname):
        """
        :param ip_or_hostname: IP address or hostname of target host - the IpStack API resolves
        the hostname for us
        :return: json string
        """
        res = requests.get(f'{self.__base_url}/{ip_or_hostname}?access_key={self.ApiKey}').json()
        self.__deserialize_api_response(res)
        return res


class IpStackLocation:
    """
    To help with data structure of api response
    """
    def __init__(self, geoname_id, capital, country_flag, country_flag_emoji,
                 country_flag_emoji_unicode, calling_code, is_eu, languages):
        self.geoname_id = geoname_id
        self.capital = capital
        self.country_flag = country_flag
        self.country_flag_emoji = country_flag_emoji
        self.country_flag_emoji_unicode = country_flag_emoji_unicode
        self.calling_code = calling_code
        self.is_eu = is_eu
        self.languages = languages

