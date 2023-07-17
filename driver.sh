#!/bin/bash

MODEL_PATH="../../../../hy-tmp/chatglm-6b"
CASE_PATH="./IOFiles/cases.txt"

rm -rf ./IOFiles/Responses/
mkdir ./IOFiles/Responses/

for trial in {1..2}
do
    echo "Trial $trial started."
    RESPONSES_PATH="./IOFiles/Responses/Trial-${trial}/"
    mkdir $RESPONSES_PATH
    python3 main.py $MODEL_PATH $RESPONSES_PATH $CASE_PATH
done