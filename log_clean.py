import re
from urllib.parse import urlparse
import requests
import hashlib

class Log_clean:
    def __init__(self):
        self.ip = None
        self.user = None
        self.is_email = False
        self.domain = None
        self.status = None
        self.status_verbose = None
        self.timestamp=None
        self.method=None
        self.schema=None
        self.host=None
        self.size=None
        self.size_k_b=None
        self.size_m_b=None
        self.url=None
        self.year=None
        self.month=None
        self.day=None
        self.day_of_week=None
        self.time=None
        self.country=None
        self.city=None
        self.session=None
        self.rest_vers=None

    def parse(self, line: str):
    
        regex = re.compile(r"(?P<ip>\S{7,15}) (?P<session>\S{1}|\S{15}) (?P<user>\S{1,50}) \[(?P<timestamp>\S{20}) "
                           r"(?P<utc>\S{5})\] \"(?P<method>GET|POST|DELETE|PATCH|PUT|HEAD) (?P<url>\S{1,9500}) "
                           r"(?P<version>\S{1,10})\" (?P<status>\d{3}) (?P<size>\d+) -")
        match = re.search(regex, line)
        self.ip = match.group("ip")
        self.user = match.group("user")
        self.status = match.group("status")
        self.session=match.group("session")
        self.method=match.group("method")
        self.size=match.group("size")
        self.url=match.group("url")
        
    
    
    def MD5(self, line: str):
            m=hashlib.md5()
            m.update(line.encode('utf-8'))
            self.id= m.hexdigest()
  

    def get_location(self, ip_adr: str):
            ip_address = ip_adr
            response = requests.get(f'https://ipapi.co/{self.ip}/json/').json()
            location_data = {
            "ip": ip_address,
            "city": response.get("city"),
            "region": response.get("region"),
            "country": response.get("country_name")
            }
            self.country=location_data.get("country")
            self.city=location_data.get("city")
       

    def TimeStamp(self, line: str):
        timestamp_regex = r'\[(\d{2})/(\w{3})/(\d{4}):(\d{2}):(\d{2}):(\d{2}) ([+-]\d{4})\]'
        match = re.search(timestamp_regex, line)
        self.timestamp=match.group().replace("[","").replace("]","")
      
    
    def rest_version(self, line: str):
        pattern = r'HTTP/(\d\.\d)'
        match = re.search(pattern, line)
        self.rest_vers=match.group()

        
    def __str__(self):
        return f"""
        timestamp:{self.timestamp}
        year:{self.year}
        month:{self.month}
        day:{self.day}
        day_of_week:{self.day_of_week}
        time:{self.time}
        ip: {self.ip}
        country:{self.country}
        city:{self.city}
        session:{self.session}
        user: {self.user}
        is_email: {self.is_email}
        domain: {self.domain}
        method:{self.method}
        url:{self.url}
        schema:{self.schema}
        host:{self.host}
        rest_version:{self.rest_vers}
        status: {self.status}
        status_verbose: {self.status_verbose}
        size:{self.size}
        size_k_b:{self.size_k_b}
        size_m_b:{self.size_m_b}
        """
