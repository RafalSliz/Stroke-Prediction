# Stroke Prediction

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

#### 1. Create account and log on to GCP
#### 2. Create new project
My First Project > New project

<img src="https://user-images.githubusercontent.com/35708288/158665837-7f7453ba-c91b-4d42-83b9-60f0d3fa2e99.png" width="400"/> 

#### 3. Select the project as active 
My First Project > stroke-prediction

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
#### 14. Edit .bashrc
Add environment variables:
```
export SPARK_HOME=~/pyspark/spark-3.2.1-bin-hadoop2.7
export PATH=$PATH:$SPARK_HOME/bin
export PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH
export PYSPARK_PYTHON=python3
export PATH=$PATH:$JAVA_HOME/jre/bin
```
#### 15. Upload files to server
Move all files in the Stroke-Prediction/App directory to the server. 

<img src="https://user-images.githubusercontent.com/35708288/158706169-42d8a470-1419-49d2-9508-3755f1c97fb8.png" width="350"/>

#### 16. Install requirements
```
pip3 install -r requirements.txt
```

#### 17. Create firewall rule
For accessing the Streamlit application using external IP address you need to create a Firewall rule. This is necessary because Streamlit uses port 8501. 

<img src="https://user-images.githubusercontent.com/35708288/158707836-fe97bff8-3f47-4d10-89b8-cddb7cf3e205.png" width="300"/>
<img src="https://user-images.githubusercontent.com/35708288/158707856-8091d61e-1579-4f60-a4c8-3f987efca9b3.png" width="350"/>
<img src="https://user-images.githubusercontent.com/35708288/158707858-16f53a26-357b-440f-835b-b48fb85fbc7f.png" width="350"/>
<img src="https://user-images.githubusercontent.com/35708288/158707925-aae87395-6301-4696-bb1a-65a6a102eb2e.png" width="350"/>
<img src="https://user-images.githubusercontent.com/35708288/158707927-30e7d948-1089-40c3-8948-2dbeaf50414d.png" width="350"/>

#### 18. Run Streamlit app
```
streamlit run app.py
```
<img src="https://user-images.githubusercontent.com/35708288/158708401-8e5d3501-e9ab-429d-ac2c-81d606e67f42.png" width="500"/>
From now on, the application is available at external url.

#### 19. Register domain
I chose the Freenom platform and registered the domain stroke-prediction.ml 

<img src="https://user-images.githubusercontent.com/35708288/158709508-3e6a17c5-825d-495e-a292-a5eb58fb0f80.png" width="500"/>

#### 20. Install NGINX
NGINX server is used to link the application to the external domain of stroke-prediction.ml 
```
sudo apt install nginx
```
#### 21. Configure the NGINX server
Go to directory /etc/nginx/sites-enabled and create tactml file.
```
cd /etc/nginx/sites-enabled
touch tactml
```
tactml file should look like below:
```
server {
    listen 80;    server_name stroke-prediction.ml www.stroke-prediction.ml;    index index.php index.html index.htm;    location / {
        proxy_pass http://0.0.0.0:8501/;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }    error_page 404 /404.html;
    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
        root /usr/share/nginx/html;
    }
}
```
#### 22. Restart NGINX
```
sudo systemctl restart nginx
```

#### 23. Enable Cloud DNS and create DNS zone

<img src="https://user-images.githubusercontent.com/35708288/158711274-1a2c9f1b-b3cf-47d2-9d6e-d4c9dc7d683d.png" width="200"/>
<img src="https://user-images.githubusercontent.com/35708288/158711281-5113baf0-60aa-4827-9327-c51c8e1088c5.png" width="300"/>
<img src="https://user-images.githubusercontent.com/35708288/158711291-cb92e639-c139-4232-bffa-c30d680903fa.png" width="400"/>
<img src="https://user-images.githubusercontent.com/35708288/158711297-00dfdc59-4403-4fc0-b4b2-93cd42695293.png" width="400"/>
<img src="https://user-images.githubusercontent.com/35708288/158711300-eefa0352-5477-4e54-a1ee-5af78cb1f89c.png" width="400"/>

Add records to the DNS zone and copy marked on the screen below routing policy: 

<img src="https://user-images.githubusercontent.com/35708288/158711305-fb50dd08-cced-4c31-be66-2ad3b784bc5e.png" width="600"/>

#### 24. Domain configuration on the Freenom platform 

<img src="https://user-images.githubusercontent.com/35708288/158712490-4b6f7099-f122-49a0-b941-1dbdba4a75da.png" width="200"/>
<img src="https://user-images.githubusercontent.com/35708288/158712493-6472a268-a682-4a1b-9f9a-6b2e6fc71bba.png" width="400"/>
<img src="https://user-images.githubusercontent.com/35708288/158712499-6c463b18-29e7-46dc-be50-2d5de1cf0dfa.png" width="400"/>

Paste the copied routing policy:

<img src="https://user-images.githubusercontent.com/35708288/158712516-04d0e197-09ca-4a4a-b74f-98a231f9a1a9.png" width="600"/>

#### 25. Run the application using tmux 
Start a new session in the console
```
tmux new -s stroke-prediction
```
Run the Streamlit app
```
streamlit run app.py
```
That's all.
You can check app: www.stroke-prediction.ml
