# Stroke-Prediction

<img src="https://user-images.githubusercontent.com/35708288/158497746-9a402e1f-a522-4d48-b558-aa2ef37eed61.png" width="81"/> <img src="https://user-images.githubusercontent.com/35708288/158497344-08840e35-c859-4fd0-8605-e063ec1b5789.png" width="182"/> <img src="https://user-images.githubusercontent.com/35708288/158498250-096dfe50-bdc5-49d2-8f75-9c43e745c215.png" width="182"/> <img src="https://user-images.githubusercontent.com/35708288/158498254-d32accc7-259e-422f-8588-5b4ed4d83cd8.png" width="105"/> <img src="https://user-images.githubusercontent.com/35708288/158499086-a8c483c7-c210-493b-9867-bc9ef318c315.png" width="105"/> <img src="https://user-images.githubusercontent.com/35708288/158498353-1f996fdd-9a68-43f4-9926-3b3db5548265.png" width="97"/> 

The goal of the project is to build an application capable of detecting the risk of a stroke on the basis of data such as age, hypertension, heart disease, glucose level. The dataset includes 43k patient records. Among the records, 1.8% of them are related to stroke patients and the remaining 98.2% of them are related to non-stroke patients. The data is extremely imbalanced.

## Data
Dataset can be downloaded from the Kaggle or repository Stroke-Prediction/Data/dataset.csv

## ML model
Google Colab was used to perform data analysis and build a machine learning model. Prediction algorithm was developed in Spark. The entire process of preparing the ML model is described in the comments in the Stroke-Prediction/Colab-notebooks/StrokePrediction01.ipynb file.

## App
The application was developed in Python and Streamlit framework. Based on the machine learning model, the application classifies whether there is a risk of a stroke or not. All files necessary to run the application are available in Stroke-Prediction/App.

## Deploying app in Google Cloud Platform
The process of deploying an application in GCP is described in detail below. 

<img src=" " width="400"/> 

#### 1. Create account and log on to GCP
#### 2. Create new project
My Rirst Project > New project

<img src="https://user-images.githubusercontent.com/35708288/158665837-7f7453ba-c91b-4d42-83b9-60f0d3fa2e99.png" width="400"/> 

#### 3. Select the project as active 
My Rirst Project > stroke-prediction

<img src="https://user-images.githubusercontent.com/35708288/158666897-06abe2f8-3422-4fed-84d0-aed2e22e1262.png" width="400"/> 

#### 4. Enable Compute Engine

<img src="https://user-images.githubusercontent.com/35708288/158667640-16301ef6-9a1c-4f81-a895-7a261888b4f6.png" width="130"/> <img src="https://user-images.githubusercontent.com/35708288/158667651-2c4ccfc8-2347-43a7-bc25-8cbc3de1aacd.png" width="250"/> 

#### 5. Create instance
<img src="https://user-images.githubusercontent.com/35708288/158681767-f1605e85-8dde-430a-b75d-2738ad240a64.png" width="400"/>
<img src="https://user-images.githubusercontent.com/35708288/158681775-c9f34ff1-c22e-47a1-8b4d-225c6388aa14.png" width="350"/>
<img src="https://user-images.githubusercontent.com/35708288/158681782-4dc7bd50-9b82-4bc1-ab28-53045a1059ff.png" width="400"/>
<img src="https://user-images.githubusercontent.com/35708288/158681791-b5b96606-9ddf-4cb4-b22f-748943bdb054.png" width="350"/> 

#### 6. Log in to newly created VM instance by SSH

<img src="https://user-images.githubusercontent.com/35708288/158683030-9940bbb8-6c62-4f87-8075-cc55fc51b053.png" width="400"/>

#### 7. Update package information
```
sudo apt update
```
#### 8. Install Supporting Software
```
sudo apt install software-properties-common
```
#### 9. Add Deadsnakes PPA
```
sudo add-apt-repository ppa:deadsnakes/ppa
```
#### 10. Install Python 3
```
sudo apt install python3
```
#### 11. Install Java
```
sudo apt install openjdk-8-jdk
```
#### 12. Download Spark
Go to the Spark website and select the Spark release and package type to download. 

https://spark.apache.org/downloads.html
```
wget https://dlcdn.apache.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop2.7.tgz
```
#### 13. Install Spark
```
sudo tar -zxvf spark-3.2.1-bin-hadoop2.7.tgz
```







You can check app: www.stroke-prediction.ml
