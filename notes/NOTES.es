Index config in api, not es

esimport.py doesn't create index. in es egs
eswrappers.py - api/mrpapi/es
Create using template.py
es.create(index='name', config='')
puttemplate


python elasticsearch - rest interface

jq - Tool for json. Eg. xml-grep

mrp-api bitbucket wiki


Dev es:
ssh -i ~/git/mrp-ops/deploy/encrypted_keys/mrp_us-west-1.pem ec2-user@es.rmtg.co
(Needs passphrase)
2 machines in cluster
both machines with shards, so need to update simultaneously.

Get info about meetings in dev
token www-dev.remeeting.com/app/#/d and look in console

curl -s -H "Authorization: Bearer $tok" "https://api-dev.remeeting.com/v0.3/meeting/" | jq '.Meetings[].Meeting'  # list meetings
curl -s -H "Authorization: Bearer $tok" "https://api-dev.remeeting.com/v0.3/meeting/7d31" | jq  # show meeting

Data from meeting (including annotations)
curl -s -H "Authorization: Bearer $tok" "https://api-dev.remeeting.com/v0.3/meeting/data/7d31/" | jq


