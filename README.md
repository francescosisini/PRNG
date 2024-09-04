# PRNG (Physical Random Number Generator) Service

Questo progetto fornisce un servizio per la generazione e il consumo di numeri casuali generati tramite un Physical Random Number Generator (PRNG). I dati vengono gestiti tramite Google Cloud Pub/Sub, dove i client possono pubblicare e consumare numeri casuali direttamente attraverso script Python.

## Struttura del Progetto

Il progetto è composto da due funzioni principali:

1) Pubblicazione dei numeri casuali su Pub/Sub
2) Consumo dei numeri casuali da Pub/Sub

## Prerequisiti

Prima di procedere, assicurati di avere i seguenti strumenti installati:

* Python 3.7 o superiore
* Google Cloud SDK (gcloud)
* Un progetto Google Cloud attivo
* Autenticazione configurata per accedere ai servizi Google Cloud tramite l'SDK:
* Autenticati con gcloud auth login
* Imposta il progetto predefinito: gcloud config set project [YOUR_PROJECT_ID]

Inoltre, assicurati di aver creato un topic Pub/Sub e una subscription per la gestione dei messaggi:

```

gcloud pubsub topics create [YOUR_TOPIC]
gcloud pubsub subscriptions create [YOUR_SUBSCRIPTION] --topic=[YOUR_TOPIC]
```
## Installazione

    Clona il repository nel tuo ambiente locale:

```
git clone https://github.com/[USERNAME]/PRNG.git
cd PRNG
```
Installa le dipendenze del progetto:

```
pip install -r requirements.txt
``` 
Imposta le credenziali per l'accesso a Google Cloud Pub/Sub:

Assicurati di avere un file di credenziali JSON per l'account di servizio. Imposta la variabile d'ambiente GOOGLE_APPLICATION_CREDENTIALS con il percorso al file di credenziali:

```

    export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/credentials.json"
```
Pubblicazione dei Numeri Casuali

Lo script prng_publisher.py pubblica numeri casuali generati fisicamente sul topic di Pub/Sub.

Ecco un esempio di utilizzo:

```

python prng_publisher.py
```
Codice di esempio per la pubblicazione:
```


import random
from google.cloud import pubsub_v1

project_id = "YOUR_PROJECT_ID"
topic_id = "YOUR_TOPIC_ID"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

def publish_random_number():
    random_number = str(random.randint(0, 100))  # Simulazione di un numero casuale fisicamente generato
    future = publisher.publish(topic_path, random_number.encode("utf-8"))
    print(f"Numero pubblicato: {random_number}")
    future.result()  # Attende fino a quando il messaggio viene pubblicato

if __name__ == "__main__":
    publish_random_number()
```
Risultato:

Il numero casuale generato verrà pubblicato sul topic specificato.
Consumo dei Numeri Casuali

Lo script prng_consumer.py consuma i messaggi dalla subscription di Pub/Sub.

Ecco come eseguirlo:

```

python prng_consumer.py
```
Codice di esempio per il consumo:
```


from google.cloud import pubsub_v1

project_id = "YOUR_PROJECT_ID"
subscription_id = "YOUR_SUBSCRIPTION_ID"

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

def callback(message):
    print(f"Numero ricevuto: {message.data.decode('utf-8')}")
    message.ack()

def consume_numbers():
    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print("In ascolto dei numeri casuali...")

    try:
        streaming_pull_future.result()
    except KeyboardInterrupt:
        streaming_pull_future.cancel()

if __name__ == "__main__":
    consume_numbers()
```
Risultato:

I numeri casuali pubblicati vengono consumati e stampati in console.
Debugging e Log

Puoi monitorare i log delle funzioni e le attività di Pub/Sub tramite i seguenti comandi:

```

gcloud functions logs read --limit=50
```
Per vedere i log specifici delle subscription o eventuali errori:

```

gcloud pubsub subscriptions pull [YOUR_SUBSCRIPTION] --limit=5 --auto-ack
```
## Contributi

Sono benvenuti contributi sotto forma di pull request. Assicurati di seguire le linee guida per i commit.

## Conclusione

Ora puoi pubblicare e consumare numeri casuali generati fisicamente tramite Google Cloud Pub/Sub usando semplici script Python. Se hai domande o problemi, sentiti libero di aprire una issue nel repository.
