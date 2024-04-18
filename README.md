# MLOps-chest-cancer-classification

This project focuses on building an end-to-end machine learning pipeline for chest cancer classification, leveraging MLflow and DVC for streamlined ML lifecycle management. The pipeline is deployed using GitHub, Docker, and AWS, with the application hosted in a Flask environment.

Key Components:
1. Data Ingestion: Importing and preprocessing the dataset.
2. Preparing Model: Feature engineering and selection.
3. Training Model: Model training and hyperparameter tuning.
4. Model Evaluation: Evaluating model performance and generating metrics.
5. Prediction: An interactive pipeline allowing users to make predictions based on the trained model.

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml

## MLFLOW

To track model versions and evaluate them based on various metrics, uncomment 
``` python
# evaluation.log_into_mlflow()
```
under \src\cnnClassifier\pipeline\stage_04_model_evaluation.py

The following must be exported as env variables prior to logging in:
```shell
export MLFLOW_TRACKING_URI=https://dagshub.com/a-ayesh/MLOps-Chest-Cancer-Classification.mlflow 
export MLFLOW_TRACKING_USERNAME=a-ayesh 
export MLFLOW_TRACKING_PASSWORD=3c9db54c5412e695ee06168b89ca8ae39847b403 
```
## AWS CI/CD Deployment with GitHub Actions

The steps taken for the deployment are as follows:
1. Build docker image of the source code
2. Push the docker image to ECR
3. Launch EC2 instance
4. Pull the image from ECR into the EC2 instance
5. Launch the image within EC2

1. ### Create IAM user for deployment
```
Provide it with the following access policies:
1. AmazonEC2FullAccess
2. AmazonEC2ContainerRegistryFullAccess
```

2. ### Create ECR repo to store the docker image
```
URI: 058264514472.dkr.ecr.us-east-1.amazonaws.com/chest
```

3. ### Create (Ubuntu) EC2 instance

4. ### Install docker on the EC2 instance
```shell
sudo apt-get update -y

sudo apt-get upgrade

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

5. ### Configure the EC2 as a self-hosted runner:
```
setting>actions>runner>new self hosted runner> choose os> then run command one by one
```

6. ### Setup GitHub secrets
```
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  058264514472.dkr.ecr.us-east-1.amazonaws.com

ECR_REPOSITORY_NAME = chest
```