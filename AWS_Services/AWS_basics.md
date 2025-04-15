Data Centers - It contains physical infrastructure like, - Server (Compute Resources) - Storage Systems - Network Equipment.

1. What is region in AWS

    - The AWS data centers are distributed across geographical location called AWS Regions. AWS Regions are isolated and do not communicate with other regions by default.
What are availability zones in AWS

    - A AWS Region may have multiple data centers and the data centers may be logical grouped together in to availability zones (AZ's).

    - A AWS Region may have atleast 2 AZ's.

    - AZ's are communicate with each other by high bandwidth and low latency links for communication.

    - Having AWS Regions and AZ's can help in making services a. Fault tolerant (Application continues to run even when one of the components fails). Fault Tolerant applications use redundancy (backup) in case component failures. Redundancy (The application can be backed up in different AZ's so that services may be available in case of Hardware, network or another break down.) b. High Availability - Minimum downtime. Strategies such as load balancing, routers are used for HA. The applications are directed to different availability zone in case of failure.

    - A application has be created in the Region which is closer to geography of the business. This will help in building low latency application.