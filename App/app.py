
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml import PipelineModel
from pyspark.ml import Pipeline
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

from pyspark.ml.classification import DecisionTreeClassificationModel
from pyspark.ml.tuning import CrossValidatorModel

import findspark
findspark.init()

sc = SparkSession.builder.appName('stroke-prediction').getOrCreate()
model_in = DecisionTreeClassificationModel.load('model01')
featureColumns = ['age', 'hypertension',
                  'heart_disease', 'ever_married', 'avg_glucose_level']

def predict2(age, hypertension, heart_disease, ever_married, avg_glucose_level):
    predictDf = pd.DataFrame(np.array(
        [[age, hypertension, heart_disease, ever_married, avg_glucose_level]]), columns=featureColumns)
    sparkPredictDf = sc.createDataFrame(predictDf)

    predictAssembler = VectorAssembler(inputCols=[
                                       'age', 'hypertension', 'heart_disease', 'ever_married', 'avg_glucose_level'], outputCol='features')
    predictAssembled = predictAssembler.transform(sparkPredictDf)
    predictAssembled = predictAssembled.select(['features'])

    predictedDf = model_in.transform(predictAssembled)
    predictedValue = predictedDf.collect()[0][3]
    return predictedValue


st.set_page_config(page_title="Stroke Prediction", layout="centered")

with st.container():
    st.markdown("<h1 style='text-align: center; color: #FFFFFF;'>Stroke Prediction using Machine Learning</h1>",
                unsafe_allow_html=True)
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            "A stroke is the death of a part of the brain when blood flow to the brain is stopped. In developed countries, 2 in 1000 people in the general population suffer a stroke each year, but as many as 10 in 1000 people over the age of 65. 30 percent of patients die within three months of having a stroke."
        )
    with right_column:
        image = Image.open("niedokrwienne.jpg")
        st.image(image)

with st.form('Form1'):
    with st.container():
        st.markdown(
            "<h2 style='text-align: center; color: #FFFFFF;'>Fill in the form below to check your risk of a stroke </h2>", unsafe_allow_html=True)
        age = st.slider('How old are you ?', 0, 100, 50)
        hypertensionSelected = st.selectbox(
            'Do you have hypertension ?', ('Yes', 'No'))
        if hypertensionSelected == 'Yes':
            hypertension = 1
        elif hypertensionSelected == 'No':
            hypertension = 0
        heartDiseaseSelected = st.selectbox(
            'Do you have any heart disease ?', ('Yes', 'No'))
        if heartDiseaseSelected == 'Yes':
            heartDisease = 1
        elif heartDiseaseSelected == 'No':
            heartDisease = 0

        everMarriedSelected = st.selectbox(
            'Are you married ?', ('Yes', 'No'))
        if everMarriedSelected == 'Yes':
            everMarried = 1
        elif everMarriedSelected == 'No':
            everMarried = 0

        glucoseLevel = st.slider('Glucose level ?', 0, 260, 80)

        st.markdown(
            "<h3 style='text-align: center; color: #FFFFFF;'>Check that the entered data are correct and click the &quot;Predict&quot; button </h3>", unsafe_allow_html=True)
        submitted1 = st.form_submit_button('Predict')

        if submitted1:
            predictValue = predict2(
                age, hypertension, heartDisease, everMarried, glucoseLevel)
            if predictValue == 1.0:
                st.markdown(
                    "<h4 style='text-align: center; color: #d63227;'>High risk of stroke has been detected. Contact a doctor.</h4>", unsafe_allow_html=True)
            elif predictValue == 0.0:
                st.markdown(
                    "<h4 style='text-align: center; color: #FFFFFF;'>No risk of stroke has been detected.</h4>", unsafe_allow_html=True)
