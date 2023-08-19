import json
import pyodbc

# read from file
with open('config.json') as config_file:
    config_data = json.load(config_file)
server_name = config_data['ServerConfig']['server_name']
dbname_name = config_data['ServerConfig']['dbname_name']
username = config_data['ServerConfig']['username']
password = config_data['ServerConfig']['password']

# make db connection
def create_db_connection():
    conn = pyodbc.connect(
        f'DRIVER={{SQL Server}};SERVER={server_name};DATABASE={dbname_name};UID={username};PWD={password}'
    )
    return conn
