import time
from transformations import UserTransformation,StatusCodeTransformation, UrlTransformation, TimeTransformation, IPTransformation, sizeTransformation
from server import channel
from logclean import Log_clean
from topic_producer import QUEUES, EXCHANGE_NAME
import csv


# Ouvrir le fichier web-server-nginx.log
with open("C:/Users/Windows-10/Desktop/Projet/python/class-4/assets/web-server-nginx.log") as file:
    logs = file.readlines()

# Créer un fichier CSV et écrire l'en-tête
with open("parsed_data.csv", mode="w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        "id",
        "timestamp",
        "year",
        "month",
        "day",
        "day_of_week",
        "time",
        "ip",
        "country",
        "city",
        "session",
        "user",
        "is_email",
        "email_domain",
        "rest_method",
        "url",
        "schema",
        "host",
        "rest_version",
        "status",
        "status_verbose",
        "size_bytes",
        "size_kilo_bytes",
        "size_mega_bytes"
    ])

    # Parcourir chaque ligne de logs
    for line in logs:
        # Parser les données avec la classe Log_clean
       X=Log_clean()
    X.parse(line)
    X.TimeStamp(line)
    X.rest_version(line)
    X=UserTransformation()
    X=StatusCodeTransformation()
    X=UrlTransformation()
    X=TimeTransformation()
    X=IPTransformation()
    X=sizeTransformation()

        # Ecrire chaque ligne dans le fichier CSV
    writer.writerow([
           # log_clean.id,
            X.TimeStamp,
            X.year,
            X.month,
            X.day,
            X.day_of_week,
            X.time,
            X.ip,
            X.country,
            X.city,
            X.session,
            X.user,
            X.is_email,
            X.email_domain,
            X.rest_method,
            X.url,
            X.schema,
            X.host,
            X.rest_version,
            X.status,
            X.status_verbose,
            X.size_bytes,
            X.size_kilo_bytes,
            X.size_mega_bytes
        ])
if hasattr(X, 'timestamp'):
    writer.writerow([
        X.ip_address, 
        X.user_agent, 
        X.username, 
        X.timestamp.strftime('%Y-%m-%d %H:%M:%S'), 
        X.method, 
        X.endpoint, 
        X.response_code, 
        X.size
    ])
else:
    writer.writerow([
        X.ip_address, 
        X.user_agent, 
        X.username, 
        '',  # mettre une chaîne vide si l'attribut timestamp n'existe pas
        X.method, 
        X.endpoint, 
        X.response_code, 
        X.size
    ])