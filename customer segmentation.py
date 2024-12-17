#!/usr/bin/env python
# coding: utf-8

# In[29]:


cd downloads


# In[35]:


cd archive


# In[36]:


import pandas as pd


# In[40]:


data = pd.read_csv('Mall_Customers.csv')


# In[41]:


data.head()


# In[42]:


data.tail()


# In[45]:


data.shape


# In[43]:


data.info()


# In[46]:


data.isnull().sum()


# In[48]:


data.describe()


# In[49]:


data.columns


# In[58]:


X = data[['Annual Income (k$)','Spending Score (1-100)']]


# In[ ]:





# In[66]:


from sklearn.cluster import KMeans


# In[68]:


k_means = KMeans()
k_means.fit(X)


# In[69]:


k_means = KMeans()
k_means.fit_predict(X)


# In[74]:


wcss=[]

for i in range(1,11):
    k_means = KMeans(n_clusters=i)
    k_means.fit(X)
    wcss.append(kmeans.inertia_)


# In[75]:


wcss


# In[76]:


import matplotlib.pyplot as plt


# In[83]:


plt.plot(range(1,11),wcss)
plt.title("Elbow method")
plt.xlabel("number of clusters")
plt.ylabel("WCSS")
plt.show()


# In[ ]:





# In[86]:


X = data[['Annual Income (k$)','Spending Score (1-100)']]
X


# In[88]:


k_means = KMeans(n_clusters=5, random_state=42)
ymeans = k_means.fit_predict(X)


# In[89]:


ymeans


# In[107]:


plt.scatter(X.iloc[ymeans==0,0],X.iloc[ymeans==0,1],s=100,c='red',label='cluster 1')
plt.scatter(X.iloc[ymeans==1,0],X.iloc[ymeans==1,1],s=100,c='yellow',label='cluster 2')
plt.scatter(X.iloc[ymeans==2,0],X.iloc[ymeans==2,1],s=100,c='blue',label='cluster 3')
plt.scatter(X.iloc[ymeans==3,0],X.iloc[ymeans==3,1],s=100,c='green',label='cluster 4')
plt.scatter(X.iloc[ymeans==4,0],X.iloc[ymeans==4,1],s=100,c='black',label='cluster 5')
plt.scatter(k_means.cluster_centers_[:,0],k_means.cluster_centers_[:,1],s=100,c='pink')
plt.title('Customer Segmentation')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend()
plt.show()


# In[121]:


k_means.predict([[70,110]])


# In[122]:


import joblib


# In[124]:


joblib.dump(k_means,"customer segmentation")


# In[125]:


model = joblib.load("customer segmentation")


# In[127]:


model.predict([[60,100]])


# In[138]:


from tkinter import *
import joblib


# In[ ]:


def show_entry_fields():
    p1=int(e1.get())
    p2=int(e2.get())
    
    
    model = joblib.load('customer segmentation')
    result=model.predict([[p1,p2]])
    print("This Customer belongs to cluster no: ", result[0])
    
    if result[0] == 0:
        Label(master, text='Customers with medium annual income and medium annual spending')
    elif result[0]==1:
         Label(master, text='Customers with high annual income and low annual spending')
    elif result[0]==2:
         Label(master, text='Customers with low annual income and low annual spending')
    elif result[0]==3:
         Label(master, text='Customers with low annual income and high annual spending')
    elif result[0]==4:
         Label(master, text='Customers with high annual income and high annual spending')
            
    
master = Tk()
master.title("Customer Segmentation Using Machine Learning")

label = Label(master, text = "Customer Segmentation Using Machine Learning", bg = "black", fg = "white").grid(row=0,columnspan=2)

Label(master,text="Annual Income").grid(row=1)
Label(master, text="Spemding Score").grid(row=2)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)

Button(master, text='Predict', command=show_entry_fields).grid()
mainloop()


# In[ ]:




