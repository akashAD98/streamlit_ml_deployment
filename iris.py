import streamlit as st 
import pandas as pd 
import numpy as np 
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import os


st.write("""

# iris dataset  flower prediction
the app prdoict iris flower dataset

## by **akash desai**  www.github.com/akashAD98
	""")


st.sidebar.header("User input parameter")

def user_input_data():

	sepal_length=st.sidebar.slider('sepal lengrh1',4.3,7.9,5.4)
	sepal_width=st.sidebar.slider(' sepal width',2.0,4.4,3.4)
	petal_length=st.sidebar.slider('petal length',1.0,6.0,1.3)
	petal_width=st.sidebar.slider('petal width ',0.1,2.5,0.2)
	data={'sepal_length':sepal_length,
			'sepal_width':sepal_width,
			'petal_length':petal_length,
			'petal_width':petal_width}

	features=pd.DataFrame(data,index=[0])
	return features

df=user_input_data()

st.subheader('user input parameter')
st.write(df)





iris = datasets.load_iris()
X= iris.data
Y= iris.target

clf=RandomForestClassifier()
clf.fit(X,Y)

prediction=clf.predict(df)
prediction_proba=clf.predict_proba(df)

st.subheader('class label and there corresponding index number ')
st.write(iris.target_names)

st.subheader('prediction ')
st.write(iris.target_names[prediction])

st.subheader('prediction probability ')
st.write(prediction_proba)








