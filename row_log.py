import re
import hashlib
from datetime import datetime, timezone, timedelta

class Log_lake:
    def __init__(self):
        self.id = None
        self.timestamp = None
        self.log = None

    def MD5(self, line: str):
        try:
            m=hashlib.md5()
            m.update(line.encode('utf-8'))
            self.id= m.hexdigest()
        except Exception as e:
               print(e)

    def TimeStamp(self, line: str):
        timestamp_regex = r'\[(\d{2})/(\w{3})/(\d{4}):(\d{2}):(\d{2}):(\d{2}) ([+-]\d{4})\]'
        try:
            match = re.search(timestamp_regex, line)
            self.timestamp=match.group().replace("[","").replace("]","")
            print(self.timestamp)
        except Exception as e:
               self.timestamp=""
    
    def line (self,line:str):
        self.line=line.replace('"','')
        delimiter = "-"
        replacement = ""
        parts = self.line.rsplit(delimiter, 1)
        self.log = replacement.join(parts)
        print(self.line)
    
    def __str__(self):
        return f"""
        id: {self.id}
        timestamp: {self.TimeStamp}
        line:{self.line}
        """