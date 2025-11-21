import psycopg2
import os


"""PostgreSQL 데이터베이스에 연결합니다."""

# 환경 변수 또는 기본값으로 데이터베이스 연결 정보 설정
db_host = "db_postgresql"
db_port = "5432"
db_name = "main_db"
db_user = "admin"
db_password = "admin123"
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
)
print("PostgreSQL 데이터베이스에 성공적으로 연결되었습니다.")
# return conn

with conn.cursor() as cursor :
    # cursor.execute("INSERT INTO users_uuid_name (name) VALUES ('from code');")
    # cursor.execute("""UPDATE users_uuid_name
    #                 SET name = 'code Name'
    #                 WHERE id_name = '48655869-c0a9-4426-9aad-5e895fb0f621';""")
    # 
    cursor.execute("SELECT name, id_name FROM users_uuid_name;")
    records = cursor.fetchall()
    for row in records :
        print(row)
        print(f'{row[0]} : {row[1]}')
conn.commit()

