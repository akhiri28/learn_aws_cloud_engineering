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
