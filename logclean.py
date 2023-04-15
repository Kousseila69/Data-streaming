import re
from urllib.parse import urlparse

#class Log_clean:
 #   def __init__(self, ip="", user="", timestamp="", utc="", method="", url="", rest_vers="", status="", size=""):
     #       self.ip = ip
    #        self.user = user
    #        self.timestamp = timestamp
    #        self.utc = utc
     #       self.method = method
      #      self.url = url
    #        self.rest_vers = rest_vers
       #     self.status = status
       #     self.size = size
   #     self.schema = ""

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
        self.version=None
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
        self.rest_ver=None


    def parse(self, line: str):
        print(f"parsing --> {line}")
        regex = re.compile(r"(?P<ip>\S{7,15}) (?P<session>\S{1}|\S{15}) (?P<user>\S{1,50}) \[(?P<timestamp>\S{20}) "
                           r"(?P<utc>\S{5})\] \"(?P<method>GET|POST|DELETE|PATCH|PUT) (?P<url>\S{1,4500}) "
                           r"(?P<version>\S{1,10})\" (?P<status>\d{3}) (?P<size>\d+) -")
       
        match = re.search(regex, line)

        if match:
               self.ip = match.group("ip")
               self.user = match.group("user")
               self.status = match.group("status")
               self.session = match.group("session")
               self.method = match.group("method")
               self.size = match.group("size")
               self.url = match.group("url")
        else:
            print("No match found")


      #  self.ip = match.group("ip")
      #  self.user = match.group("user")
      #  self.status = match.group("status")
      #  self.session=match.group("session")
      #  self.method=match.group("method")
       # self.size=match.group("size")
      #  self.url=match.group("url")


    def TimeStamp(self, line: str):
      #  timestamp_regex = r'[(\d{2})/(\w{3})/(\d{4}):(\d{2}):(\d{2}):(\d{2}) ([+-]\d{4})]'
       #  timestamp_regex = r'[(\d{2})/(\w{3})/(\d{4}):(\d{2}):(\d{2}):(\d{2}) ([+-]\d{4})]'
         # timestamp_regex = r'[(\d{2})/(\w{3})/(\d{4}):(\d{2}):(\d{2}):(\d{2}) ([+-]\d{4})]'

        timestamp_regex = r'\[(\d{2})/(\w{3})/(\d{4}):(\d{2}):(\d{2}):(\d{2}) ([+-]\d{4})\]'
 
        match = re.search(timestamp_regex, line)
        self.timestamp=match.group().replace("[","").replace("]","")



    def rest_version(self, line: str):
        pattern = r'HTTP/(\d.\d)'
        match = re.search(pattern, line)
        self.rest_vers=match.group()
#/*

   #     class LogClean:
    #   def __init__(self):
    #       self.ip = ""
    #       self.user = ""
    # --     self.timestamp = ""
      #     self.utc = ""
       #    self.status = ""
 #  -#-   #     self.session = ""
    #    self.method = ""
   #--     self.size = ""
    #  --  #      self.url = ""
    #       self.rest_vers = ""

#    def parse(self, line: str):
 #       regex = re.compile(r"(?P<ip>\S{7,15}) (?P<session>\S{1}|\S{15}) (?P<user>\S{1,50}) \[(?P<timestamp>\S{20}) "
#                           r"(?P<utc>\S{5})\] \"(?P<method>GET|POST|DELETE|PATCH|PUT) (?P<url>\S{1,4500}) "
 #                          r"(?P<version>\S{1,10})\" (?P<status>\d{3}) (?P<size>\d+) -")
  #      match = re.search(regex, line)
        
   #     self.ip = match.group("ip")
   #     self.user = match.group("user")
  #      self.status = match.group("status")
    #    self.session = match.group("session")
  # #     self.method = match.group("method")
   #     self.size = match.group("size")
   ##     self.url = match.group("url")
   #     self.TimeStamp(line)
    #    self.rest_version(line)

        # Write parsed data to CSV file
  #      with open('parsed_data.csv', mode='a', newline='') as file:
   #         writer = csv.writer(file)
   #         writer.writerow([self.ip, self.session, self.user, self.timestamp, self.utc, self.method, self.url, self.rest_vers, self.status, self.size])

   # def TimeStamp(self, line: str):
      #    timestamp_regex = r'\[(\d{2})/(\w{3})/(\d{4}):(\d{2}):(\d{2}):(\d{2}) ([+-]\d{4})\]'
   #     match = re.search(timestamp_regex, line)
   #     self.timestamp = match.group().replace("[","").replace("]","")

   # def rest_version(self, line: str):
  #      pattern = r'HTTP/(\d.\d)'
   #     match = re.search(pattern, line)
   #     self.rest_vers = match.group()

# */ 


# publish event