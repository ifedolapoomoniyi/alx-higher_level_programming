#!/bin/bash
# script that takes a url and sends a request to it displaying the size of the body
curl -s "$1" | wc -c
