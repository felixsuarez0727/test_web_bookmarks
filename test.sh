#!/bin/bash

echo "GET"
echo -e "\n"
curl http://35.238.101.89:8000/bookmark/
echo -e "\n"

echo "POST"
echo -e "\n"
curl -d "title=test&url=abc&created_at=aaa" http://localhost:8000/bookmark/
echo -e "\n"

echo "GET"
echo -e "\n"
curl http://35.238.101.89:8000/bookmark/1/
echo -e "\n"
