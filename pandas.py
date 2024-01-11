
# -*- coding: utf-8 -*-

import pandas as pd
#to read a csv file
df=pd.read_csv('address of csv file')
#shape returns no of rows and columns of dataframe, info retruns all info about the dataframe
df.shape #shape is an attribute
df.info() #info is a method
#normally 25 columns and 5 rows from start and 5 from end is showing but we can use this option
pd.set_option('display.max_columns', 85)# prints 85 columns
pd.set_option('display.max_rows',95) #prints 95 rows
df.head(10)
df.tail()
#before we get into dataframe lets look at some dictionaries

dict1={
       ' Name':'ALi',
       ' LastName':'Ahmadi',
       ' Email':'aliahmadi@gmail.com'
        }
dict2={
       'name':['ali','lunatic'],
       'lastname':['ahmadi','crazy'],
       'email':['aliahmadi@gmail.com','crazy@gmail.com']  
       }
dict3={
       'name':['ali','hassan','jawad'],
       'lastname':['ahmadi','hassani','jawadi'],
       'email':['aliahmadi@gmail.com','hassani@gmail.com','jawadi@gmail.com'],
       'salary':[10000,50000,60000],
       'skills':['python,jave,php','java,sql,php','php,python,sql'],
       'country':['India','Bamyan','Jamaica'],
       'answer':['yes','no','yes'],
       'age':[25,40,88]
       }
#accessing keys of the dictionary
print(dict3['lastname'])
print(dict3['name'],dict3['email'])

#converting dictionary to dataframe and accessing its columns, accessing is like dictionary we can access by columns names
df=pd.DataFrame(dict3)
print(df['name'])
#or
print(df.name)

#A dataframe has many data serieses, each column is a data series or series, but a series is a list of items, its like one dimensional array
print(type(df['name']))
#the following is a series
print(df['name'])

#accessing many columns
print(df[['name','email']])
#to get the column names
print(df.columns)
#to get the rows we have, loc and iloc attributes iloc is integer location for which you only pass integers as rows or columns
#accessing one or multiple rows
print(df.iloc[0])
#accessing many rows
print(df.iloc[[0,1]])
#accessing rows with specific columns, we can not pass column name only its index should be passed


print(df.iloc[[1,2],2])

print(df.iloc[[1,2],[0,2]])
#using loc, with loc we can column labels
#accessing first row
print(df.loc[0])
#accessing many row one columns and more
print(df.loc[[0,2],'email'])
print(df.loc[[0,2],['email','name']])
#it counts how many of times one value is repeated
print(df['name'].value_counts())
#using slicing
print(df.loc[0:2,'email'])
print(df.loc[0:2,'name':'email'])
#one specific cell
print(df.loc[0,'email'])
#to set the email column as the index
df.set_index('email')
#to access using index
df.loc('aliahmadi@gmail.com')
#if once you set using the set_index then you can reset it
df.reset_index(inplace=True)
#if you got unsorted words index, you can sort it
df.sort_index()


#filtering

filt=(df['lastname']=='hassani')
print(df[filt])
print(filt)#it gives true or false answer
df.loc[filt,'email'] #getting emails for true values
filt2=(df['lastname']=='hassani' ) & (df['name']=='hassan') # | is or
#to find the opposite of filt or the values which are not true or =='hassani',all except the filt
df.loc[-filt,'email']
#if we have a salary column
highsalary=(df['salary']>30000)
print(df.loc[highsalary,['name','email']])

names=['ali','hassan']
filt=df['name'].isin(names)
print(df[filt])
#sometimes a cell contains many values so we use this method, na=False avoids errors if we face na value
filt=df['skills'].str.contains('python',na=False)
print(df.loc[filt,'skills'])

#changing column labels and rows
#if you change all column names do as follow
df.columns=['firstname','last','emailha','allowance','languages']
#to upper case all column names
df.columns=[x.upper() for x in df.columns]
print(df)
#to replace space with underscore
df.columns=df.columns.str.replace(' ','_')
#changing few columns names
df.rename(columns={'firstname':'name','last':'lastname','emailha':'emails'},inplace=True)
#to change a rows data
df.loc[2]=['John','Smith','johnsmith@gmail.com','80000','django,javascript,flask,java,python']
#updating specifc cells
df.loc[2,['name','email']]=['jackson','jackson@gmail.com']
#changing single value
df.loc[2,'name']='lunatic'
df.at[2,'name']='lunatic'
#the following single value change gives an error
filt=(df['name']=='lunatic')
df[filt]['lastname']='Jungli'
#to solve
df.loc[filt,'lastname']='Jungli'
#to lower case col values
df['email']=df['email'].str.lower()

#to find the len of all cells of a column
#apply usages with series
df['email'].apply(len)
#function
def update_email(email):
    return email.upper()
df['email'].apply(update_email)
#or use lambda 
df['email'].apply(lambda x: x.lower())
#to find len of each column, axis='columns' does it on rows
df.apply(len,axis='columns')
#to grab min of each column, str gives firsts in alpabet,following both are same
df.apply(pd.Series.min)
df.apply(lambda x: x.min())

#applymap does calc on each cell, it is only for Dataframe not series, int has no len
df.applymap(len)
df.applymap(str.lower)# if you have int in your df then it can give error since str.lower is str method, len also
#replace and map are series methods
df['name'].map({'ali':'nokol','lunatic':'crazy'}) #but the names we did not give value in the map becomes NAN
#In order to avoid getting nan we use replace
df['name'].replace({'ali':'nokol','lunatic':'crazy'})


df2=pd.DataFrame(dict2)
df=pd.DataFrame(dict3)

#addding and removing columns
df['fullname']=df['name']+' '+df['lastname']
df.drop(columns=['fullname','name'],inplace=True)
#to separate full names into name and lastname, use expand to make it a df
df['fullname'].str.split(' ',expand=True)
#to assign them to two columns
df[['good','bad']]=df['fullname'].str.split(' ',expand=True)
#to add a row, ignore_index=true to avoid erro
df.append({'first':'tony'},ignore_index=True)
#to append one df to another, remember append has no inplace argument
df.append(df2,ignore_index=True)
#to drop using index
df.drop(index=4)
#using conditions, drop has inplace argument
df.drop(index=df[df['lastname']=='jawadi'].index)
#or do this
filt=df['lastname']=='jawadi'
df.drop(index=df[filt].index)

#sorting df
df.sort_values(by='name',ascending=False)
#sorting by two columns, one after other,first sort by name then by lastname 
df.sort_values(by=['name','lastname'],ascending=False)
#sorting name in ascending, lastname in descending order
df.sort_values(by=['name','lastname'],ascending=[False,True])
#sort by index, or sort series
df.sort_index()
df['name'].sort_values()
#finding two  largest salaries
df['salary'].nlargest(2)
#gives all details for the largest salary holders
df.nlargest(2,'salary')

#grouping methods
df['salary'].head(2)
df.median()
df.describe()
df['country'].value_counts()
#use normalize=true to count by percentage, yes or no
df['answer'].value_counts(normalize=True)
df.count()
countryGroup=df.groupby(['country'])
countryGroup.get_group('Bamyan')
countryGroup['skills'].value_counts()
#the following finds which social media is more used in one country
countryGroup['socialmedia'].value_counts().loc['Jamaica']
#finding the median salary in jamaica
countryGroup['salary'].median().loc['Jamaica']
#if we want to see few aggregate function 
countryGroup['salary'].agg(['median','mean']).loc['Bamyan']
#to find how many peopl knew python in one country, first using filter
filt=df['country']=='Jamaica'
df.loc[filt]['skills'].str.contains('python').sum()
#using group to find python skilled people, first one gives error
countryGroup['skills'].str.contains('python').sum()
#to solve it use the apply method, finds how many people know python in each country
countryGroup['skills'].apply(lambda x: x.str.contains('python').sum())


#handling na or missing values, the default is droping rows with one or more missing values
df.dropna(axis='index',how='any')#index or 0, columns or 1
df.dropna(axis=0,how='all')#if all values of a row is na will be dropped
#dropping na based on a column, if these subset columns are not missing then dont dropna
df.dropna(axis=0,subset=['lastname','email'])
#handling missing or na values when creating datagrame
df.pd.DataFrame(dict2)
df.replace('NA',np.nan,inplace=True)
df.replace('Missing',np.nan,inplace=True)
#to check if a values is na
df.isna()
#to fill na values
df.fillna('MISSING') #OR df.fillna(0)
#to check column dtypes
df.dtypes
#na is a float
type(np.nan)
#if your column has missing values, either you fill that na values to zero, or you use float to cast them
#this gives error
df['age']=df['age'].astype(int)
#but this works
df['age']=df['age'].astype(float)
#to cast whole dataframe of numbers
df.astype(float)


dictn={
       'date':['2020-03-13 06-PM','2020-03-13 05-PM','2020-03-13 04-PM','2020-03-13 03-PM','2020-03-13 02-PM',
               '2021-03-13 06-PM','2021-03-13 05-PM','2019-03-13 04-PM','2019-03-13 03-PM','2019-03-13 02-PM'],
       'close':[13.5,15,19,20,20.5,
               40,50,3,2,8]
       
       }
pd.to_csv(dictn.csv)
df=pd.DataFrame(dictn)
#datetime handling and methods
df['date']=pd.to_datetime(df['date'],format='%Y-%m-%d %I-%p')
df.loc[0,'date'].day_name()
#suppose dictn is also saved as csv, importing it and setting date as date
d_parser=lambda x: pd.datetime.strptime(x,'%Y-%m-%d %I-%p')
df=pd.read_csv('dictn.csv',parse_dates=['date'],date_parser=d_parser)
#find all days of date
df['date'].dt.day_name()
df['date'].min()#oldest date
df['date'].max()#most recent date
df['date'].max()-df['date'].min()
#filtering
filt=(df['date']>='2020')#or filt=(df['date]>='2019) & (df['date]<'2020')
df.loc[filt]
# second method
filt=(df['date']>=pd.to_datetime('2019-03-13')) & (df['date']< pd.to_datetime('2021-03-13'))
#to set index as date then we can do these
df.set_index('date',inplace=True)
#to filter now
df['2020-03-13':'2021-03-13']['close'].mean()
df['2020']
#to find the max of daily
df['close'].resample('D').max()
#for jupyter to plot inline use following
%matplotlib inline
sampl=df.resample('w').mean()
#to find different agg for different columns
df.resample('w').agg({'close':'mean','high':'max','Adj Close':'min'})
print(sampl)


#adding rows to the end of a dataframe

df.loc[len(df)]=[name,lastname,age]



#droping duplicates based on two columns
    df.drop_duplicates(subset=['col','schedule'],keep='first',inplace=True)
    df.reset_index(drop=True,inplace=True)



cols_with_missing = [col for col in X_train.columns
                     if X_train[col].isnull().any()] 

# Drop columns in X_train data
reduced_X_train = X_train.drop(cols_with_missing, axis=1)


#it is used to make multiindex just an index

df.index=df.index.droplevel[0]


#changing seconds to datetime, need to specify the unit=s, data['time'] is time in seconds
data['time']=pd.to_datetime(data['time'],unit='s')


x=1648737903882 #it is unix time in milliseconds
#changin unix time to a naive time
time=pd.to_datetime(x,unit='ms')
print(time)
#the above outputs: 2022-03-31 14:45:03.882000 , which is a naive 
#to change the above naive time to my local time, we first localize the naive time to utc and then change it to ours 
dt_now_kabul=time.tz_localize('UTC').tz_convert('Asia/Kabul')
print(dt_now_kabul)

#to change a dataframe column which contains naive datetime, do as following
df['Date'] = df['Date'].dt.tz_localize('UTC').dt.tz_convert('Asia/Kolkata')
print (df['Date'])

#generating naive datetime and converting to local time
start = pd.to_datetime('2015-02-24')
rng = pd.date_range(start, periods=10)
df = pd.DataFrame({'Date': rng, 'a': range(10)})  

df.Date = df.Date.dt.tz_localize('UTC').dt.tz_convert('Asia/Kolkata')
print (df)
           










