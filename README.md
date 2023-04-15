# Data-Streaming-RabbitMQ
# introduction: 
Les données en streaming sont des données générées en continu par différentes sources. De telles données doivent être traitées de manière incrémentale en utilisant des techniques de traitement en continu sans avoir accès à l'ensemble des données. De plus, il est important de prendre en compte la possibilité de changements dans les propriétés de ces données au fil du temps, également appelée dérive conceptuelle.

Ces données sont souvent associées au concept de big data, car elles sont générées par de nombreuses sources différentes à grande vitesse. Le streaming de données peut également être expliqué comme une technologie utilisée pour fournir du contenu à des appareils via Internet, ce qui permet aux utilisateurs d'y accéder immédiatement, sans avoir à attendre qu'il soit téléchargé.

Le stockage étant un enjeu majeur pour les organisations traitant de grandes quantités de données, les concepts de "data lake" et de "data stream" ont vu le jour. Un "data lake" correspond au stockage de grandes quantités de données structurées et semi-structurées, et est utile pour le traitement du big data, car il permet de plonger dans le lac de données et de récupérer ce dont on a besoin au moment où on en a besoin. En revanche, le "data stream" permet d'effectuer une analyse en temps réel des données en streaming, sans avoir à les stocker au préalable. Cette approche se distingue du "data lake" par sa vitesse d'analyse et sa nature continue, ce qui la rend idéale pour le traitement de grandes quantités de données en continu.

# RabbitMQ:
RabbitMQ est l'un des courtiers de messages open-source les plus populaires, utilisé par des dizaines de milliers d'utilisateurs dans le monde entier, des petites start-ups aux grandes entreprises telles que T-Mobile et Runtastic.

RabbitMQ est facile à déployer sur site ou dans le cloud, et est léger. Il prend en charge plusieurs protocoles de messagerie et peut être déployé dans des configurations distribuées et fédérées pour répondre aux exigences de haute disponibilité et de grande échelle.

Il fonctionne sur de nombreux systèmes d'exploitation et environnements de cloud, et offre une large gamme d'outils pour les développeurs dans la plupart des langages de programmation populaires.

Pour en savoir plus sur RabbitMQ, vous pouvez consulter leur site web à l'adresse suivante: https://www.rabbitmq.com/

<p align="center">
  <img src="assets/RabbitMG.PNG" alt="My Image">
</p>

# Le Projet:
Notre projet consiste à créer un producteur qui lit un fichier journal (logs) et publie les données sur deux files d'attente, queue-data-lake et queue-data-clean. Les deux files d'attente utilisent la même clé de routage, "logs", ce qui signifie que chaque événement publié par le producteur sera envoyé aux deux files d'attente. Deux consommateurs seront créés pour consommer les événements de chaque file d'attente, transformer les données et les insérer dans une base de données à l'aide d'un ORM.

Voici quelques suggestions pour améliorer votre idée de projet :

Définir l'objectif du projet: Avant de commencer à développer le projet, il est important de définir clairement l'objectif et les cas d'utilisation. Par exemple, l'objectif peut être de collecter et de stocker des données de journalisation pour l'analyse ou pour surveiller la santé d'une application. Les cas d'utilisation peuvent inclure la détection des erreurs, le suivi des performances, la sécurité ou la conformité.

Choisir la technologie appropriée : Il est important de choisir les technologies appropriées pour le projet, en fonction des besoins de l'objectif. Par exemple, pour la collecte et la diffusion de données de journalisation, il peut être judicieux d'utiliser des technologies de file d'attente comme Apache Kafka ou RabbitMQ. Pour stocker les données dans une base de données, vous pouvez utiliser un ORM (Object Relational Mapping) comme SQLAlchemy ou Hibernate.

Définir les formats de données : Il est important de définir les formats de données pour les fichiers journaux et pour les messages échangés entre les producteurs et les consommateurs. Les formats de données doivent être normalisés et cohérents pour faciliter la transformation et le stockage des données.

Définir les stratégies de traitement des erreurs : Il est important de définir les stratégies de traitement des erreurs pour gérer les échecs de traitement des messages, les pannes des consommateurs ou des producteurs, et les conflits de données. Les stratégies peuvent inclure la gestion des redémarrages automatiques, la journalisation des erreurs, la mise en place de mécanismes de sauvegarde et de restauration, et la gestion des conflits de données.

Sécurité : La sécurité doit être prise en compte dès le début du projet, et les bonnes pratiques doivent être appliquées pour garantir la confidentialité, l'intégrité et la disponibilité des données. Il est important de définir les politiques de sécurité, d'authentification et de contrôle d'accès appropriées pour le projet.

En résumé, pour améliorer votre idée de projet, il est important de définir clairement l'objectif et les cas d'utilisation, de choisir les technologies appropriées, de définir les formats de données et les stratégies de traitement des erreurs, et de prendre en compte les aspects de sécurité.

<p align="center">
  <img src="assets/schema.png" alt="My Image">
</p>