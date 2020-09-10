# cloud-function


Simple cloud function which allow to export table from dataset and send to Google Cloud Storage.
project_name = "xxxxx"   #type project name 
bucket_name = "xxxxxxxx" 
dataset_name = "xxxxxx" 
table_name = "xxxxxx" 
destination_uri = "gs://{}/{}".format(bucket_name, "name_of_your_new_file.csv"). #path to you bucket
