

Interview Questions
-------------------
Q: What is AWS IAM, and why is it important?
A: IAM - Identity and Access Management System, is a service is access control and security management service proivided by AWS.
   It helps to create and manage entities to access to AWS Resources. This helps only autherized entities can aaccess AWS resources and thus reducing the security risks.
   It is like a security system for the AWS account.


Q: What is the difference between IAM users and IAM roles?
A: IAM Users represents individual people or entities that need access to AWS resources. They have their own credentials and typicall associated with long term access.
   IAM Roles is entity provides temporary access usually given to application or AWS Services to perform specific actions on AWS Resources. 
   Roles have associated policies. The actions that can be performed on AWs Resources is controlled by Policies.


Q: What are IAM policies, and how do they work?
A: Policy is a JSON documents which has the details of level of permission that is provided to the AWS Service, actions that are allowed and denied. 
   IAM Policy is attached to IAM entities.


Q: What is the principle of least privilege, and why is it important in IAM?
A: Principle of least priviledge states that the only enough level permission is to given to IAM entities that is required to complete the task. 


Q: What is an AWS managed policy?
A: AWS managed policy is policies are predefined policies that are created and managed by AWS.
