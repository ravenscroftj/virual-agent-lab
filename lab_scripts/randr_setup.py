# coding=utf-8
import json, requests, sys
from os.path import join, dirname
from watson_developer_cloud import RetrieveAndRankV1
import variables

retrieve_and_rank = RetrieveAndRankV1(
    username=variables.RR_USERNAME,
    password=variables.RR_PASSWORD)

print(json.dumps(retrieve_and_rank.list_solr_clusters(), indent=2))
# CREATE A SOLR CLUSTER
created_cluster = retrieve_and_rank.create_solr_cluster(cluster_name='Test Cluster', cluster_size='1')
print(json.dumps(created_cluster))
solr_cluster_id = created_cluster["solr_cluster_id"]

msg="Waiting for cluster"

loop="."
while True:
    status = retrieve_and_rank.get_solr_cluster_status(solr_cluster_id=solr_cluster_id)
    if(status["solr_cluster_status"] == "READY"):
        print("Cluster ready, moving on")
        break
    else:
        msg=msg + '.'
        sys.stdout.write('\r' + msg)
        sys.stdout.flush() # important

# UPLOAD SOLR CONFIG
with open(join(dirname(__file__), '../rr_config/gemstone_solr_config/gemstone_solr_config.zip'), 'rb') as config:
    config_status = retrieve_and_rank.create_config(solr_cluster_id, 'gem_config', config)
    print(json.dumps(config_status, indent=2))

print(json.dumps(retrieve_and_rank.list_configs(solr_cluster_id=solr_cluster_id), indent=2))
print("*****Remember to copy the solr_cluster_id (" + solr_cluster_id + ") to the bottom of the variables file*****")

