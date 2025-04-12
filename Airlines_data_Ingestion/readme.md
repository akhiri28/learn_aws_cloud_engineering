1 Dim Table for Airport Codes
In S3 on daily basis flight data will arraive in hive style partition.

Key Words
- Incremental Data Load.
- Denormalised table. 


S3 as data lake
Event Bridge Rule
Step Function for Orchestration
Glue Crawler
Glue Job
Redshift as Datawarehouse
SNS for notification

Redshift --> airport_dim (dim table) -- (load from airport_dim.csv)
         --> flight_fact (fact table)

s3 bucket --> airport_dim.csv
          --> daily_files --> event bridge rule (capture the event) --> trigger step function --> glue   crawler (wait for success) --> trigger glue job (join operations)  --> failed (SNS. Failed notification) | success (store in flight _fact table.)


![data ingestion pod](<../images/Data Ingestion Project.jpg>)