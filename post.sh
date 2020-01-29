#!/bin/bash

# -d is the data, -H is the headers, -X is the request type
curl -d "@data.json"  -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/user/$1
