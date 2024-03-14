# MrGlider. Telegram bot

## Deploy

```commandline
docker build --tag app -f Dokcerfile
docker run -v /usr/share/mr_glider:/usr/share/mr_glider/data --env-file ./.env -p 8000:8000 --name mrglider app
```
