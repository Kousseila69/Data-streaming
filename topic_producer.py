import time
from transformations import UserTransformation,StatusCodeTransformation, UrlTransformation, TimeTransformation, IPTransformation, sizeTransformation
from server import channel
from logclean import Log_clean
import csv
##Queues : queue-data-lake and queue-data-clean
QUEUES = [
    {
        "name": "queue-data-lake",
        "routing_key": "logs"
    },
    {
        "name": "queue-data-clean",
        "routing_key": "logs"
    },
    
]
######################################################""
EVENTS = [
    {
        "routing_key": "logs",
        "body": "event 1"
    },
    {
        "routing_key": "logs",
        "body": "event 1"
    },
    
]

EXCHANGE_NAME = "topic-exchange-logs"

# create exchange
channel.exchange_declare(EXCHANGE_NAME, durable=True, exchange_type='topic')

# create queues
for queue in QUEUES:
    channel.queue_declare(queue=queue['name'])
    channel.queue_bind(exchange=EXCHANGE_NAME, queue=queue['name'], routing_key=queue['routing_key'])

# utilisation de la fonction open pour ouvrir le fichier web-server-nginx.log
logs_files = open("C:/Users/Windows-10/Desktop/Projet/python/Data-streaming-RabbitMQ/assets/web-server-nginx.log")

for line in logs_files:
    channel.basic_publish(exchange=EXCHANGE_NAME, routing_key='logs', body=line)
   


   # for queue in QUEUES: channel.queue_declare(queue=queue['name']) channel.queue_bind(exchange=EXCHANGE_NAME, queue=queue['name'], routing_key=queue['routing_key'])
  # print()
    #time.sleep(2)   
# publish event
#print(f"[x] published {line}' in topic `{queue['routing_key']}`")


 
# Initialize CSV file
#with open('parsed_data.csv', mode='w', newline='') as file:
  #  writer = csv.writer(file)
  #  writer.writerow(['IP', 'user', 'is_email', 'domain', 'status', 'status_verbose', 'timestamp', 'method', 'version', 'schema', 'host', 'size', 'size_k_b', 

               
#for event in EVENTS:
 #   channel.basic_publish(exchange=EXCHANGE_NAME, routing_key=event['routing_key'], body=event['body'])
 #   time.sleep(2)
 #   print(f"[x] published event `{event['body']}` in topic `{event['routing_key']}`")

