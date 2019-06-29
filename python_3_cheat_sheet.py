

##

## pandas 0.24

##### (1) fill 'None' as text #####

df = pd.DataFrame({'A': 'None None'.split()}) #create a dataframe with the text 'None'

print(df)
#      A
#0  None
#1  None

df['A']=df['A'].replace("None",0)

print(df['A'])
#0    0
#1    0
#2    0
#Name: A, dtype: object


##### (2) fill 'None' as an object ##### when the dataframe is empty, it will have 'None' as an object


df['A'] = df['A'].fillna(value=0) # fill the 'None' objects as 0


##### (3) Check if a dataframe is empty or not #####

if df.empty == True:

    # blah blah

elif df['A'].isnull().values.any() == True or df['A'].any() == 'None':

## or if there is any null value in the dataframe

## if any value is None as an object

    df['A'] = df['A'].fillna(value=0)  # fill the 'None' objects as 0

## reference: https://stackoverflow.com/questions/23743460/replace-none-with-nan-in-pandas-dataframe
## https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html


