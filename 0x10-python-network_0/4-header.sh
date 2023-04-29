#/bin/bash
# Send a GET request to a given URL with a header variable.
curl -s $1 -H "X-School-user-id: 98"
