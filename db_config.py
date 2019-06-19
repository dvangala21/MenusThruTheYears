database = {
    'user': 'default', 
    'password': '',
    'port': 3306,
    'host': '35.202.195.199',
    'database': 'restaurant_menu',
    'dialect': 'mysql',
    'driver': 'mysqldb',
    'projectid':'vangala-nuchidat-1553038499976',
    'instancename':'restaurantmenu'
}

# Supported dialects https://docs.sqlalchemy.org/en/13/dialects/index.html

db_prefix = database['dialect']
if database['driver'] is not None:
    db_prefix += "+" + database['driver']

# Logic for building database connection URLS
# DATABASE_URL = f"{db_prefix}://{database['user']}:{database['password']}@{database['host']}:{database['port']}/{database['database']}"
DATABASE_URL = f"{db_prefix}://{database['user']}@{database['host']}/{database['database']}?unix_socket=/cloudsql/{database['projectid']}:{database['instancename']}"
print(DATABASE_URL)