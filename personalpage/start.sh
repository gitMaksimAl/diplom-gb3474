#!/bin/bash

while read -r LINE;
do
    export $LINE;
done < ".env";
gunicorn -D -w 3 personalpage.wsgi -b $HOST:$PORT;
