#!/bin/bash
# sends a request to a URL passed as an argument, and displays only the status code of the response
curl -sI $1 | head -1 | cut -d ' ' -f 2
