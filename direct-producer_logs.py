import time
from transformations import UserTransformation,StatusCodeTransformation, UrlTransformation, TimeTransformation, IPTransformation, sizeTransformation
from server import channel

QUEUE_LOGS = "logs-producer"
EXCHANGE_NAME = "topic-exchange-logs"

# create exchange
channel.exchange_declare(EXCHANGE_NAME, durable=True, exchange_type='topic')

# create a queue
channel.queue_declare(queue=QUEUE_LOGS)
channel.queue_bind(exchange=EXCHANGE_NAME, queue=QUEUE_LOGS)

# publish event
#events = ["event 1", "event 2", "event 3", "event 4", "event 5"]


logs_files = open("C:/Users/Windows-10/Desktop/Projet/python/class-4/assets/web-server-nginx.log")

for line in logs_files:
    channel.basic_publish(exchange=EXCHANGE_NAME, routing_key=QUEUE_LOGS, body=line)
    UserTransformation(line)
    StatusCodeTransformation(line)
    UrlTransformation(line)
    TimeTransformation(line)
    IPTransformation(line)
    sizeTransformation(line)



    time.sleep(2)
    
    print(f"[x] published {line}")




#for event in events:
 #   channel.basic_publish(exchange=EXCHANGE_NAME, routing_key=QUEUE_LOGS, body=event)
 #   time.sleep(2)
#    print(f"[x] published {event}")