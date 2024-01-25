import requests
from datetime import datetime
import pandas

data = pandas.read_csv('my_info.csv') #All neccessary informations are kept in this .csv file
my_data = data.to_dict(orient='records')

user_name = my_data[0]['user']
token = my_data[0]['token']
graph_id = my_data[0]['graph_id']
pixela_link = my_data[0]['pixela_link']

def createAccount():
    user_parameters= {'token':'IftikhaRShamSNiloy5916',
                      'username': 'niloy21',
                      'agreeTermsOfService':'yes',
                      'notMinor':'yes'}
    response = requests.post(url=pixela_link, json=user_parameters)
    print(response.text)

def createGraph():
    graph_endpoint_link = f'{pixela_link}/{user_name}/graphs'
    config_graph = {'id':graph_id,
                     'name':'Study Graph',
                     'unit':'Hour',
                     'type':'int',
                     'color':'momiji'}
    response = requests.post(url=graph_endpoint_link, json=config_graph, headers=head)
    print(response.text)

def createData(value):
    pixel_creation_endpoint_link = f'{pixela_link}/{user_name}/graphs/{graph_id}'
    pixel_creation_data = {'date':today,
                           'quantity':value}
    response = requests.post(url = pixel_creation_endpoint_link,
                             json = pixel_creation_data,
                             headers = head)
    print(response.text)

def updateData(new_val):
    update_endpoint_link = f'{pixela_link}/{user_name}/graphs/{graph_id}/{today}'
    new_data = {'quantity':new_val}
    response = requests.put(url=update_endpoint_link, json=new_data, headers=head)
    print(response.text)

access_link = f'{pixela_link}/{user_name}/graphs/{graph_id}.html'
print(access_link)
head = {'X-USER-TOKEN': token}
today = datetime.today()
today = today.strftime('%Y%m%d')
createData('2')
