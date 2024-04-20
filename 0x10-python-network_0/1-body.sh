#!/bin/bash
# 1-body.sh
curl -o /dev/null -s -w "%{http_code}\n" "$1" | grep 200
