#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pandas as pd
import numpy as n
from scipy import stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score , confusion_matrix 
from sklearn.model_selection import train_test_split


# In[2]:


# load data
df = pd.read_csv("att_df.csv",index_col=0)
business = pd.read_csv('bars_business.csv')
df = pd.concat([df,pd.DataFrame(business.stars)], axis=1)
# drop NaN
df = df.dropna(axis=0, how='any')
df = df.reset_index(drop=True)


# In[3]:


# solve 'u' and transfer string 
for i in range(df.shape[0]):
  if df.NoiseLevel[i][0] == 'u':
    df.NoiseLevel[i] = df.NoiseLevel[i][1:]
  if df.WiFi[i][0] == 'u':
    df.WiFi[i] = df.WiFi[i][1:]
  if df.Alcohol[i][0] == 'u':
    df.Alcohol[i] = df.Alcohol[i][1:]
  df.BusinessParking[i] = eval(df.BusinessParking[i])
  df.Music[i] = eval(df.Music[i])
  df.Ambience[i] =eval(df.Ambience[i])
  # df.BikeParking[i] = eval(df.BikeParking[i])
  # df.BusinessAcceptsCreditCards[i] = eval(df.BusinessAcceptsCreditCards[i])
  df.RestaurantsReservations[i] = eval(df.RestaurantsReservations[i])
  df.RestaurantsTakeOut[i] = eval(df.RestaurantsTakeOut[i])
  df.RestaurantsDelivery[i] = eval(df.RestaurantsDelivery[i])
  # df.HasTV[i] = eval(df.HasTV[i])
  # df.RestaurantsPriceRange2[i] = eval(df.RestaurantsPriceRange2[i])
  # df.RestaurantsGoodForGroups[i] = eval(df.RestaurantsGoodForGroups[i])
  df.OutdoorSeating[i] = eval(df.OutdoorSeating[i])
  # df.HappyHour[i] = eval(df.HappyHour[i])
  df.NoiseLevel[i] = eval(df.NoiseLevel[i])
  df.WiFi[i] = eval(df.WiFi[i])
  df.Alcohol[i] = eval(df.Alcohol[i])
# drop NaN
df = df.dropna(axis=0, how='any')
df = df.reset_index(drop=True)


# In[4]:


df.head()


# In[5]:


# BusinessParking df
df_bp = pd.DataFrame(df.BusinessParking)


# In[6]:


# insert new cols in df_bp
df_bp.insert(df_bp.shape[1], 'garage', None)
df_bp.insert(df_bp.shape[1], 'street', None)
df_bp.insert(df_bp.shape[1], 'valet', None)
df_bp.insert(df_bp.shape[1], 'validated', None)
df_bp.insert(df_bp.shape[1], 'lot', None)


# In[7]:


# give values
for i in range(df_bp.shape[0]):
  if(df_bp.BusinessParking[i] and 'garage' in df_bp.BusinessParking[i].keys()):
    df_bp.garage[i] = df_bp.BusinessParking[i]['garage']
  if(df_bp.BusinessParking[i] and 'street' in df_bp.BusinessParking[i].keys()):
    df_bp.street[i] = df_bp.BusinessParking[i]['street']
  if(df_bp.BusinessParking[i] and 'valet' in df_bp.BusinessParking[i].keys()):
    df_bp.valet[i] = df_bp.BusinessParking[i]['valet']
  if(df_bp.BusinessParking[i] and 'validated' in df_bp.BusinessParking[i].keys()):
    df_bp.validated[i] = df_bp.BusinessParking[i]['validated']
  if(df_bp.BusinessParking[i] and 'lot' in df_bp.BusinessParking[i].keys()):
    df_bp.lot[i] = df_bp.BusinessParking[i]['lot']
df_bp = df_bp.drop("BusinessParking", axis=1)
df_bp = df_bp.fillna(False)


# In[8]:


df_bp.head()


# In[9]:


# Music df
df_m = pd.DataFrame(df.Music)


# In[10]:


# insert new cols in df_m
df_m.insert(df_m.shape[1], 'dj', None)
df_m.insert(df_m.shape[1], 'background_music', None)
df_m.insert(df_m.shape[1], 'no_music', None)
df_m.insert(df_m.shape[1], 'jukebox', None)
df_m.insert(df_m.shape[1], 'live', None)
df_m.insert(df_m.shape[1], 'video', None)
df_m.insert(df_m.shape[1], 'karaoke', None)


# In[11]:


# give values
for i in range(df_m.shape[0]):
  if(df_m.Music[i] and 'dj' in df_m.Music[i].keys()):
    df_m.dj[i] = df_m.Music[i]['dj']
  if(df_m.Music[i] and 'background_music' in df_m.Music[i].keys()):
    df_m.background_music[i] = df_m.Music[i]['background_music']
  if(df_m.Music[i] and 'no_music' in df_m.Music[i].keys()):
    df_m.no_music[i] = df_m.Music[i]['no_music']
  if(df_m.Music[i] and 'jukebox' in df_m.Music[i].keys()):
    df_m.jukebox[i] = df_m.Music[i]['jukebox']
  if(df_m.Music[i] and 'live' in df_m.Music[i].keys()):
    df_m.live[i] = df_m.Music[i]['live']
  if(df_m.Music[i] and 'video' in df_m.Music[i].keys()):
    df_m.video[i] = df_m.Music[i]['video']
  if(df_m.Music[i] and 'karaoke' in df_m.Music[i].keys()):
    df_m.karaoke[i] = df_m.Music[i]['karaoke']
df_m = df_m.drop("Music", axis=1)
df_m = df_m.fillna(False)


# In[12]:


df_m.head()


# In[13]:


# Ambience df
df_a = pd.DataFrame(df.Ambience)


# In[14]:


# insert new cols in df_m
df_a.insert(df_a.shape[1], 'touristy', None)
df_a.insert(df_a.shape[1], 'hipster', None)
df_a.insert(df_a.shape[1], 'romantic', None)
df_a.insert(df_a.shape[1], 'divey', None)
df_a.insert(df_a.shape[1], 'intimate', None)
df_a.insert(df_a.shape[1], 'trendy', None)
df_a.insert(df_a.shape[1], 'upscale', None)
df_a.insert(df_a.shape[1], 'classy', None)
df_a.insert(df_a.shape[1], 'casual', None)


# In[15]:


# give values
for i in range(df_a.shape[0]):
  if(df_a.Ambience[i] and 'touristy' in df_a.Ambience[i].keys()):
    df_a.touristy[i] = df_a.Ambience[i]['touristy']
  if(df_a.Ambience[i] and 'hipster' in df_a.Ambience[i].keys()):
    df_a.hipster[i] = df_a.Ambience[i]['hipster']
  if(df_a.Ambience[i] and 'romantic' in df_a.Ambience[i].keys()):
    df_a.romantic[i] = df_a.Ambience[i]['romantic']
  if(df_a.Ambience[i] and 'divey' in df_a.Ambience[i].keys()):
    df_a.divey[i] = df_a.Ambience[i]['divey']
  if(df_a.Ambience[i] and 'intimate' in df_a.Ambience[i].keys()):
    df_a.intimate[i] = df_a.Ambience[i]['intimate'] 
  if(df_a.Ambience[i] and 'trendy' in df_a.Ambience[i].keys()):
    df_a.trendy[i] = df_a.Ambience[i]['trendy']
  if(df_a.Ambience[i] and 'upscale' in df_a.Ambience[i].keys()):
    df_a.upscale[i] = df_a.Ambience[i]['upscale']
  if(df_a.Ambience[i] and 'classy' in df_a.Ambience[i].keys()):
    df_a.classy[i] = df_a.Ambience[i]['classy']
  if(df_a.Ambience[i] and 'casual' in df_a.Ambience[i].keys()):
    df_a.casual[i] = df_a.Ambience[i]['casual']
df_a = df_a.drop("Ambience", axis=1)
df_a = df_a.fillna(False)


# In[16]:


df_a.head()


# In[17]:


df1=df.drop(['BusinessParking','Music','Ambience'],axis=1)
df_bp=pd.concat([df_bp,pd.DataFrame(df1.stars)], axis=1)
df_m=pd.concat([df_m,pd.DataFrame(df1.stars)], axis=1)
df_a=pd.concat([df_a,pd.DataFrame(df1.stars)], axis=1)


# In[18]:


# ANOVA Part1
formula = 'stars~C(NoiseLevel)+C(BikeParking)+C(BusinessAcceptsCreditCards)+C(RestaurantsReservations)+C(RestaurantsTakeOut)+C(WiFi)+C(RestaurantsDelivery)+C(HasTV)+C(RestaurantsPriceRange2)+C(Alcohol)+C(RestaurantsGoodForGroups)+C(OutdoorSeating)+C(HappyHour)'
anova1 = anova_lm(ols(formula,df1).fit())
print(anova1)
# NoiseLevel, RestaurantsDelivery, HasTV, OutdoorSeating are significant. Next we will apply Tuckey multiple comparison.


# In[19]:


# Tuckey Multiple Comparison
NL = pairwise_tukeyhsd(df1['stars'],df['NoiseLevel'])
print(NL.summary())
# NoiseLevel: very_loud has less stars than average or very_quiet


# In[20]:


RD = pairwise_tukeyhsd(df1['stars'],df['RestaurantsDelivery'])
print(RD.summary())
# RestaurantsDelivery: False has less stars than True


# In[21]:


HT = pairwise_tukeyhsd(df1['stars'],df['HasTV'])
print(HT.summary())
# HasTV: True has less stars than average or False (maybe it is consistent with preference in quiet places)


# In[22]:


OS = pairwise_tukeyhsd(df1['stars'],df['OutdoorSeating'])
print(OS.summary())
# OutdoorSeating: False has less stars than True


# In[23]:


# ANOVA Part2(Business Parking)
formula = 'stars~C(garage)+C(street)+C(valet)+C(validated)+C(lot)'
anova2 = anova_lm(ols(formula,df_bp).fit())
print(anova2)
# Street is significant. Next we will apply Tuckey multiple comparison.


# In[24]:


# Tuckey Multiple Comparison
S = pairwise_tukeyhsd(df_bp['stars'],df_bp['street'])
print(S.summary())
# street: False has less stars than True


# In[25]:


# ANOVA Part3(Music)
formula = 'stars~C(dj)+C(background_music)+C(no_music)+C(jukebox)+C(live)+C(video)+C(karaoke)'
anova3 = anova_lm(ols(formula,df_m).fit())
print(anova3)
# Background_music, jukebox, karaoke are significant. Next we will apply Tuckey multiple comparison.


# In[26]:


# Tuckey Multiple Comparison
BM = pairwise_tukeyhsd(df_m['stars'],df_m['background_music'])
print(BM.summary())
# background_music: True has less stars than False


# In[27]:


J = pairwise_tukeyhsd(df_m['stars'],df_m['jukebox'])
print(J.summary())
# jukebox: True has less stars than False


# In[28]:


K = pairwise_tukeyhsd(df_m['stars'],df_m['karaoke'])
print(K.summary())
# Karaoke: True has less stars than False


# In[29]:


# ANOVA Part4(Ambience)
formula = 'stars~C(touristy)+C(hipster)+C(romantic)+C(divey)+C(intimate)+C(upscale)+C(classy)+C(casual)'
anova4 = anova_lm(ols(formula,df_a).fit())
print(anova4)
# Romantic, intimate are significant. Next we will apply Tuckey multiple comparison.


# In[30]:


# Tuckey Multiple Comparison
R = pairwise_tukeyhsd(df_a['stars'],df_a['romantic'])
print(R.summary())
# romantic: False has less stars than True


# In[31]:


I = pairwise_tukeyhsd(df_a['stars'],df_a['intimate'])
print(I.summary())
# intimate: False has less stars than True


# In[51]:


# Decision Tree
y = df1['stars'] # labels
x = df1.drop('stars',axis=1) 
x = pd.concat([df1.drop('stars',axis=1),df_bp.drop('stars',axis=1),df_m.drop('stars',axis=1),df_a.drop('stars',axis=1)], axis=1) # data
x = pd.get_dummies(x) # one hot encoding since categorical data cannot be handled well
x_train , x_test , y_train , y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)
# Random Forest
forest = RandomForestClassifier()
forest.fit(x_train , y_train.astype('int'))
# Predict
y_pred_test = forest.predict(x_test)
# Model Performance
print("Accuracy:", accuracy_score(y_test.astype('int') , y_pred_test.astype('int'))) 
print("\nConfusion Matrix:")
print(confusion_matrix(y_test.astype('int') , y_pred_test.astype('int')))

#Accuracy: 0.6477272727272727

#Confusion Matrix:
#[[ 0  0  1]
# [ 0 15 16]
# [ 0 14 42]]


# In[ ]:





# In[ ]:




