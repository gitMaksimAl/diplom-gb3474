# MrGlider. Telegram bot

## Deploy

```commandline
docker build --tag app -f Dokcerfile
docker run --env-file ./.env -p 8000:8000 --name mrglider app
```
