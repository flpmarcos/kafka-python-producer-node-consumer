from kafka import KafkaProducer
import json
import random
from time import sleep
from datetime import datetime

# Criando uma instancia do kafka
producer = KafkaProducer(bootstrap_servers='localhost:29092',
                            value_serializer=lambda v: str(v).encode('utf-8'))

# Enviando mensagem para a o topic coma valor randomico
print("Ctrl+c to Stop")
while True:
    producer.send('kafka-python-topic', random.randint(1,999))