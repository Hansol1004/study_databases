## 문제 해결을 하기 위한 json 코드 제작 프롬프트
```
당신은 30년 경력의 visual studio code, python 코드 개발자 입니다.

아래의 요구사항 들에 맞는 python 함수를 제작해야 합니다.

아래의 문제들을 해결하기 위한 내용을 json형식의 프롬프트로 출력 먼저 하고,

문제들을 해결해야함.

아래 항목의 내용들을 답변의 결과를 적지 않고 형식만 출력할 것.

[아래]

<문제 해결을 위한 프롬프트>

## 문제 1 테이블 생성 함수 만들기

아래 요구사항에 맞게 **Python 함수(create_books_table())**를 작성하시오.
 함수 실행 시 PostgreSQL에 books 테이블이 생성되어야 한다.
✔ 요구사항
테이블명: books
컬럼명
자료형
id
UUID PRIMARY KEY DEFAULT uuid_generate_v4()
title
VARCHAR(100)
price
INT

✨ 출력 예
books 테이블이 생성되었습니다.

## 문제 2 INSERT 함수 만들기

아래 데이터를 books 테이블에 추가하는 insert_books() 함수를 작성하시오.
✔ 테스트용 데이터
id
title
price
1
파이썬 입문
19000
2
알고리즘 기초
25000
3
네트워크 이해
30000

🔥 id는 자동 UUID이므로 INSERT 시 제외

## 문제 3  SELECT 함수 만들기
아래 조건을 만족하는 조회용 Python 함수들을 작성하시오.
✔ 요구 함수
전체 조회 함수


함수명: get_all_books()


가격이 25000원 이상인 데이터 조회 함수


함수명: get_expensive_books()


title 이 “파이썬 입문”인 데이터 조회 함수


함수명: get_book_by_title()


parameter: title


## 문제 4 UPDATE 함수 만들기

저장된 순서에서 두 번째 도서의 가격을 27000으로 변경하는 함수를 만드시오.
함수명: update_second_book_price()


옵션:


두 번째 도서의 UUID를 SELECT 로 먼저 가져온 후


UPDATE 를 수행한다.


✨ 출력 예
두 번째 도서 가격이 27000으로 수정되었습니다.

## 문제 5 DELETE 함수 만들기

저장된 순서에서 세 번째 도서 데이터를 삭제하는 Python 함수를 작성하시오.
함수명: delete_third_book()


옵션:


SELECT로 UUID 조회 후 DELETE 수행


✨ 출력 예
세 번째 도서가 삭제되었습니다.
```

##  출력된 json 코드와 문제 해결 프롬프트

```
당신은 30년 경력의 visual studio code, python 코드 개발자 입니다.

아래의 json코드 형식의 질문들에 대한 답변들을 합니다.

python 코드로 출력하며, 문제마다 각각 따로 코드들을 작성.

[json 형식]
{
  "문제 1 테이블 생성 함수 만들기": {
    "함수명": "create_books_table",
    "요구사항": "PostgreSQL books 테이블 생성",
    "사용_라이브러리": "psycopg2",
    "DB_설정": "UUID 생성 기능(uuid-ossp extension) 활성화 필요",
    "SQL_구문": "CREATE TABLE books (id UUID PRIMARY KEY DEFAULT uuid_generate_v4(), title VARCHAR(100) NOT NULL, price INT NOT NULL)",
    "출력_예": "books 테이블이 생성되었습니다."
  },
  "문제 2 INSERT 함수 만들기": {
    "함수명": "insert_books",
    "요구사항": "3권의 테스트 도서 데이터를 books 테이블에 삽입",
    "사용_라이브러리": "psycopg2",
    "데이터_구성": [
      {"title": "파이썬 입문", "price": 19000},
      {"title": "알고리즘 기초", "price": 25000},
      {"title": "네트워크 이해", "price": 30000}
    ],
    "SQL_구문": "INSERT INTO books (title, price) VALUES (%s, %s)",
    "특징": "id 컬럼은 DEFAULT 값이 적용되므로 INSERT 시 제외"
  },
  "문제 3 SELECT 함수 만들기": {
    "전체_조회": {
      "함수명": "get_all_books",
      "SQL_구문": "SELECT id, title, price FROM books"
    },
    "가격_조건_조회": {
      "함수명": "get_expensive_books",
      "조건": "가격 >= 25000",
      "SQL_구문": "SELECT id, title, price FROM books WHERE price >= 25000"
    },
    "제목_조건_조회": {
      "함수명": "get_book_by_title",
      "파라미터": "title (제목)",
      "SQL_구문": "SELECT id, title, price FROM books WHERE title = %s"
    },
    "결과_처리": "조회 결과를 Dictionary 리스트 형태로 반환"
  },
  "문제 4 UPDATE 함수 만들기": {
    "함수명": "update_second_book_price",
    "요구사항": "저장된 순서 기준 두 번째 도서의 가격을 27000으로 수정",
    "작업_순서": [
      "1. SELECT 쿼리로 두 번째 도서의 UUID를 조회 (ORDER BY title ASC, LIMIT 1 OFFSET 1 사용)",
      "2. 조회된 UUID를 사용하여 UPDATE 쿼리 실행"
    ],
    "UPDATE_SQL_구문": "UPDATE books SET price = 27000 WHERE id = %s",
    "출력_예": "두 번째 도서 가격이 27000으로 수정되었습니다."
  },
  "문제 5 DELETE 함수 만들기": {
    "함수명": "delete_third_book",
    "요구사항": "저장된 순서 기준 세 번째 도서 데이터 삭제",
    "작업_순서": [
      "1. SELECT 쿼리로 세 번째 도서의 UUID를 조회 (ORDER BY title ASC, LIMIT 1 OFFSET 2 사용)",
      "2. 조회된 UUID를 사용하여 DELETE 쿼리 실행"
    ],
    "DELETE_SQL_구문": "DELETE FROM books WHERE id = %s",
    "출력_예": "세 번째 도서가 삭제되었습니다."
  }
}
```