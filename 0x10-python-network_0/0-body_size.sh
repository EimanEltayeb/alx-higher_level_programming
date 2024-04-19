#!/bin/bash
# 0-body_size.sh
curl -s -w "%{size_download}" "$1" 
~                
