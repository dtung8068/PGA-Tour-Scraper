from sklearn.linear_model import LinearRegression
import psycopg2
import os

connection = psycopg2.connect(database=os.getenv('POSTGRES_DATABASE'),
                              user=os.getenv('POSTGRES_USERNAME'),
                              password=os.getenv('POSTGRES_PASSWORD'),
                              port=5432)

cursor = connection.cursor()
cursor.execute("SELECT * FROM TOURNAMENT_DATA WHERE PARS >= 0 AND BOGEYS >= 0 AND EAGLES >= 0 AND DOUBLE_BOGEYS >= 0")
record = cursor.fetchall()

print("Data from Database:- ", record)