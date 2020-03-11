## pandas 0.24, python 3

##### (0) connect to the database and return a pandas dataframe

import psycopg2
import hvac
import os

vault = hvac.Client(url='{vault_url}', token=os.environ['environment variables'])

config = {}

config['sql_name'] = vault.read('path')['data']['data']

connection = psycopg2.connect(host=config['sql_name']['host_url'],
                              user=config['sql_name']['host_user'],
                              password=config['sql_name']['host_pass'],
                              database=config['sql_name']['host_db'],
                              port=config['sql_name']['host_port'])

connection.autocommit = True  # without this line the psycopg2 won't insert the data into the database!

# sql_query_test="""
# select * from mqt_staging.pp_table limit 1;
# """
#
# with connection.cursor() as cursor:
#     cursor.execute(sql_query_test)
#     data = pd.DataFrame(cursor.fetchall())
#     print(data.head())

read_sql = "select * from table_{} ;".format(variable1)


tokens = {
                    "variable1": self.variable1,
                    "variable2": self.variable2
                }

read_sql = "select * from table_{} ;".format(**tokens) # the other way to format a SQL query



dataframe_b_read_sql = pd.read_sql(read_sql, connection)                 # read the sql and returns a dataframe


## for update, insert, delete sql queries

delete_sql_queries="delete from schema_name.table_name;"

with connection.cursor() as cursor:
    cursor.execute(delete_sql_queries)


##### (1) fill 'None' as text #####

dataframe_b = pd.DataFrame({'A': 'None None'.split()}) #create a dataframe with the text 'None'

print(dataframe_b)
#      A
#0  None
#1  None

dataframe_b['A']=dataframe_b['A'].replace("None",0)

print(dataframe_b['A'])
#0    0
#1    0
#2    0
#Name: A, dtype: object


##### (2) fill 'None' as an object ##### when the dataframe is empty, it will have 'None' as an object


dataframe_b['A'] = dataframe_b['A'].fillna(value=0) # fill the 'None' objects as 0


##### (3) Check if a dataframe is empty or not #####

if dataframe_b.empty is True:

    # blah blah

elif dataframe_b.empty is False:

    # blah blah

elif dataframe_b['A'].isnull().values.any() is True or dataframe_b['A'].any() == 'None':

## or if there is any null value in the dataframe

## if any value is None as an object

    dataframe_b['A'] = dataframe_b['A'].fillna(value=0)  # fill the 'None' objects as 0

## reference: https://stackoverflow.com/questions/23743460/replace-none-with-nan-in-pandas-dataframe
## https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html

###### (3) Check if the dataframe has a value equal to an int

import pandas as pd
import numpy as np

data = ['2']

df = pd.DataFrame(data)

print(df)

print(str(df.head(n=1)))

if '2' in df.head(n=1).values:
    print('yes')


##### (4) loop over 2 pandas data frames

for index, row in dataframe_b[['column1', 'column2']].iterrows(): # a pandas dataframe always come with index,
                                                         # so the index needs to be in the loop as well

    try:

        # if you want to print the data in the row 1

        print(row['column1'],row['column2'])

    except ValueError as ve:
    print('ValueError: ', ve)
    continue


###### (5) calculate how many rows in a dataframe

number_of_rows = len(dataframe_b['column_name']) # returns an int

if number_of_rows == 0:

    #do something

    continue

elif number_of_rows > 0:

    #do something


# slack
# box


###### (6) find matches between 2 dataframes

def find_matched(self, dataframe_a, dataframe_b, dataframe_a_column, dataframe_b_column, new_column):
    dataframe_a_dict = dataframe_a[ofac_column].value_counts().to_dict()
    dataframe_b[new_column] = dataframe_b[dataframe_b_column].map(dataframe_a_dict)
    dataframe_b[new_column] = dataframe_b[dataframe_b_column].map(dataframe_a_dict)


self.find_matched(dataframe_a, dataframe_b, 'dataframe_a_column', 'dataframe_b_column', 'new_column_name_to_see_if_matched')

###### (6) get dictionary JSON objects

    uuid = json_object['uuid']
    
    
######


###### (7) make a slack post

import json
import requests

class Slack():

    # deal with the key values
    def __init__(self):
         if Slack.kv is None:

            kv = key_values #key_values from somewhere

         self.slack_url = Slack.kv['url']

    def post_message(self, channel, message, attachments=None):

        if attachments is None:
            attachments = {}

        slack_attachments = []
        for att in attachments:
            slack_attachment = {"title": "", "footer": ""}
            if isinstance(att, dict):
                slack_attachment.update(att)
            else:
                slack_attachment['image_url'] = att

            slack_attachments.append(slack_attachment)

        payload = {
            'username': username,
            'icon_emoji': ':whatever_emoji:',
            'link_names': '#an integer',
            'channel': channel,
            'text': message,
            'attachments': slack_attachments
        }
        headers = {
            'cache-control': "no-cache",
            'content-type': "application/x-www-form-urlencoded"
        }

        requests.request("POST", self.slack_url, data=json.dumps(payload), headers=headers)



s = Slack()
s.post_message(slack_channel_name,
                            "message {}".format(123))


###### (8) get time

from datetime import date, datetime, timedelta

jobid_in_timestamp = datetime.now()                         ##get the current time   '%m-%d-%Y %H-%M-%S'

jobid = jobid_in_timestamp.strftime('%m-%d-%Y-%H-%M-%S')    ## add the dash in the space


def __init__(self, params={}):
    self.start_date = params.get('start_date', '')  ## how many dates in integers like 30
    self.end_date = params.get('end_date', '')      ## how many dates in integers like 0
    self.how_many_days_to_look_back = params.get('how_many_days_to_look_back', '')

    if self.how_many_days_to_look_back == '':
        start_date = datetime.today() - timedelta(days=int(self.start_date))

        end_date = datetime.today() - timedelta(days=int(self.end_date))

        how_many_days_to_look_back = 'Between ' + start_date.strftime("%m/%d/%Y") + ' and ' + end_date.strftime(
            "%m/%d/%Y")

###### (9) logging

import logging

def log(self, operation, response, message, actor=None):
    log_info = {
        'operation': operation,
        'response': response,
        'message': message,
        'actor': actor
    }
    logging.info(json.dumps(log_info))


# or log error messages

logging.error(format(e))