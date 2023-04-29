#!/bin/bash
# Sends a delete request to the url passed as the first argument
curl -s "$1" -X DELETE
