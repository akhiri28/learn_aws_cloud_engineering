What is EC2?
------------

    - EC2 - Elastic Compute Capacity, is service provided by AWS to build on-demand, secure, scalable, reliable (consistent and correct) compute capacity in AWS with commitment of 99.9% availability (always accessible). Using Ec2, as many Virtual Machines as required can be spinned easily and quickly. The storage, network and security can be configured manually.

    - (Optional) - Explore in perspective of security - AWS Nitro System. 

    - EC2 Instance is a virtual serer in AWS cloud. 

What are Feature of EC2?
------------------------

    - Features of Ec2
        - Instances - Virtual Server on AWS Cloud.
        - Amazon Machine Images (AMI) - Packged OS and Other software required for Instance.
        - Instance Types - Instance type determines the type of compute (CPU / GPU), memory, network and storage.
        - EBS Volumes - Elastic Block Store 
            - It provides persistant storage to EC2 instance to store the OS, Application Files, Logs and other things etc.
        - Instance store 
            - If EBS volume is not available, EC2 uses temporary storage called, Instance store. Instance store is small storage from the physical machine of data center. The Instance store is lost as soon as the instance is stopped / terminated or hardware fails.
            - (Optional) It is Network Attached Storage (NAS) in Cloud. NAS is storage connected to a network which can be accessed by many devices in the network.
        - Key pairs - Secure login to the EC2 instance - Public key is stored in AWS and private key in store near user.
        - Security groups - A virtual firewall that provide range of IP address, ports and protocols that can be used to access the instance and IP address of the destination which can be access by instance.
        - Instance States
            - running
            - pending
            - stopping
            - stopped
            - shuting down
            - terminated
        - Pricing model for EC2
            - On-demand - Pay by the second/hour. No commitment. - Instance may not be available, a rare case though. - Use Case - Short-term or unpredictable workloads - Development and Testing, Ad-Hoc Data Analytics.
            - Reserved - Commit to 1 or 3 years for a discount (up to ~75%). - Use case - Steady, always-on workloads - Web Servers for Production Websites, Databases (e.g., RDS or EC2-based), Data Warehousing.
            - Spot Instances - Use spare capacity at huge discount (up to 90% off) - High Risk as AWS can take back the instance with 2 hours notice. - Use Case - Flexible, fault-tolerant jobs - Serverless Functions (e.g., AWS Lambda), Data Processing with Auto-scaling.


Types of EC2 Instance
---------------------
    - General purpose
    - Compute optimized
    - Memory optimized
    - Storage optimized
    - Accelerated computing

Instance Performance
---------------------
    - Fixed performance 
    - burstable performance
    - flex


Use Cases of EC2?
------------------

- Deliver secure, reliable, high-performance, and cost-effective compute infrastructure to meet demanding business needs.
- Access the on-demand infrastructure and capacity you need to run 'HPC applications' faster and cost-effectively. (HPC Apps)
- Access environments in minutes, dynamically scale capacity as needed, and benefit from AWS’s pay-as-you-go pricing. (cost, easily, quick, scale)
- Deliver the broadest choice of compute, networking (up to 400 Gbps), and storage services purpose-built to optimize price performance for ML projects (ML, Cpst)

- Keywords - secure, reliable, high-performance, cost, easily, quick, scale, HPC Apps, ML


How to Use EC2?
---------------
- Launch EC2
- Configure Instance - (Instance Type, Network Settings, Storage, security groups, key pairs).
- Accessing and troubleshooting using SSH (Secure Shell).
- Monitor instance performance and utilization.

Interview Questions
-------------------

Set 1

1. What is Amazon EC2?

2. How does Amazon EC2 work?

3. What are the different instance types in EC2?

4. Explain the differences between on-demand, reserved, and spot instances.

5. How can you improve the availability of EC2 instances?

6. What is an Amazon Machine Image (AMI)?

7. How can you secure your EC2 instances?

8. Explain the difference between public IP and Elastic IP in EC2.

9. How can you scale your application using EC2?

10. What is Amazon EBS?

11. How can you encrypt data on EBS volumes?

12. How can you back up your EC2 instances?

13. What is the difference between instance store and EBS-backed instances?

14. What are instance metadata and user data in EC2?

15. How can you launch instances in a Virtual Private Cloud (VPC)?

16. What is the purpose of an EC2 security group?

17. How can you automate the deployment of EC2 instances?

18. How can you achieve high availability for an application using EC2?

19. What is Amazon Machine Learning (Amazon ML)?

20. What is Amazon EC2 Instance Connect?


Set 2

1. What is Amazon EC2, and why is it used?

2. What types of EC2 instances are available, and how should one choose?

3. How does EC2 Auto Scaling help in managing application availability and scalability?

4. You need to deploy a web application on EC2 instances across multiple Availability
Zones to ensure high availability. Describe how you would architect this setup.

5. Explain the process and considerations for optimizing EC2 instances for both cost and
performance when deploying a compute-intensive application.
















