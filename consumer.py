import os
from google.cloud import pubsub_v1

# Imposta il percorso al file delle credenziali JSON
#credentials_path = "PATH_TO_KEY.json"
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

# Configurazione del timeout (opzionale, puoi rimuoverlo se non è necessario)
timeout = 5.0

# Inizializza il client Subscriber
subscriber = pubsub_v1.SubscriberClient()

# Specifica il percorso completo della subscription
project_id = "integrazione-pgrn"
subscription_id = "physics-subscription"
subscription_path = f"projects/{project_id}/subscriptions/{subscription_id}"

# Definisci la funzione di callback per gestire i messaggi ricevuti
def callback(message):
    print('Received message:', message)
    print('Data:', message.data.decode('utf-8'))  # Decodifica i dati del messaggio
    message.ack()  # Conferma che il messaggio è stato ricevuto

# Sottoscrivi alla subscription e ascolta i messaggi
streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print("Listening for messages on ", subscription_path)

# Mantieni la connessione aperta per ricevere i messaggi
with subscriber:
    try:
        # Attendi indefinitamente fino a quando i messaggi non vengono ricevuti
        # Se preferisci un timeout, puoi usare: streaming_pull_future.result(timeout=timeout)
        streaming_pull_future.result()
    except TimeoutError:
        print("Timeout reached, cancelling the streaming pull future...")
        streaming_pull_future.cancel()  # Cancella la sottoscrizione in caso di timeout
        streaming_pull_future.result()  # Attende che lo streaming si chiuda completamente
