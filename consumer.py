import time
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic
from pika.spec import BasicProperties
from server import channel
from row_log import Log_lake
from log_clean import Log_clean
from transformations import UserTransformation,StatusCodeTransformation, UrlTransformation, TimeTransformation, IPTransformation, sizeTransformation
from models import Base,raw_log,clean_log
from sqlalchemy import create_engine
from database import CONFIG
from sqlalchemy.orm import sessionmaker



def process_msg(chan: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body):
    print(f"[{method.routing_key}] event consumed from exchange `{method.exchange}` body `{body}`")


QUEUES = [
    {
        "name": "queue-data-lake",
        "routing_key": "logs"
    },
    {
        "name": "queue-data-clean",
        "routing_key": "logs"
    }
]

EXCHANGE_NAME = "topic-exchange-logs"
# create exchange
channel.exchange_declare(EXCHANGE_NAME, durable=True, exchange_type='topic')
# create queues
for queue in QUEUES:
    channel.queue_declare(queue=queue['name'])
    channel.queue_bind(exchange=EXCHANGE_NAME, queue=queue['name'], routing_key=queue['routing_key'])

engine = create_engine(
    "mysql+mysqlconnector://%s:%s@localhost:3309/%s" %
    (CONFIG['DB_USER'], CONFIG['DB_PASSWORD'], CONFIG['DB_NAME'])
)


connection = engine.connect()
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()



#data-clean-consumer

def process_msg_clean(chan: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body):
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

 # event consumed from exchange `{method.exchange}` body `{body}`")


    log=body.decode("utf-8")
    if '- -' not in log:
       log_clean=Log_clean()
       log_clean.MD5(log)
       log_clean.parse(log)
       log_clean.TimeStamp(log)
       log_clean.rest_version(log)
       log_clean = StatusCodeTransformation().transform(log_clean)
       log_clean = UserTransformation().transform(log_clean)
       log_clean=UrlTransformation().get_schema_host_from_url(log_clean)
       log_clean=TimeTransformation().Time_UTC_O(log_clean)
      # log_clean=IPTransformation().get_country_city_from_IP(log_clean)
       #log_clean.get_location(log_clean.ip)
       log_clean=sizeTransformation().kilo_mega_bytes(log_clean)
       # INSERT INTO THE DATA BASE 
       # try:
       RowClean= clean_log(id=log_clean.id,timestamp=log_clean.timestamp,year=log_clean.year,month=log_clean.month,day=log_clean.day,day_of_week=log_clean.day_of_week,time=log_clean.time,ip=log_clean.ip,
                           country=log_clean.country,city=log_clean.city,session=log_clean.session,user=log_clean.user,is_email=log_clean.is_email,url=log_clean.url,schema=log_clean.schema,host=log_clean.host,
                           rest_version=log_clean.rest_vers,status=log_clean.status,status_verbose=log_clean.status_verbose,size_bytes=log_clean.size,size_kilo_bytes=log_clean.size_k_b,size_mega_bytes=log_clean.size_m_b,
                           email_domain=log_clean.domain,rest_method=log_clean.method)
       c_instance = session.query(clean_log).filter_by(id=RowClean.id).one_or_none()
       if not c_instance:
                session.add(RowClean)
                session.commit()
      # except Exception as e:
              #  print(e)             

#data-lake-consumer
def process_msg_lake(chan: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body):
    print(f"[{method.routing_key}] event consumed from exchange `{method.exchange}` body `{body}`")

    log=body.decode("utf-8")
    if '- -' not in log:
       log_lake=Log_lake()
       log_lake.MD5(log)
       log_lake.TimeStamp(log)
       log_lake.line(log)
       # INSERT INTO THE DATA BASE
       try:
           RowLog= raw_log(id=log_lake.id,timestamp=log_lake.timestamp,log=log_lake.log)
           c_instance = session.query(raw_log).filter_by(id=RowLog.id).one_or_none()
           if not c_instance:
                session.add(RowLog)
                session.commit()
                print(f"consuming --> {log}")
       except Exception as e:
                print(e) 


# consume messages from queues
channel.basic_consume(queue="queue-data-lake", on_message_callback=process_msg_lake, auto_ack=True)
channel.basic_consume(queue="queue-data-clean", on_message_callback=process_msg_clean, auto_ack=True)
#channel.basic_consume(queue="queue-b", on_message_callback=process_msg, auto_ack=True)
#channel.basic_consume(queue="queue-c", on_message_callback=process_msg, auto_ack=True)
channel.start_consuming()
