# magazine_test.py
from magazine import Magazine
from article import Article
from author import Author

def test_magazine_name():
    magazine = Magazine("Magazine 1", "Category 1")
    assert magazine.name == "Magazine 1"

def test_magazine_category():
    magazine = Magazine("Magazine 1", "Category 1")
    assert magazine.category == "Category 1"

def test_magazine_articles():
    magazine = Magazine("Magazine 1", "Category 1")
    article1 = Article(Author("John Doe"), magazine, "Article 1")
    article2 = Article(Author("Jane Doe"), magazine, "Article 2")
    magazine._articles = [article1, article2]
    assert magazine.articles() == [article1, article2]

def test_magazine_contributors():
    magazine = Magazine("Magazine 1", "Category 1")
    author1 = Author("John Doe")
    author2 = Author("Jane Doe")
    article1 = Article(author1, magazine, "Article 1")
    article2 = Article(author2, magazine, "Article 2")
    magazine._articles = [article1, article2]
    assert magazine.contributors() == [author1, author2]

def test_magazine_article_titles():
    magazine = Magazine("Magazine 1", "Category 1")
    article1 = Article(Author("John Doe"), magazine, "Article 1")
    article2 = Article(Author("Jane Doe"), magazine, "Article 2")
    magazine._articles = [article1, article2]
    assert magazine.article_titles() == ["Article 1", "Article 2"]

def test_magazine_contributing_authors():
    magazine = Magazine("Magazine 1", "Category 1")
    author1 = Author("John Doe")
    author2 = Author("Jane Doe")
    article1 = Article(author1, magazine, "Article 1")
    article2 = Article(author1, magazine, "Article 2")
    article3 = Article(author2, magazine, "Article 3")
    magazine._articles = [article1, article2, article3]
    assert magazine.contributing_authors() == [author1]
