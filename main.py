# Imports the BigQuery client library
from google.cloud import bigquery

def hello_world(request):
        # Replace these values according to your project
    project_name = "xcaliber-betitonpartners" 
    bucket_name = "betitionpartners_prd" 
    dataset_name = "betition_test" 
    table_name = "dynamic_variables" 
    destination_uri = "gs://{}/{}".format(bucket_name, "bq_export.csv.gz")

    bq_client = bigquery.Client(project=project_name)

    dataset = bq_client.dataset(dataset_name, project=project_name)
    table_to_export = dataset.table(table_name)

    job_config = bigquery.job.ExtractJobConfig()
    job_config.compression = bigquery.Compression.GZIP

    extract_job = bq_client.extract_table(
        table_to_export,
        destination_uri,
        # Location must match that of the source table.
        location="US",
        job_config=job_config,
    )  
    return "Job with ID {} started exporting data from {}.{} to {}".form