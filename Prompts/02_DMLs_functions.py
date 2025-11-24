import psycopg2
from psycopg2 import extras
from typing import Any

# --- 💡 개발 환경 설정 (실제 환경에 맞게 수정 필요) ---
DB_SETTINGS = {
    'host': 'db_postgresql',
    'database': 'main_db', # 실제 DB 이름으로 변경하세요
    'user': 'admin',         # 실제 사용자 이름으로 변경하세요
    'password': 'admin123', # 실제 비밀번호로 변경하세요
    'port': '5432'
}
TABLE_NAME = "books"

# --- 🛠️ 데이터베이스 연결 및 커서 헬퍼 함수 (필수 포함) ---
def execute_query(sql: str, params: tuple = None, fetch_one: bool = False, fetch_all: bool = False) -> Any:
    """SQL 쿼리를 실행하고 결과를 처리하는 범용 헬퍼 함수입니다."""
    conn = None
    try:
        conn = psycopg2.connect(**DB_SETTINGS)
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute(sql, params)

        # SELECT가 아닌 경우 커밋
        if sql.strip().upper().startswith(('CREATE', 'INSERT', 'UPDATE', 'DELETE', 'DROP')):
            conn.commit()
            return True

        # SELECT 결과 반환
        if fetch_one:
            return cur.fetchone()
        elif fetch_all:
            return cur.fetchall()
        
        return None
    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        print(f"🚨 PostgreSQL 오류 발생: {e}")
        return False
    finally:
        if conn:
            conn.close()

# --- 1. 테이블 생성 함수 구현 (create_books_table) ---

def create_books_table() -> None:
    """
    PostgreSQL에 books 테이블을 생성하고, UUID 생성을 위해 uuid-ossp 확장을 활성화합니다.
    """
    print("--- 문제 1: 테이블 생성 ---")
    
    # 1. uuid-ossp 확장 활성화 (ID 자동 생성을 위한 필수 단계)
    execute_query("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";")

    # 2. books 테이블 생성 쿼리
    create_table_sql = f"""
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        title VARCHAR(100) NOT NULL,
        price INT NOT NULL
    );
    """
    
    if execute_query(create_table_sql):
        print(f"✨ 출력 예\n{TABLE_NAME} 테이블이 생성되었습니다.")

if __name__ == '__main__':
    # 테이블 생성 전 안전하게 테이블을 삭제합니다 (테스트용)
    execute_query(f"DROP TABLE IF EXISTS {TABLE_NAME} CASCADE")
    create_books_table()

# --- 2. INSERT 함수 구현 (insert_books) ---

def insert_books() -> None:
    """
    테스트용 데이터를 books 테이블에 삽입합니다. ID는 DB에서 자동 생성됩니다.
    """
    print("--- 문제 2: 데이터 삽입 ---")
    test_data = [
        ("파이썬 입문", 19000),
        ("알고리즘 기초", 25000),
        ("네트워크 이해", 30000),
    ]

    insert_sql = f"INSERT INTO {TABLE_NAME} (title, price) VALUES (%s, %s)"
    
    # execute_query 함수는 단일 쿼리 실행에 최적화되어 있으므로, 
    # executemany를 사용하기 위해 직접 연결을 처리합니다.
    conn = None
    try:
        conn = psycopg2.connect(**DB_SETTINGS)
        cur = conn.cursor()
        
        # executemany를 사용하여 한 번에 여러 행 삽입 (성능 최적화)
        cur.executemany(insert_sql, test_data)
        conn.commit()
        print(f"✅ {len(test_data)}개의 도서 데이터가 성공적으로 삽입되었습니다.")
    
    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        print(f"🚨 데이터 삽입 오류: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    # NOTE: 이 코드를 실행하기 전에 반드시 create_table.py를 먼저 실행해야 테이블이 존재합니다.
    # 안전한 실행을 위해 테이블이 존재하는지 확인하거나, 문제 1의 함수를 포함해야 합니다.
    # 여기서는 삽입 기능만 집중하여 보여줍니다. (테이블이 이미 생성되었다고 가정)
    print("⚠️ 이 코드는 테이블이 미리 생성되어 있어야 실행됩니다.")
    insert_books()
    
    # 삽입 확인용으로 전체 조회 함수를 임시로 호출할 수 있습니다.
    # (실제 실행 시 execute_query 함수 내부에서 SELECT가 정의되어 있어야 함)

# --- 3. SELECT 함수들 구현 ---

def get_all_books() -> List[Dict[str, Any]]:
    """
    books 테이블의 전체 데이터를 제목 기준 오름차순으로 조회합니다.
    """
    select_sql = f"SELECT id, title, price FROM {TABLE_NAME} ORDER BY title ASC"
    results = execute_query(select_sql, fetch_all=True)
    print("\n--- 문제 3-1: 전체 조회 (get_all_books) ---")
    if results:
        for book in results:
            print(f"  ID: {book['id'][:8]}..., 제목: {book['title']}, 가격: {book['price']}원")
    else:
        print("  데이터가 없습니다.")
    return results

def get_expensive_books() -> List[Dict[str, Any]]:
    """
    가격이 25000원 이상인 도서 데이터를 조회합니다.
    """
    select_sql = f"SELECT id, title, price FROM {TABLE_NAME} WHERE price >= 25000"
    results = execute_query(select_sql, fetch_all=True)
    print("\n--- 문제 3-2: 가격 조건 조회 (get_expensive_books) ---")
    if results:
        for book in results:
            print(f"  ID: {book['id'][:8]}..., 제목: {book['title']}, 가격: {book['price']}원")
    else:
        print("  조건에 맞는 도서가 없습니다.")
    return results

def get_book_by_title(title: str) -> Dict[str, Any] | None:
    """
    title 파라미터와 제목이 일치하는 도서 데이터를 조회합니다.
    """
    select_sql = f"SELECT id, title, price FROM {TABLE_NAME} WHERE title = %s"
    result = execute_query(select_sql, (title,), fetch_one=True)
    print(f"\n--- 문제 3-3: 제목 조건 조회 (get_book_by_title - \"{title}\") ---")
    if result:
        print(f"  ID: {result['id'][:8]}..., 제목: {result['title']}, 가격: {result['price']}원")
    else:
        print(f"  제목이 \"{title}\"인 도서를 찾을 수 없습니다.")
    return result

if __name__ == '__main__':
    # NOTE: 이 코드를 실행하기 전에 반드시 create_table.py와 insert_data.py를 먼저 실행해야 데이터가 존재합니다.
    # (데이터가 존재한다고 가정하고 함수들을 호출합니다.)
    get_all_books()
    get_expensive_books()
    get_book_by_title("파이썬 입문")
    get_book_by_title("존재하지 않는 책")

    # --- 4. UPDATE 함수 구현 (update_second_book_price) ---

def update_second_book_price() -> None:
    """
    저장된 순서(제목 기준 오름차순)에서 두 번째 도서의 가격을 27000으로 변경합니다.
    UUID를 먼저 조회 후 UPDATE를 수행합니다.
    """
    print("--- 문제 4: 데이터 수정 ---")
    
    # 1. 두 번째 도서의 ID를 조회 (ORDER BY title ASC, LIMIT 1 OFFSET 1 사용)
    # 참고: 데이터 삽입 순서와 상관없이 제목 순으로 정렬하여 두 번째 항목을 찾습니다.
    select_id_sql = f"SELECT id FROM {TABLE_NAME} ORDER BY title ASC LIMIT 1 OFFSET 1"
    second_book = execute_query(select_id_sql, fetch_one=True)

    if not second_book:
        print("⚠️ 두 번째 도서를 찾을 수 없어 업데이트를 수행하지 않습니다. 데이터가 2개 미만입니다.")
        return

    second_book_id = second_book['id']
    
    # 2. 해당 ID를 사용하여 가격을 업데이트
    update_sql = f"UPDATE {TABLE_NAME} SET price = 27000 WHERE id = %s"
    
    if execute_query(update_sql, (second_book_id,)):
        print(f"✅ 업데이트된 도서 ID (부분): {second_book_id[:8]}...")
        print("✨ 출력 예\n두 번째 도서 가격이 27000으로 수정되었습니다.")
        
if __name__ == '__main__':
    # NOTE: 이 코드를 실행하기 전에 반드시 create_table.py와 insert_data.py를 먼저 실행해야 데이터가 존재합니다.
    update_second_book_price()
    # 수정 확인을 위해 전체 조회 함수 호출 (execute_query 함수 정의 필요)

    # --- 5. DELETE 함수 구현 (delete_third_book) ---

def delete_third_book() -> None:
    """
    저장된 순서(제목 기준 오름차순)에서 세 번째 도서 데이터를 삭제합니다.
    SELECT로 UUID 조회 후 DELETE를 수행합니다.
    """
    print("--- 문제 5: 데이터 삭제 ---")
    
    # 1. 세 번째 도서의 ID를 조회 (ORDER BY title ASC, LIMIT 1 OFFSET 2 사용)
    select_id_sql = f"SELECT id FROM {TABLE_NAME} ORDER BY title ASC LIMIT 1 OFFSET 2"
    third_book = execute_query(select_id_sql, fetch_one=True)

    if not third_book:
        print("⚠️ 세 번째 도서를 찾을 수 없어 삭제를 수행하지 않습니다. 데이터가 3개 미만입니다.")
        return

    third_book_id = third_book['id']
    
    # 2. 해당 ID를 사용하여 데이터 삭제
    delete_sql = f"DELETE FROM {TABLE_NAME} WHERE id = %s"
    
    if execute_query(delete_sql, (third_book_id,)):
        print(f"✅ 삭제된 도서 ID (부분): {third_book_id[:8]}...")
        print("✨ 출력 예\n세 번째 도서가 삭제되었습니다.")

if __name__ == '__main__':
    # NOTE: 이 코드를 실행하기 전에 반드시 create_table.py와 insert_data.py를 먼저 실행해야 데이터가 존재합니다.
    # 또한, 문제 4의 UPDATE가 수행되어 데이터가 2개 이상 남아있어야 합니다.
    delete_third_book()
    # 삭제 확인을 위해 전체 조회 함수 호출 (execute_query 함수 정의 필요)