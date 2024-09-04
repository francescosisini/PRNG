# PRNG - Integrazione con Generatore di Numeri Casuali Quantistico
## Panoramica

Questo progetto dimostra l'integrazione di un Generatore di Numeri Casuali Fisico (Physics) (PRNG) con Google Cloud per creare un servizio consumabile che fornisce numeri casuali tramite un'API REST. Il sistema è costruito utilizzando un Raspberry Pi, che interagisce con il dispositivo QRNG, e i servizi Google Cloud, inclusi Pub/Sub e Cloud Functions.
## Architettura
### Componenti
- Dispositivo PRNG: Un Generatore di Numeri Casuali Fisico collegato a un Raspberry Pi, che genera numeri casuali veri basati su processi quantistici.
- Raspberry Pi: Il Raspberry Pi è responsabile della lettura dei numeri casuali generati dal PRNG e della loro pubblicazione su un topic Google Cloud Pub/Sub.
- Google Cloud Pub/Sub: Pub/Sub viene utilizzato come servizio di messaggistica che disaccoppia la generazione dei numeri casuali dal loro consumo. I numeri casuali vengono pubblicati su un topic specifico e possono essere consumati da qualsiasi sottoscrittore.
- Google Cloud Functions: Una Cloud Function espone un'API REST che i clienti possono chiamare per ricevere numeri casuali. La Cloud Function agisce come un sottoscrittore Pub/Sub, recuperando i numeri casuali dalla sottoscrizione e restituendoli al cliente tramite una risposta HTTP.

## Workflow

  ### Generazione dei Numeri:
- Il QRNG genera numeri casuali, che vengono poi letti dal Raspberry Pi.
- Il Raspberry Pi esegue uno script Python che legge continuamente i numeri casuali dal dispositivo PRNG e li pubblica su un topic Google Cloud Pub/Sub.
- Pubblicazione dei Messaggi:
        Lo script Python sul Raspberry Pi pubblica ogni numero casuale come un messaggio sul topic Pub/Sub.
- Gestione delle Richieste API:
        Un cliente invia una richiesta HTTP GET all'endpoint API REST esposto da Google Cloud Functions.
        La Cloud Function si sottoscrive al topic Pub/Sub, recupera un numero casuale dalla sottoscrizione e lo restituisce nella risposta HTTP al cliente.
```
  
+-------------+            +-----------------+          +----------------+                       +---------------------+
|  Dispositivo|  --> USB --> | Raspberry Pi   |  --> Pub/Sub Topic  -->  | Cloud Function |  -->  Richiesta del Cliente |
|     PRNG    |            +-----------------+          +----------------+                        +---------------------+
                                                             |
                                                             |
                                                     +-----------------+
                                                     | Pub/Sub Sottosc. |
                                                     +-----------------+
```
## Installazione
Configurazione di Python su Ubuntu

Se stai configurando il Raspberry Pi o un altro sistema Ubuntu, segui questi passaggi per installare Python e le dipendenze necessarie:

    Aggiorna la lista dei pacchetti:
```
sudo apt update
```
Installa Python 3:

```
sudo apt install python3
```
Installa pip:
```

sudo apt install python3-pip
```
Verifica l'installazione:
```

python3 --version
pip3 --version
```
Installa le dipendenze necessarie:
```

    pip3 install google-cloud-pubsub
```
## Configurazione del Raspberry Pi
Installazione delle Dipendenze: Installa le librerie Python necessarie sul tuo Raspberry Pi (già spiegato nella sezione precedente).
### Configurazione di Google Cloud:
- Assicurati di avere un progetto Google Cloud configurato.
- Crea un topic Pub/Sub e una corrispondente sottoscrizione nella Console Google Cloud.
- Scarica la chiave dell'account di servizio per l'autenticazione e posizionala sul tuo Raspberry Pi.
- Imposta la variabile d'ambiente per autenticarti con Google Cloud:

```
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"
```
Esegui lo Script di Pubblicazione: Usa lo script Python fornito per iniziare a pubblicare numeri casuali su Pub/Sub:

```
    python publisher.py
```
### Configurazione di Google Cloud Functions
Crea la Cloud Function:
- Distribuisci una Google Cloud Function che funge da sottoscrittore Pub/Sub ed espone un'API REST.
- Il codice della funzione dovrebbe essere simile all'esempio fornito nel file main.py in questo repository.
Distribuisci la Funzione:
```

gcloud functions deploy getRandomNumber \
--runtime python310 \
--trigger-http \
--allow-unauthenticated \
--set-env-vars GOOGLE_CLOUD_PROJECT=your-project-id
```
Testa l'API:

    Dopo aver distribuito la funzione, riceverai un URL per l'API REST. Puoi usare strumenti come curl o Postman per effettuare richieste e ricevere numeri casuali.

Esempio:

```
    curl https://REGION-PROJECT_ID.cloudfunctions.net/getRandomNumber
```
## Contributi

Accogliamo con piacere contributi per migliorare questo progetto. Se hai suggerimenti o trovi problemi, invia una pull request o apri un issue.
Licenza

Questo progetto è concesso sotto licenza MIT. Consulta il file LICENSE per i dettagli.
