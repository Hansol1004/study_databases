# 문제1
INSERT INTO news_articles (numberID, title, url, author, published_at)
VALUES (1, 'AI 시대 도래', 'https://news.com/ai', '홍길동', '2025-01-01');
VALUES (2, '경제 성장률 상승', 'https://news.com/economy', '이영희', '2025-01-05');

# 문제2
INSERT INTO web_links (numberID, link_text, link_url, category) 
VALUES (1, '네이버', 'https://www.naver.com', 'portal');
VALUES (2, '구글', 'http://google.com', 'portal');
VALUES (3, '깃허브', 'https://github.com', 'dev');

# 문제3
INSERT INTO scraping_html_results (numberID, page_title, page_url, html_legth, status_code) 
VALUES (1, '홈페이지', 'https://site.com', 15700, 200);
VALUES (2, '블로그', 'https://blog.com', 9800, 200);
VALUES (3, '404페이지', 'https://site.com/notfound', 0, 404);

# 문제4
INSERT INTO keyword_search_logs (numberID, keyword, result_count, search_time) 
VALUES (1, 'python', 120, '2025-11-19 10:00:00');
VALUES (2, 'chatgpt', 300, '2025-11-19 10:05:00');
VALUES (3, 'docker', 90, '2025-11-19 10:10:00');

# 문제5
INSERT INTO shop_products (productID, name, price, stock, category)
VALUES (1, 'USB 메모리', 12000, 50, '전자제품');
VALUES (2, '블루투스 스피커', 45000, 20, '전자제품');
VALUES (3, '물병', 5000, 100, '생활용품');