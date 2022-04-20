# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TYRb0_eIuyOeVpmv1UdtPmSAKrzbwSTl
"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import csv,numpy as np,pandas as pd
import os
description_list = dict()
precautionDictionary=dict()
data = pd.read_csv("Training.csv")
df = pd.DataFrame(data)
cols = df.columns
cols = cols[:-1]
x = df[cols]
y = df['prognosis']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

print ("DecisionTree")
dt = DecisionTreeClassifier()
clf_dt=dt.fit(x_train,y_train)
#print ("Acurracy: ", clf_dt.score(x_test,y_test))

# with open('templates/Testing.csv', newline='') as f:
#         reader = csv.reader(f)
#         symptoms = next(reader)
#         symptoms = symptoms[:len(symptoms)-1]

indices = [i for i in range(132)]
symptoms = df.columns.values[:-1]

dictionary = dict(zip(symptoms,indices))

def getDescription():
    global description_list
    with open('symptom_Description.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            _description={row[0]:row[1]}
            description_list.update(_description)


def getprecautionDict():
    global precautionDictionary
    with open('symptom_precaution.csv') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            _prec={row[0]:[row[1],row[2],row[3],row[4]]}
            precautionDictionary.update(_prec)


def dosomething(symptom):
    user_input_symptoms = symptom
    user_input_label = [0 for i in range(132)]
    for i in user_input_symptoms:
        idx = dictionary[i]
        user_input_label[idx] = 1

    user_input_label = np.array(user_input_label)
    user_input_label = user_input_label.reshape((-1,1)).transpose()
    disease=dt.predict(user_input_label)
    description=description_list[disease[0]]
    precution_list=precautionDictionary[disease[0]]
    precautions=" "
    for  i,j in enumerate(precution_list):
      precautions=precautions+"\n"+str(i+1)+")"+str(j)
    return disease,description,precautions

# print(dosomething(['headache','muscle_weakness','puffy_face_and_eyes','mild_fever','skin_rash']))
# prediction = []
# for i in range(7):
#     pred = dosomething(['headache'])   
#     prediction.append(pred) 
# print(prediction)
getDescription()
getprecautionDict()

# -*- coding: utf-8 -*-
"""Chatbot_vishal_working.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qEvBIs4phI_OrnmHj1aiADemFv7SRJUt
"""

import nltk
import string
import pandas as pd

import nlp_utils as nu
import matplotlib.pyplot as plt
# Loading necessary libraries

# #f = open("dialogs.txt", "r")
# #print(f.read())
# # reading the data 
# df=pd.read_csv('/content/dialogs.txt',names=('Query','Response'),sep=(','))
# df.to_csv('dialogues.csv')

import pandas as pd

# encoding_list = ['ascii', 'big5', 'big5hkscs', 'cp037', 'cp273', 'cp424', 'cp437', 'cp500', 'cp720', 'cp737'
#                  , 'cp775', 'cp850', 'cp852', 'cp855', 'cp856', 'cp857', 'cp858', 'cp860', 'cp861', 'cp862'
#                  , 'cp863', 'cp864', 'cp865', 'cp866', 'cp869', 'cp874', 'cp875', 'cp932', 'cp949', 'cp950'
#                  , 'cp1006', 'cp1026', 'cp1125', 'cp1140', 'cp1250', 'cp1251', 'cp1252', 'cp1253', 'cp1254'
#                  , 'cp1255', 'cp1256', 'cp1257', 'cp1258', 'euc_jp', 'euc_jis_2004', 'euc_jisx0213', 'euc_kr'
#                  , 'gb2312', 'gbk', 'gb18030', 'hz', 'iso2022_jp', 'iso2022_jp_1', 'iso2022_jp_2'
#                  , 'iso2022_jp_2004', 'iso2022_jp_3', 'iso2022_jp_ext', 'iso2022_kr', 'latin_1', 'iso8859_2'
#                  , 'iso8859_3', 'iso8859_4', 'iso8859_5', 'iso8859_6', 'iso8859_7', 'iso8859_8', 'iso8859_9'
#                  , 'iso8859_10', 'iso8859_11', 'iso8859_13', 'iso8859_14', 'iso8859_15', 'iso8859_16', 'johab'
#                  , 'koi8_r', 'koi8_t', 'koi8_u', 'kz1048', 'mac_cyrillic', 'mac_greek', 'mac_iceland', 'mac_latin2'
#                  , 'mac_roman', 'mac_turkish', 'ptcp154', 'shift_jis', 'shift_jis_2004', 'shift_jisx0213', 'utf_32'
#                  , 'utf_32_be', 'utf_32_le', 'utf_16', 'utf_16_be', 'utf_16_le', 'utf_7', 'utf_8', 'utf_8_sig']

# for encoding in encoding_list:
#     worked = True
#     try:
#         df = pd.read_csv('Dataset_Full_chatbot.csv', encoding=encoding, nrows=5)
#     except:
#         worked = False
#     if worked:
#         print(encoding, ':\n', df.head())

df=pd.read_csv('Dataset_Full_chatbot.csv',encoding='ptcp154')
# Reading the data







df['Query'] = df['Query'].astype(str)
df['Response'] = df['Response'].astype(str)
df.drop_duplicates()
df.dropna()
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
# loading the data

"""## Data Understanding"""

df.shape
# There are 3724 rows and 2 columns in our dataset

df.columns
# Displaying the names of columns present in the dataset

df.info()
# Checking information of the data

df.describe()
# Describe function shows us the frequency,unique and counts of all columns

df.nunique()
# nunique() function return number of unique elements in the object.

df.isnull().sum()
# Checking for the presence of null values in the data. As we can see there are no null values present in the data

df['Query'].value_counts()
# Checking the counts of the values present in the column 'Query'

df['Response'].value_counts()
# Checking the counts of the values present in the column 'Response'

"""## Data Visualization"""

from nltk.sentiment.vader import SentimentIntensityAnalyzer

Text=df['Query']

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()
for sentence in Text:
     #print(sentence)
     sentence=str(sentence)   
     ss = sid.polarity_scores(sentence)
    #  for k in ss:
    #      print('{0}: {1}, ' .format(k, ss[k]), end='')
    #  print()

analyzer = SentimentIntensityAnalyzer()
df['rating'] = Text.apply(analyzer.polarity_scores)
df=pd.concat([df.drop(['rating'], axis=1), df['rating'].apply(pd.Series)], axis=1)
### Creating a dataframe.

df

from wordcloud import WordCloud
# importing word cloud

def wordcloud(df, label):
    
    subset=df[df[label]==1]
    text=df.Query.values
    wc= WordCloud(background_color="black",max_words=1000)

    wc.generate(" ".join(text))

    plt.figure(figsize=(20,20))
    plt.subplot(221)
    plt.axis("off")
    plt.title("Words frequented in {}".format(label), fontsize=20)
    plt.imshow(wc.recolor(colormap= 'gist_earth' , random_state=244), alpha=0.98)
# visualising wordcloud

#wordcloud(df,'question')
# top words in the query column
wordcloud(df,'Query')

wordcloud(df,'Response')
# top words in the response column

"""## Text-Normalization"""

# Removing special characters

import re
# importing regular expressions

punc_lower = lambda x: re.sub('[%s]' % re.escape(string.punctuation), ' ', x.lower())
# Lower case conversion

remove_n = lambda x: re.sub("\n", " ", x)
# removing \n and replacing them with empty value

remove_non_ascii = lambda x: re.sub(r'[^\x00-\x7f]',r' ', x)
# removing non ascii characters

alphanumeric = lambda x: re.sub('\w*\d\w*', ' ', x)
# removing alpha numeric values

df['Query'] = df['Query'].map(alphanumeric).map(punc_lower).map(remove_n).map(remove_non_ascii)
# using map function and applying the function on query column

df['Response'] = df['Response'].map(alphanumeric).map(punc_lower).map(remove_n).map(remove_non_ascii)
#using map function and applying the function on response column

df
# final cleaned dataset

pd.set_option('display.max_rows',3800)
# Displaying all rows in the dataset

df

"""### Important Sentence"""

imp_sent=df.sort_values(by='compound', ascending=False)
# arranging the compound column in descending order to find the best sentence.

imp_sent.head(5)
# printing the first 5 rows

"""### Top Positive Sentence"""

pos_sent=df.sort_values(by='pos', ascending=False)
# Arranging the dataframe by positive column in descending order to find the best postive sentence.

pos_sent.head(5)
# printing the first 5 rows

"""### Top Negative Sentence"""

neg_sent=df.sort_values(by='neg', ascending=False)
# Arranging the dataframe by negative column in descending order to find the best negative sentence.

neg_sent.head(5)
# printing the first 5 rows

"""### Top Neutral Sentence"""

neu_sent=df.sort_values(by='neu', ascending=False)
# Arranging the dataframe by negative column in descending order to find the best neutral sentence.

neu_sent.head(5)
# printing the first 5 rows

from sklearn.feature_extraction.text import TfidfVectorizer
# importing tfidf vectorizer

tfidf = TfidfVectorizer()
# Word Embedding - TF-IDF

factors = tfidf.fit_transform(df['Query']).toarray()
# changing column into array

tfidf.get_feature_names()
# displaying feature names

"""# Application"""

from sklearn.metrics.pairwise import cosine_distances

query = 'who are you ?'
def chatbot(query):
    # step:-1 clean
    query = nu.lemmatization_sentence(query)
    # step:-2 word embedding - transform
    query_vector = tfidf.transform([query]).toarray()
    # step-3: cosine similarity
    similar_score = 1 -cosine_distances(factors,query_vector)
    index = similar_score.argmax() # take max index position
    # searching or matching question
    matching_question = df.loc[index]['Query']
    response = df.loc[index]['Response']
    pos_score = df.loc[index]['pos']
    neg_score = df.loc[index]['neg']
    neu_score = df.loc[index]['neu']
    confidence = similar_score[index][0]
    chat_dict = {'match':matching_question,
                'response':response,
                'score':confidence,
                'pos':pos_score,
                'neg':neg_score,
                'neu':neu_score}
    return chat_dict

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
def start(query):
  while True:
    
    if query == 'exit':
        return "Bye"
        break
        
    response = chatbot(query)
    if response['score'] <= 0.2: # 
        return 'BOT: Please rephrase your Question.'
    
    else:
        # print('='*80)
        # print('logs:\n Matched Question: %r\n Confidence Score: %0.2f \n PositiveScore: %r \n NegativeScore: %r\n NeutralScore: %r'%(
        #     response['match'],response['score']*100,response['pos'],response['neg'],response['neu']))
        # print('='*80)
        return 'BOT: ' + response['response']



import csv
from flask import Flask, render_template,request,redirect,url_for

#import mySQLdb

app = Flask(__name__,template_folder='templates')
#conn = MySQLdb.connect(host='localhost',user='root',password='',db='disease_database')

with open('Testing.csv', newline='') as f:
        reader = csv.reader(f)
        symptoms = next(reader)
        symptoms = symptoms[:len(symptoms)-1]

@app.route("/")
def home():
    return render_template("/homee.html")

@app.route('/chatbot/')
def route1():
    return render_template('index.html')

# @app.route("/get")
# def get_bot_response():
#     query = request.args.get('msg')
#     response = "this is an answer"
#     return response
@app.route("/get")
def get_bot_response():
    query = request.args.get('msg')
    response = start(query)
    return response



@app.route("/Disease Prediction/")
def route2():
    return render_template("home.html",symptoms=symptoms)


@app.route('/disease_predict', methods=['POST'])
def disease_predict():
    selected_symptoms = []
    if(request.form['Symptom1']!="") and (request.form['Symptom1'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom1'])
    if(request.form['Symptom2']!="") and (request.form['Symptom2'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom2'])
    if(request.form['Symptom3']!="") and (request.form['Symptom3'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom3'])
    if(request.form['Symptom4']!="") and (request.form['Symptom4'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom4'])
    if(request.form['Symptom5']!="") and (request.form['Symptom5'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom5'])

    # disease_list = []
    # for i in range(7):
    #     disease = diseaseprediction.dosomething(selected_symptoms)
    #     disease_list.append(disease)
    # return render_template('disease_predict.html',disease_list=disease_list)
    disease,description,precautions = dosomething(selected_symptoms)
    return render_template('disease_predict.html',disease=disease,description=description,precautions=precautions,symptoms=symptoms)

if __name__ == '__main__':
    app.run(debug=True)