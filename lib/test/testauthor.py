# author_test.py
from author import Author
from article import Article
from magazine import Magazine

def test_author_name():
    author = Author("John Doe")
    assert author.name == "John Doe"

def test_author_articles():
    author = Author("John Doe")
    article1 = author.add_article(Magazine("Magazine 1", "Category 1"), "Article 1")
    article2 = author.add_article(Magazine("Magazine 2", "Category 2"), "Article 2")
    assert author.articles() == [article1, article2]

def test_author_magazines():
    author = Author("John Doe")
    author.add_article(Magazine("Magazine 1", "Category 1"), "Article 1")
    author.add_article(Magazine("Magazine 2", "Category 2"), "Article 2")
    assert author.magazines() == ["Category 1", "Category 2"]

def test_author_add_article():
    author = Author("John Doe")
    article = author.add_article(Magazine("Magazine 1", "Category 1"), "Article 1")
    assert article.author == author

def test_author_topic_areas():
    author = Author("John Doe")
    author.add_article(Magazine("Magazine 1", "Category 1"), "Article 1")
    author.add_article(Magazine("Magazine 2", "Category 2"), "Article 2")
    assert author.topic_areas() == ["Category 1", "Category 2"]
