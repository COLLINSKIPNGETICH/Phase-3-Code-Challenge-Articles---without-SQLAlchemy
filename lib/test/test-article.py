# article_test.py
from article import Article
from author import Author
from magazine import Magazine

def test_article_title():
    article = Article(Author("John Doe"), Magazine("Magazine 1", "Category 1"), "Article 1")
    assert article.title == "Article 1"

def test_article_author():
    author = Author("John Doe")
    article = Article(author, Magazine("Magazine 1", "Category 1"), "Article 1")
    assert article.author == author

def test_article_magazine():
    magazine = Magazine("Magazine 1", "Category 1")
    article = Article(Author("John Doe"), magazine, "Article 1")
    assert article.magazine == magazine
