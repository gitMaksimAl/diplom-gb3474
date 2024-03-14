#!/bin/bash

export -n HOST;
export -n PORT;
export -n DATABASE_URI;
pkill gunicorn;
