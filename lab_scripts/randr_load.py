# coding=utf-8
import json, requests, sys
from os.path import join, dirname
from watson_developer_cloud import RetrieveAndRankV1
import variables

retrieve_and_rank = RetrieveAndRankV1(
    username=variables.RR_USERNAME,
    password=variables.RR_PASSWORD)

# CREATE SOLR COLLECTION
collection = retrieve_and_rank.create_collection(variables.SOLR_CLUSTER_ID, variables.SOLR_COLLECTION_NAME, 'gem_config')
print(collection)

print(json.dumps(retrieve_and_rank.list_collections(solr_cluster_id=variables.SOLR_CLUSTER_ID), indent=2))

# INDEX DOCUMENTS (SDK doesn't include this option)
url = 'https://gateway.watsonplatform.net/retrieve-and-rank/api/v1/solr_clusters/' + \
    variables.SOLR_CLUSTER_ID + '/solr/' + \
    variables.SOLR_COLLECTION_NAME + '/update'
with open(join(dirname(__file__), '../rr_config/fda_medwatch_docs.json'), 'rb') as doc_file:
    result = requests.post(url, auth=(variables.RR_USERNAME, variables.RR_PASSWORD), headers={'content-type': 'application/json'}, data=doc_file)
    print(result.text)