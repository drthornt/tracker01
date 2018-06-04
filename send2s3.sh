#!/bin/bash

BUCKET=mymainsqueeze
FOLDER="mymainsqueeze"

for i in tracker.log light.log
    do
    aws s3 cp $i s3://${BUCKET}/${FOLDER}/$i
    done

