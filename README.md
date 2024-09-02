# QRNG - Integrazione con Generatore di Numeri Casuali Quantistico
## Panoramica

Questo progetto dimostra l'integrazione di un Generatore di Numeri Casuali Quantistico (QRNG) con Google Cloud per creare un servizio consumabile che fornisce numeri casuali tramite un'API REST. Il sistema è costruito utilizzando un Raspberry Pi, che interagisce con il dispositivo QRNG, e i servizi Google Cloud, inclusi Pub/Sub e Cloud Functions.
## Architettura
### Componenti
- Dispositivo QRNG: Un Generatore di Numeri Casuali Quantistico collegato a un Raspberry Pi, che genera numeri casuali veri basati su processi quantistici.
- Raspberry Pi: Il Raspberry Pi è responsabile della lettura dei numeri casuali generati dal QRNG e della loro pubblicazione su un topic Google Cloud Pub/Sub.
- Google Cloud Pub/Sub: Pub/Sub viene utilizzato come servizio di messaggistica che disaccoppia la generazione dei numeri casuali dal loro consumo. I numeri casuali vengono pubblicati su un topic specifico e possono essere consumati da qualsiasi sottoscrittore.
- Google Cloud Functions: Una Cloud Function espone un'API REST che i clienti possono chiamare per ricevere numeri casuali. La Cloud Function agisce come un sottoscrittore Pub/Sub, recuperando i numeri casuali dalla sottoscrizione e restituendoli al cliente tramite una risposta HTTP.

## Workflow

  ### Generazione dei Numeri:
- Il QRNG genera numeri casuali, che vengono poi letti dal Raspberry Pi.
- Il Raspberry Pi esegue uno script Python che legge continuamente i numeri casuali dal dispositivo QRNG e li pubblica su un topic Google Cloud Pub/Sub.
- Pubblicazione dei Messaggi:
        Lo script Python sul Raspberry Pi pubblica ogni numero casuale come un messaggio sul topic Pub/Sub.
- Gestione delle Richieste API:
        Un cliente invia una richiesta HTTP GET all'endpoint API REST esposto da Google Cloud Functions.
        La Cloud Function si sottoscrive al topic Pub/Sub, recupera un numero casuale dalla sottoscrizione e lo restituisce nella risposta HTTP al cliente.
