from google.cloud import bigquery

def backup(request):
       
    project_name = "project-clientname" 
    bucket_name = "bucket_name_client" 
    dataset_name = "client_env" 
    table_name = "dynamic_variable" 
    destination_uri = "gs://{}/{}".format(bucket_name, "bq_export.csv.gz")

    bq_client = bigquery.Client(project=project_name)

    dataset = bq_client.dataset(dataset_name, project=project_name)
    table_to_export = dataset.table(table_name)

    job_config = bigquery.job.ExtractJobConfig()
    job_config.compression = bigquery.Compression.GZIP

    extract_job = bq_client.extract_table(
        table_to_export,
        destination_uri,
        
        location="US",
        job_config=job_config,
    )  
    return "Job with ID {} started exporting data from {}.{} to {}".form
