
# coding: utf-8

# In[17]:


import pickle
import os 
import sklearn

def predict(arr):

    filename = '/model/finalized_model.sav'
    knn = pickle.load(open(os.path.dirname(__file__)+filename, 'rb'))
    # [6.3,3.3,4.7,1.6]
    X_validation = [arr]
    predictions = knn.predict(X_validation)
    return predictions[0]