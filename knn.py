import os

import numpy as np
from flask import send_file, abort, jsonify
from sklearn.cluster import KMeans

import pandas as pd
import json
#from cloudmesh-admin.cloudmesh.mongo.CmDatabase import CmDatabase
#from cloudmesh_admin import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.metrics import confusion_matrix
from flask import request
from werkzeug.datastructures import FileStorage
import tkinter as tk
from tkinter import filedialog

#cmdb = CmDatabase()
# db = cmdb.client["cloudmesh"]
# data = db["local-file"]
#db = cmdb.client["cloudmesh_ai"]
#collection = db["files"]


def upload(file=None):
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()

    df=pd.read_csv(file_path)
 #   df.to_json('datajson.json')
 #   jdf=open('datajson.json').read()
 #   data=json.loads(jdf)
 #   collection.insert_one({"filename": data})
    return df


def fit(df):
    #d=pd.DataFrame(list(collection.find()))
    #d=pd.read_csv(file)
    X=df.iloc[:,:-1].values
    y=df.iloc[:,-1]
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20)


    #Scaling

    #scaler=StandardScaler()
    #scaler.fit(X_train)
    #X_train=scaler.transform(X_train)
    #X_test=scaler.transform(X_test)

    classifier =KNeighborsClassifier(n_neighbors=3)
    classifier.fit(X_train,y_train)

    return X_test,y_test,classifier





def predict(X_test,y_test,classifier):

    y_pred=classifier.predict(X_test)
    confusion=confusion_matrix(y_test,y_pred)
    accuracy=accuracy_score(y_test,y_pred)

    output_file = open('Accuracy.txt', 'w')
    output_file.write('Accuracy is: \n' + str(accuracy))
    output_file.close()

    return output_file


#col,df=upload()
#X_test,y_test,classifier=fit(df)
#conf,accu=predict(X_test,y_test,classifier)






