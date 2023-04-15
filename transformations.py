import re
from urllib.parse import urlparse
from abc import ABC, abstractmethod
from logclean import Log_clean
from datetime import datetime, timedelta
from urllib.parse import urlparse
import socket
import requests
#from ip2geotools.databases.noncommercial import DbIpCity
import geoip2.database
import http


class BaseTransformation:
    
    @abstractmethod
    def transform(self, log: Log_clean) -> Log_clean:
        raise NotImplementedError
    


class UserTransformation(BaseTransformation):

 def transform(self, log: Log_clean) -> Log_clean:
        if domain := self.get_domain_from_email(log.user):
            log.is_email = True
            log.domain = domain
        return log

 def get_domain_from_email(self, user: str) -> str | None:
        regex = re.compile(r"\S+@(?P<domain>\S+.\S+)")
        if match := re.search(regex, user):
            return match.group("domain")
        return None



class UrlTransformation(BaseTransformation):

      def get_schema_host_from_url(self, log: Log_clean) -> Log_clean:
        parsed_url = urlparse(log.url)
        log.schema = parsed_url.scheme
        log.host = parsed_url.netloc
        return log


class IPTransformation(BaseTransformation):

      def get_country_city_from_IP(self, log: Log_clean) -> Log_clean:
          #reader = geoip2.database.Reader('GeoLite2-City.mmdb')
          #response = reader.city(log.ip)
          #log.country=response.country.name
          #log.city=response.city.name
          #return log
          #res = DbIpCity.get(log.ip, api_key="free")
          #log.country = res.country
         # log.city = res.city
         return log

class TimeTransformation(BaseTransformation):

      def Time_UTC_O(self, log: Log_clean) -> Log_clean:
        timestamp=datetime.strptime(log.timestamp,"%d/%b/%Y:%H:%M:%S %z")
        utc_offset = timedelta(hours=0)
        utc_time_stamp=timestamp - timestamp.utcoffset() + utc_offset
        utc_str = utc_time_stamp.strftime("%d/%b/%Y:%H:%M:%S")
        log.timestamp=utc_str
        log.year=utc_time_stamp.year
        log.day=utc_time_stamp.day
        log.day_of_week=utc_time_stamp.strftime('%A')
        log.month=utc_time_stamp.strftime('%B')
        log.time=utc_time_stamp.time()
        return log

class StatusCodeTransformation(BaseTransformation):

    def transform(self, log: Log_clean) -> Log_clean:
        try:
            log.status_verbose = http.HTTPStatus(int(log.status)).phrase
        except:
            log.status_verbose="Invalide status"
        return log
    


class sizeTransformation(BaseTransformation):

    def kilo_mega_bytes(self, log: Log_clean) -> Log_clean:
        size_kilo_bytes=int(log.size)/1024
        log.size_k_b=size_kilo_bytes
        size_mega_bytes=int(log.size)/(1024*1024)
        log.size_m_b=size_mega_bytes
        return log