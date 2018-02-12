
# coding: utf-8

# In[17]:


import pickle
filename = './model/finalized_model.sav'
knn = pickle.load(open(filename, 'rb'))


# In[22]:


X_validation = [[6.3,3.3,4.7,1.6]]

predictions = knn.predict(X_validation)


# In[23]:


predictions[0]

