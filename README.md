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



You can check app: www.stroke-prediction.ml
