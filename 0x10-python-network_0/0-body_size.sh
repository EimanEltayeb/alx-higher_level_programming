#!/bin/bash
# 0-body_size.sh
curl -o /dev/null -s -w "%{size_download}" "$1" 
