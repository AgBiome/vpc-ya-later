# VPC Ya Later

Annihilate a VPC and all its resources.

## Requirements:

* Python version: 3.8.12
* Boto3 version: 1.20.26
* Botocore version: 1.23.26
* Valid AWS API keys/profile

## Usage

```
vpc-ya-later.py [-h] -v VPC [-r REGION] [-d] [-p PROFILE]

optional arguments:
  -h, --help                    show this help message and exit
  -v VPC, --vpc VPC             The VPC to annihilate
  -r REGION, --region REGION    AWS region that the VPC resides in
  -d, --dryrun                  If exists, dry run all deletions.
  -p PROFILE, --profile PROFILE AWS profile
```
## License
[MIT](https://choosealicense.com/licenses/mit/)

## Important, please read !!!

The script will try to delete every resource within the VPC. Please use with caution.

Resources that can be deleted:

* EC2
* EKS
* ASG
* Lambda
* RDS
* ELB
* ELBv2
* NAT
* VPC Endpoint
* VPC IGW
* VPC VPGW
* ENI
* Routing tables
* Security groups
* ACLs
* VPC

