import  sqlalchemy
import  pymysql
import  pandas as pd

user_host = 'localhost'
port = int(input("Enter the Port Number (By default 3306): "))
username = str(input("Enter your MySQl server username: "))
passw = str(input("Enter your MySQl server password: "))
db = str(input("Enter the Name of Database you want to retrieve: "))
tb = str(input("Enter the Name of Table you want to retrieve: "))
driver = 'mysql+pymysql'
engine = sqlalchemy.create_engine(f'{driver}://{username}:{passw}@{user_host}:{port}/{db}')
df = pd.read_sql_query(f'SELECT * FROM {tb}', engine)
print(df)
print(df.iterrows())
