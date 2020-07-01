# 0. find/search/locate data

# interview question:

0.a. Difference between loc & iloc & ix:
  
(1) loc gets rows (or columns) with particular labels from the index.

(2) iloc gets rows (or columns) at particular positions in the index (so it only takes integers).

(3) (deprecated) ix usually tries to behave like loc but falls back to behaving like iloc if a label is not present in the index.

# 0.b. find all the row with conditions 

df.loc[(df['A'] > int(100) & (df['B'] > int(100)]
                              
# 1. unique values

# 1.a return unique sorted value from a dataframe


df = pd.DataFrame({'A':[1,1,3,2,6,2,8]})
sorted(set(df.A))

# The answer in List type:

[1, 2, 3, 6, 8]

## 1.b. return unique count in a column

df['x'].nunique()


## 1.c. return unique values in a dataframe column into a list

# will return a list of unique parent_prod_line_nm

list_sorted=sorted(set(df['parent_prod_line_nm']))

### 1.d. return unique combo and counts for more than 1 columns

# https://stackoverflow.com/questions/35268817/unique-combinations-of-values-in-selected-columns-in-pandas-data-frame-and-count

df1.groupby(['A','B']).size().reset_index().rename(columns={0:'count'})



##

## 2. DROP rows or columns related

df=df.drop_duplicates('column_number')

# drop column A & B

df=df.drop(columns=['A','B'])

# https://stackoverflow.com/questions/29763620/how-to-select-all-columns-except-one-column-in-pandas

X=X[[i for i in X.columns.tolist() \
                                if i not in ['A','B']]]


# drop all the rows where match a value in a column


agreement_outliers = [
    'd36d623c16b5786812bf0d214989ccd5',
    '0ea4c358b2cf0adefcc7cd00e072723e',
    'bc49c5e514095654551f4ab8e2cc7815',
    'e2e5ca0bfae0c92a73aba96e567c3168',
    'aff478c6832b4411afc4da645bffb7bf',
    '916eff9502abf8c4ed947fcc1574371f',
    '18c6d978f823123f1fd3e74152aedddb',
    '596703f6c3a5524a812446a251b5001b',
    '886be6e5045017a4443b3f8a279b63eb',
    '9a4c595c0a06d2bba42b033a689a2e9f',
    '7312d6048ede44f2f4caf9df4ede72f9',
    '7c6bcdc5100924ac8e5bd672c6035ff3',
    '23c1be20b420f4a6a3b71a5e03063289',
    'cc92cb5b0a4684fd45eeceb1282f7da6',
    'fb8e5ddda2885cff897b3bc06193e8e8',
    '60a4851cdc8138b677e082b4f6b572cc',
    'c51aca28c3d8a6e2e2af445c62c3aa1f',
    '98edceff83153f892b4fc5389d118637',
    'a120c1f4b020bec4e32da57b75ce95f8',
    '40105f2380473ce9bf8a4ac559530a35']

# https://stackoverflow.com/questions/27965295/dropping-rows-from-dataframe-based-on-a-not-in-condition

X_outliers_removal = X[~X['agreement_number'].isin(agreement_outliers)]


# 3. select columns related

# 3.a.select the last 3 columns

#https://stackoverflow.com/questions/33042633/selecting-last-n-columns-and-excluding-last-n-columns-in-dataframe

dataframe[dataframe.columns[-3:]]


# 3.b. keep ID after train_test_split in sklearn

# put unique ID in the df index and then split

# https://stackoverflow.com/questions/35393775/how-can-i-ensure-that-the-users-and-items-appear-in-both-train-and-test-data-set
#
#
# https://stackoverflow.com/questions/47700151/sklearn-train-test-split-retaining-unique-values-from-columns-in-training-set

# https://stackoverflow.com/questions/43549034/map-predictions-back-to-ids-python-scikit-learn-decisiontreeclassifier

X_train, X_test, y_train, y_test = test_train_split(df.ix[:, ~df.columns.isin(['ID', 'Response'])].values, df.Response)


# 3.c. get the pandas dataframe column name as a list

# https://stackoverflow.com/questions/19482970/get-list-from-pandas-dataframe-column-headers

list(df)

list(my_dataframe.columns.values)

## 4. Time stamps related

# 4.a. get months from mm-dd-yyyy

# df_account_dts_labelled_sum_renewal_qty['asset_sub_end_date_month']='2016-03-24'

df_account_dts_labelled_sum_renewal_qty['asset_sub_end_date_month'] = pd.to_datetime\
(df_account_dts_labelled_sum_renewal_qty['asset_sub_end_date']).dt.to_period('M')

# return 2016-03

df_account_dts_labelled_sum_renewal_qty['asset_sub_end_date_month'] = pd.to_datetime\
(df_account_dts_labelled_sum_renewal_qty['asset_sub_end_date']).dt.month

# return 03

select agreement_number, count(subscription_level) from table

group by agreement_number, count(subscription_level)



## 5. visualization

## 5.a. barplot

df.plot.bar(x='subscription_level', y='agreement_number', rot=30)

## 5.b. self define barplot

def hisplot(column_name, main_title, ylabel, xlabel, bin, filename):
    print('creating hisplot')
    plt.hist(column_name, bins=bin)
    plt.title(main_title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.show()
    plt.savefig(filename)

## 5.c. self define hislot

def barplot(objects, x_pos, main_title, ylabel, xlabel, filename):
    #     objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
    y_pos = np.arange(len(objects))
    #     performance = [10,8,6,4,2,1]

    plt.barh(y_pos, x_pos * 100, align='center', alpha=0.5)
    plt.yticks(y_pos, objects)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(main_title)
    plt.savefig(filename)
    plt.show()

## 5.d qq plot

import statsmodels.api as sm
from matplotlib import pyplot as plt
# Create QQ plot
sm.qqplot(df_account_dts_cleaned['parent_employee_count'], line='45')
plt.show()

## 5.e. adjust legends:

## put legends outside the chart:

# https://stackoverflow.com/questions/23556153/how-to-put-legend-outside-the-plot-with-pandas

# I think you need to call plot before you add the calling legend.

import pandas as pd
import matplotlib.pyplot as plt
a = {'Test1': {1: 21867186, 4: 20145576, 10: 18018537},
    'Test2': {1: 23256313, 4: 21668216, 10: 19795367}}

d = pd.DataFrame(a).T
#print d

f = plt.figure()

plt.title('Title here!', color='black')
d.plot(kind='bar', ax=f.gca())
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()

# ----- Panda solution If you are using pandas Dataframe.plot

dataframe_var.plot.bar().legend(loc='center left',bbox_to_anchor=(1.0, 0.5));

# 5.f. plotting the line plots

# if you have the error "TypeError: float() argument must be a string or a number, not 'Period'"

# call the following line: https://stackoverflow.com/questions/43206554/typeerror-float-argument-must-be-a-string-or-a-number-not-period

pd.plotting.register_matplotlib_converters()

ax1=forecast.plot.line(x='ds', y='yhat', title='Affirm BinHash Forecasting')
ax2=forecast.plot.line(x='ds', y='yhat_lower', ax=ax1)
ax3=forecast.plot.line(x='ds', y='yhat_upper', ax=ax1)

ax1.set(ylabel="Usage Count")

print(ax1 == ax2 == ax3)



## 6. group by

# 6.a. group by with conditions and count x column

df_dts.loc[df_dts['asset_sub_end_date'] >='2017-01-01'].groupby(['parent_prod_line_nm'])['agreement_number'].count()

# 6.b. calculate the time difference between rows

# https://stackoverflow.com/questions/60390101/check-if-each-user-has-consecutive-dates-in-a-python-3-pandas-dataframe/60390256#60390256

df_account_dts["asset_sub_end_date"] = pd.to_datetime(df_account_dts["asset_sub_end_date"],format="%Y-%m-%d")

df_account_dts=df_account_dts.sort_values(by=['account_csn', 'asset_sub_end_date'],ascending=True)

df_account_dts["renewal"] = df_account_dts.groupby(["agreement_number"])["asset_sub_end_date"].diff()

# 6.c. create a new column for number of x per y

df_account_dts_labelled_sum_renewal_qty['num_agreement_per_account_csn']=\
df_account_dts_labelled_sum_renewal_qty\
.groupby(['account_csn'])['agreement_number'].transform(len)

# 6.d. each agreement number has any subscription level which could be gold or silver

# 6.d. pandas dataframe filter a column with a key word based on the aggregation of another column


# https://stackoverflow.com/questions/61034899/pandas-dataframe-filter-a-column-with-a-key-word-based-on-the-aggregation-of-ano/61035533#61035533

# # this query return check if each agreement number has any subscription level which could be gold or not.
# # .astype(int) convert True=1, False=0
#
# df_account_dts_labelled_sum_renewal_qty['agreement_number_has_gold_subscription_levels']=\
#                         df_account_dts_labelled_sum_renewal_qty.groupby\
#                         ('agreement_number')['subscription_level'].\
#                         transform(lambda x: x.str.contains('gold', case=False).any()).astype(int)


# 6.e. pivot table

df_customer_profile_device_platform = df_customer_profile[['customer_id','device_platform']]\
.pivot_table(index="customer_id", aggfunc=("count"))

# 6.f. pivot table return unique numbers

# https://stackoverflow.com/questions/12860421/python-pandas-pivot-table-with-aggfunc-count-unique-distinct

aggfunc=pd.Series.nunique

# 7.a. Replace

# each item in the list has space in between words, so trying to replace space with underscores

a_list = [e.replace(" ", "_") for e in list_sorted]


# 8. select

# https://davidhamann.de/2017/06/26/pandas-select-elements-by-string/

# testing data

# import pandas as pd
#
# #create sample data
# data = {'model': ['Lisa', 'Lisa 2', 'Macintosh 128K', 'Macintosh 512K'],
#         'launched': [1983,1984,1984,1984],
#         'discontinued': [1986, 1985, 1984, 1986]}
#
# df = pd.DataFrame(data, columns = ['model', 'launched', 'discontinued'])

df[df['model'].str.match('Mac')]

df[df['model'].str.contains('ac')]


## 8. compare training and test sets using Kolmogorov–Smirnov test

from scipy import stats

stats.ks_2samp(x_train_outliers_removal['renewal_qty'].values, x_test_outliers_removal['renewal_qty'].values)

for column in x_test_outliers_removal:
    # Select column contents by column name using [] operator

    columnSeriesObj = x_test_outliers_removal[column]

    columnSeriesObj2 = x_train_outliers_removal[column]

    print(column)

    print(stats.ks_2samp(columnSeriesObj.values, columnSeriesObj2.values))

    import random
    import numpy
    from matplotlib import pyplot

    x = columnSeriesObj.values
    y = columnSeriesObj2.values

    bins = np.linspace(0, 10, 100)

    pyplot.hist(x, bins, alpha=1, label='Test')  # color='#0696D7'
    pyplot.hist(y, bins, alpha=1, label='Training')  # , color = 'blue'
    pyplot.legend(loc='upper right')
    pyplot.show()


# 8. create an empty dataframe with the same column names as the other

list(df_original) # return the column names in a list

df_new=pd.DataFrame(columns=list(df_original))
