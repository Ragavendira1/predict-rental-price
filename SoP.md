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

#### Start the Jenkins 
change dir to Jenkins
cd C:\jenkins\
java -jar .\jenkins.war --enable-future-java

Name of the s3 bucket: mlapp-models-stroage-artifacts-13-12-24
URI of the S3 Bucket: s3://mlapp-models-stroage-artifacts-13-12-24
AWS S3 CLI command for the file upload: 
$ aws s3 cp <name-of-the-Artifact><Name-of-the- S3 Bucket/Name of the object>
Job1: 01_mlapp_build_docker_image
This Jenkins job is designated to pull the ML mode from GitHub, and build the source code and generate .joblib file and upload to AWS S3 bucket and build images for MLApp

 aws s3 cp rental_price_model.joblib s3://mlapp-models-stroage-artifacts-13-12-24/mlapp.joblib 

Job2: 02_mlapp_push_docker_image_registry
This Job to push image built from 01_mlapp_build_docker_image into Docker Container Registry

## AWS ECR Commands
Make sure that you have the latest version of the AWS TOOLS for PowerShell and Docker installed. For more information, see Getting Started with Amazon ECR .
Use the following steps to authenticate and push an image to your repository. For additional registry authentication methods, including the Amazon ECR credential helper, see Registry Authentication .
Retrieve an authentication token and authenticate your Docker client to your registry. Use the AWS TOOLS for PowerShell:
Step 1:
(Get-ECRLoginCommand).Password | docker login --username AWS --password-stdin 590183798731.dkr.ecr.us-east-1.amazonaws.com
Note: If you receive an error using the AWS TOOLS for PowerShell, make sure that you have the latest version of the AWS TOOLS for PowerShell and Docker installed.
Build your Docker image using the following command. For information on building a Docker file from scratch see the instructions here . You can skip this step if your image is already built:
Step 2: 
docker build -t mlappecr .
After the build completes, tag your image so you can push the image to this repository:
Step 3: 
docker tag mlappecr:latest 590183798731.dkr.ecr.us-east-1.amazonaws.com/mlappecr:latest
Run the following command to push this image to your newly created AWS repository:
Step 4: 
docker push 590183798731.dkr.ecr.us-east-1.amazonaws.com/mlappecr:latest
### Installing Kubernetes (kind)
To install `kind` (Kubernetes in Docker), run the following command on Windows:
```bash
curl.exe -Lo kind-windows-amd64.exe https://kind.sigs.k8s.io/dl/v0.24.0/kind-windows-amd64
Move-Item .\kind-windows-amd64.exe c:\kind\kind.exe
```

### Create a Kubernetes Cluster
Create a local Kubernetes cluster using `kind`:
```bash
$ kind create cluster --name main-k8s-cluster
```

Verify that the cluster is up and running:
```bash
$ kubectl get nodes
$ kubectl get pods
$ kubectl get deployments
```

### Deploying the Application on Kubernetes
Use the following commands to deploy the machine learning app.

#### Apply Deployment Configuration:
```bash
$ kubectl apply -f k8s-config-files/mlapp-deployment.yaml
$ kubectl apply -f k8s-config-files/mlapp-service.yaml
$ kubectl port-forward svc/mlapp-service 5000:5000
```
