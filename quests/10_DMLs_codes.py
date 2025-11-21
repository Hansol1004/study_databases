# 문제1

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
    # 문제2
    # cursor.execute("INSERT INTO students_01 (name, age) VALUES ('홍길동', 23);")
    # cursor.execute("INSERT INTO students_01 (name, age) VALUES ('이영희', 21);")
    # cursor.execute("INSERT INTO students_01 (name, age) VALUES ('박철수', 26);")
    # 문제3
    # cursor.execute("SELECT * FROM students_01;")
    # records = cursor.fetchall()
    # for row in records :
    #     print(row)
    # cursor.execute("SELECT age FROM students_01;")
    # records = cursor.fetchall()
    # for row in records :
    #     if row[0] >= 22 :
    #         print(row[0])
    # cursor.execute("SELECT name FROM students_01;")
    # records = cursor.fetchall()
    # for row in records :
    #     if row[0] == '홍길동' :
    #         print(row[0])
    # 문제4
    # cursor.execute("SELECT id_name FROM students_01;")
    # records = cursor.fetchall()
    # for row in records :
    #     print(row)
    # cursor.execute("""UPDATE students_01
    #                  SET age = 25
    #                  WHERE id_name = '7d6e2f86-6c02-426f-a519-153d72d6187f';""")
    # cursor.execute("DELETE FROM students_01 WHERE id_name = '7d6e2f86-6c02-426f-a519-153d72d6187f';")
    # 문제5
    # cursor.execute("SELECT id_name FROM students_01;")
    # records = cursor.fetchall()
    # for row in records :
    #     print(row)
    # cursor.execute("DELETE FROM students_01 WHERE id_name = 'db97ce28-70ef-4d98-8722-0947de157bfa';")
conn.commit()

# 문제6
# {
#   "질문_내용": [
#     {
#       "항목": "발생한_에러",
#       "내용": "어떤 에러가 발생하였는가?"
#     },
#     {
#       "항목": "에러_원인",
#       "내용": "왜 발생하는가?"
#     },
#     {
#       "항목": "PRIMARY_KEY_규칙",
#       "내용": "PRIMARY KEY 의 규칙을 쓰시오."
#     }
#   ],
#   "제공된_코드": [
#     "CREATE TABLE books (book_id INT PRIMARY KEY, title VARCHAR(100), price INT);",
#     "INSERT INTO books (book_id, title, price) VALUES (1, '책 A', 10000);",
#     "INSERT INTO books (book_id, title, price) VALUES (1, '책 B', 15000);"
#   ]
# }


# 1. 발생한 에러
# 에러 유형: PRIMARY KEY 제약 조건 위반 오류 (Constraint Violation Error)

# 구체적인 에러 메시지 (일반적인 예시):

# UNIQUE constraint failed: books.book_id

# Duplicate entry '1' for key 'books.PRIMARY'

# 2. 왜 발생하는가?
# 원인: book_id 컬럼이 **PRIMARY KEY**로 정의되어 있기 때문입니다.

# 문제 상황:

# 첫 번째 INSERT 문: book_id에 값 1 삽입 (성공).

# 두 번째 INSERT 문: 다시 book_id에 값 1을 삽입하려고 시도 (실패).

# 결과: PRIMARY KEY는 중복된 값을 허용하지 않는다는 고유성(Uniqueness) 규칙을 강제하므로, 두 번째 삽입 시도에서 데이터베이스가 에러를 발생시키고 트랜잭션을 거부합니다.

# 3. PRIMARY KEY (기본 키) 의 규칙
# PRIMARY KEY는 테이블의 각 행(Row)을 고유하게 식별하기 위한 핵심 요소이며, 다음의 규칙을 반드시 따릅니다.

# ✅ 고유성 (Uniqueness): PRIMARY KEY 값은 테이블 내에서 항상 고유해야 합니다. 중복 값은 절대 허용되지 않습니다.

# ✅ NULL 불허 (NOT NULL): PRIMARY KEY 컬럼에는 NULL 값이 들어갈 수 없습니다. 모든 행은 식별 가능한 값을 가져야 합니다.

# ✅ 단일성 (Single Key): 하나의 테이블에는 **오직 하나의 PRIMARY KEY**만 지정될 수 있습니다. (다만, 여러 컬럼을 묶어 하나의 복합 기본 키를 만드는 것은 가능합니다.)