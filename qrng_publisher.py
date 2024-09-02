import random
from google.cloud import pubsub_v1
import time

# Configurazione del publisher
project_id = "servizi"
topic_id = "projects/strange-mind-312015/topics/QGRN"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

def get_random_number_from_qrng():
    # Simula la lettura dal QRNG
    # Sostituisci questa funzione con il codice per leggere il numero casuale dal tuo QRNG
    return str(random.randint(0, 100))

def publish_random_number():
    random_number = get_random_number_from_qrng()
    future = publisher.publish(topic_path, random_number.encode("utf-8"))
    print(f"Published message: {random_number}")

#while True:
publish_random_number()
time.sleep(1)  # Puoi regolare la frequenza di pubblicazione dei numeri casuali
