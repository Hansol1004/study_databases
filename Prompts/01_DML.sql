# 문제1

CREATE TABLE students (
    id int PRIMARY KEY,
    name varchar(50),
    age int
);

# 문제2
INSERT INTO students (id, name, age)
VALUES (1, '홍길동', 23);
VALUES (2, '이영희', 21);
VALUES (3, '박철수', 26);

# 문제3

SELECT *
FROM students
WHERE age > 22;
WHERE name = '홍길동' ;

# 문제4
UPDATE students
SET age = 25
WHERE id = 2 ;

# 문제5
DELETE FROM students
WHERE id = 3 ;

# 문제6
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(100),
    price INT
);

INSERT INTO books (book_id, title, price)
VALUES (1, '책 A', 10000);

INSERT INTO books (book_id, title, price)
VALUES (1, '책 B', 15000);

```
{
  "전문가_소개": "30년차 경력의 Python, Visual Studio Code 관련 전문가",
  "요청_내용": "아래의 코드 내용을 확인하고 다음의 내용을 작성",
  "작성_항목": [
    {
      "질문": "어떤 에러가 발생하였는가?"
    },
    {
      "질문": "왜 발생하는가?"
    },
    {
      "질문": "PRIMARY KEY 의 규칙을 쓰시오."
    }
  ],
  "코드_내용": [
    "CREATE TABLE books (",
    "    book_id INT PRIMARY KEY,",
    "    title VARCHAR(100),",
    "    price INT",
    ");",
    "",
    "INSERT INTO books (book_id, title, price)",
    "VALUES (1, '책 A', 10000);",
    "",
    "INSERT INTO books (book_id, title, price)",
    "VALUES (1, '책 B', 15000)"
  ]
}
```
```
### 1. 어떤 에러가 발생하였는가?

**`PRIMARY KEY` 제약 조건 위반 (Constraint Violation)** 에러가 발생합니다.

* **에러 메시지 예시:**
    * `Integrity Constraint Violation`
    * `Duplicate entry '1' for key 'PRIMARY'`
    * `UNIQUE constraint failed: books.book_id`

---

### 2. 왜 발생하는가?

에러는 두 번째 `INSERT` 구문 때문에 발생합니다.

* **원인:** `book_id` 컬럼은 **PRIMARY KEY**로 지정되었으며, 이는 해당 컬럼에 **중복된 값**을 허용하지 않습니다.
* **충돌 지점:** 첫 번째 `INSERT`에서 `book_id` **1**을 성공적으로 삽입했으나, 두 번째 `INSERT`에서 동일한 `book_id` **1**을 다시 삽입하려고 시도하여 **고유성(Uniqueness)** 규칙을 위반했기 때문에 데이터베이스가 작업을 거부하고 에러를 발생시킵니다. 

---

### 3. PRIMARY KEY 의 규칙을 쓰시오.

PRIMARY KEY (주 키)는 관계형 데이터베이스에서 테이블 내의 각 레코드(행)를 고유하게 식별하기 위해 사용됩니다.

* **고유성 (Uniqueness) 🔑:** 키의 값은 테이블 내에서 **중복될 수 없습니다**.
* **NOT NULL (비어 있지 않음) 🚫:** 키의 값은 **NULL**을 가질 수 없습니다. 모든 레코드는 반드시 키 값을 가져야 합니다.
* **단일성:** 하나의 테이블에 **오직 하나의 PRIMARY KEY**만 지정할 수 있습니다. (여러 컬럼을 묶은 복합 키는 가능)
* **식별자:** 테이블의 레코드를 대표하고 고유하게 구분하는 주요 식별자 역할을 합니다.
```