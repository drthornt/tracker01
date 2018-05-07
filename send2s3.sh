#!/bin/bash

BUCKET=mymainsqueeze
PATH="mymainsqueeze"

for i in tracker.log light.log 
aws s3 cp $i s3://${BUCKET}/${PATH}/$i

