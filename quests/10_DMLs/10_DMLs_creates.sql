# 문제1
CREATE TABLE news_articles (
    numberID int,
    title varchar(500),
    url varchar(500),
    author varchar(500),
    published_at varchar(500)
);
# 문제2
CREATE TABLE web_links (
    numberID int,
    link_text varchar(500),
    link_url varchar(500),
    category varchar(500),
);

# 문제3
CREATE TABLE scraping_html_results (
    numberID int,
    page_title varchar(500),
    page_url varchar(500),
    html_legth int,
    status_code int
);

# 문제4
CREATE TABLE keyword_search_logs (
    numberID int,
    keyword varchar(500),
    result_count int,
    search_time varchar(500)
);

# 문제5
CREATE TABLE shop_products (
    productID int,
    name varchar(500),
    price int,
    stock int,
    category varchar(500)
);