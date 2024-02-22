'''
curl --location --request POST 'http://data.binshuo.vip:9100/adjudication_document_20231215/_search' \
--header 'User-Agent: Apifox/1.0.0 (https://apifox.com)' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic c3ByaW5nYmluOkJzMTIzNDU2' \
--data-raw '{
  "_source": ["courtBelieves","title","caseNumber"], 
  "query": {
    "match_all": {}
  },
  "knn": {
    "field": "courtBelievesVector",
    "k": 10,
    "query_vector": [
        -0.010510128922760487,
        -0.021857773885130882,
        -0.009665749035775661,
        -0.020292581990361214,
        -0.023395506665110588
    ], 
    "num_candidates": 100
  }
}'''

import requests
from pprint import pprint


url = 'http://data.binshuo.vip:9100/adjudication_document_20231215/_search'
header = {
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Content-Type': 'application/json',
    'Authorization': 'Basic c3ByaW5nYmluOkJzMTIzNDU2'
}

data = {
    "_source": ["courtBelieves","title","caseNumber"], 
    "query": {
        "match_all": {}
    },
    "knn": {
        "field": "courtBelievesVector",
        "k": 10,
        "query_vector": [
            -0.010510128922760487,
            -0.021857773885130882,
            -0.009665749035775661,
            -0.020292581990361214,
            -0.023395506665110588
        ], 
        "num_candidates": 100
    }
}

result = requests.post(url, headers=header, json=data).json()
pprint(result)