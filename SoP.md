## 1. Installing Required Libraries
You’ll need to install a few libraries for machine learning tasks and dependencies like NumPy, Pandas, and scikit-learn. These can be installed with `pip`.

### NumPy Installation
To install NumPy, run:
```bash
$ pip install numpy
```

### Pandas Installation
To install Pandas, run:
```bash
$ pip install pandas
```

### scikit-learn Installation
To install or upgrade scikit-learn, run:
```bash
$ pip install -U scikit-learn
```

### scikit-learn Installation
To install joblib, run:
```bash
$ pip install joblib
```
#### AWS CLI installation on windows ####
https://awscli.amazonaws.com/AWSCLIV2.msi
Note: 
- Using IAM, create 'mlapp' user and associate AWS S3FULL Access policy to user(mlapp)
- Create IAM Credentials for same mlapp user(AccessKeyID, SecretAccessKeyID)
$ aws --version # Verify AWS CLI Installation
$ aws configure # Configure AWS CLI to allow program
    - AccessKeyID:
    - SecretAccesskey:
    - region: us-east-2
    - output: json 
## List of Docker Commands
$ docker images
$ docker ps -a
$ docker images
$ docker build -t <name_of_the_docker_image>
$ docker login
$ docker rmi <image-id>
$ docker rm $(docker ps a)
$ docker rmi $(docker images -a -q)
$ docker push <<image_id>>
$ docker push rragavendira/mlapp:latest

######################################
Using Jenkins
######################################
Name of the s3 bucket: mlapp-models-stroage-artifacts-13-12-24
URI of the S3 Bucket: s3://mlapp-models-stroage-artifacts-13-12-24
AWS S3 CLI command for the file upload: 
$ aws s3 cp <name-of-the-Artifact><Name-of-the- S3 Bucket/Name of the object>
Job1: 01_mlapp_build_docker_image
This Jenkins job is designated to pull the ML mode from GitHub, and build the source code and generate .joblib file and upload to AWS S3 bucket and build images for MLApp

 aws s3 cp rental_price_model.joblib s3://mlapp-models-stroage-artifacts-13-12-24/mlapp.joblib 

Job2: 02_mlapp_push_docker_image_registry
This Job to push image built from 01_mlapp_build_docker_image into Docker Container Registry
