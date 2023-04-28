#!/bin/bash
# Display all HTTP methods the server of a url will take.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
