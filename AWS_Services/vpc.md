1. What is VPC
    - VPC stands for Virtual Private Cloud. It is an isolated network environment, like having 
    our own data centers in the AWS cloud. VPC has range of IP Addresses.
    - VPC is created with in a AWS Region. It is virtual network (software defined network).
    - VPC consists of,
        - Subnets 
        - IP Address Range. 
        - Route Tables.
        - Internet gateway (IGW)
        - NAT Gateway.
        - Security Groups.
        - Network ACLs.
        - VPC Peering.
        - VPC Endpoints.

2. What is Subnet
    - VPC is divided into smaller network called subnets. It is a logical division of VPC using IP Address range.
    - Few IP Address are allocated to subnet.
    - Subnet can be public and private subnet. 
    - Public subnet can be accessed from internet using Internet Gateway (IGW). 
    - Private subnet can not be accessed from internet where as outbound traffic can be handled using NAT Gateway. 
    - Subnets can be distributed across AZ's within a Region. With this a VPC can span across AZ's.
    - Subnet can be used to controll the access of the application in VPC.

3. What is IP Address Range
    - It is defined using CDIR block.
    - Example
    - CIDR /16 defines a network with 65,536 possible IP addresses, ranging from 10.0.0.0 to 10.0.255.255.
    - The first 16 bits are for the network, and the last 16 bits are for the hosts.

4. What is Route Table
    - Route Tables tells AWS the detination where the it has to send the request.
    - 10.0.0.0/16 -local - Routes traffic within the VPC    (internal communication).
    - 0.0.0.0/0	- igw-xxxxxxxx (Internet Gateway) - Routes traffic to/from the   internet.
    - 10.1.0.0/16 - pcx-xxxxxxxx (VPC Peering) - Routes traffic to another VPC via peering connection.
    - 0.0.0.0/0	- nat-xxxxxxxx (NAT Gateway) - Routes traffic from private subnet to the internet.


Interview Questions
-------------------
1. What is Amazon Virtual Private Cloud (VPC)?

2. What are the key components of Amazon VPC?

3. How does Amazon VPC work?

4. What are VPC subnets?

5. How can you connect your on-premises network to Amazon VPC?

6. What is a VPC peering connection?

7. What is a route table in Amazon VPC?

8. How do security groups work in Amazon VPC?

9. What are network access control lists (ACLs) in Amazon VPC?

10. How can you ensure private communication between instances in Amazon VPC?

11. What is the default VPC in Amazon Web Services?

12. Can you peer VPCs in different regions?

13. How can you control public and private IP addresses in Amazon VPC?

14. What is a VPN connection in Amazon VPC?

15. What is an Internet Gateway (IGW) in Amazon VPC?

16. How can you ensure high availability in Amazon VPC?

17. How does Amazon VPC provide isolation?

18. Can you modify a VPC after creation?

19. What is a default route in Amazon VPC?

20. What is the purpose of the Amazon VPC Endpoint?
