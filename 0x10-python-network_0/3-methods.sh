#!/bin/bash
# takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -sI $1 | grep -Fi Allow | cut -d ' ' -f 2-
