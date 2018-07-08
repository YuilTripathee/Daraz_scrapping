# About gunicorn
Deployment server for Flask and Quart. (aka hypercorn)

## To start HTTP/2:
```bash
gunicorn --worker-class quart.worker.GunicornWorker --keyfile key.pem --certfilecert.pem --ciphers 'ECDHE+AESGCM' --bind 'localhost:5000' qserver:app
```

## Without HTTP/2
```bash
gunicorn --config gunicorn.py 'run:create_app()'
```