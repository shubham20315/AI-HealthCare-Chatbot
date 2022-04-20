# AI-HealthCare-Chatbot
# Introduction 
People are increasingly concerned about their health in the present international circumstances. Regrettably, today's medical human resource is inferior to that of the patient.The goal is to develop a medical chatbot that can converse with a patient if he is aware of his ailment and deliver relevant information, as well as diagnose the disease using disease prediction and provide basic information about the disease before contacting a doctor. Through the use of a medical chatbot, this will assist to minimize healthcare expenses and enhance access to medical information. Chatbots are computer programmes that communicate with users using natural language. The data is stored in the database so that the chatbot can recognise the sentence keywords, make a query choice, and respond to the inquiry. The n-gram, TFIDF, and cosine similarity are used to rank and calculate sentence similarity. From the supplied input sentence, a score will be calculated for each sentence, and additional comparable sentences will be found for the query. The chatbot has two different parts one of them is a conversing agent that converses with the user and another one is disease prediction that takes input from the user and predicts what is the disease and what precautions can be taken. For the disease prediction part we have used multiple machine learning classifiers such as logistic Regression, K-Nearest Neighbors, SVM, Random Forest, Decision Tree and Convolutional Neural Network on the dataset and we got highest accuracy of 91.44 using CNN classifier on test dataset.

# Documentation
One can find out more about the machine learning algorithms used to AI-HealthCare-Chatbot in the Healthcare_chatbot_Project_Report.pdf and you can find out our working model at Web Application folder

# Dataset Description
The dataset used for chatbot is a merged dataset that contains 11278 question answer pairs regarding covid, mental health, depression and general doctor-patient quotes. The  dataset used for disease prediction is disease symptom dataset. The dataset contains 4961 rows containing 129 features (Disease symptoms) and 1 target variable (Disease Name).
# Installation of Prediction Model

# Prerequisite
One needs Python 3.6 with standard libraries such as pandas, matplotlib, seaborn, numpy,sklearn and imblearn.

# Steps to run the code
1) Download the code using Web Application
2) Downlaod the dataset using full dataset.csv
3) You can run the code in your local machine having python 3.6 and libraries or you can use the Google Collab for running code without any difficulty.
