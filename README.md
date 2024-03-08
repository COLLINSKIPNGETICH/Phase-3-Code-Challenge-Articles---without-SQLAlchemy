# a Phase-3-Code-Challenge-Articles---without-SQLAlchemy

# Magazine Domain Project

This project implements a simple Magazine domain with three models: Author, Article, and Magazine.

## Classes and Methods

### Author

- ****init**(self, name):** Initializes an Author with a name.
- **name:** Property to get the author's name.
- **articles():** Returns a list of all articles the author has written.
- **magazines():** Returns a unique list of magazines the author has contributed to.
- **add_article(magazine, title):** Adds a new article associated with the author and returns the article instance.
- **topic_areas():** Returns a unique list of strings with the categories of the magazines the author has contributed to.

### Magazine

- ****init**(self, name, category):** Initializes a Magazine with a name and category.
- **name:** Property to get the magazine's name.
- **category:** Property to get the magazine's category.
- **articles():** Returns a list of all articles the magazine has published.
- **contributors():** Returns a unique list of authors who have written for this magazine.
- **add_article(author, title):** Adds a new article associated with the magazine and returns the article instance.
- **article_titles():** Returns a list of the title strings of all articles written for that magazine.
- **contributing_authors():** Returns a list of authors who have written more than 2 articles for the magazine.

### Article

- ****init**(self, author, magazine, title):** Initializes an Article with an Author instance, a Magazine instance, and a title.
- **title:** Property to get the article's title.
- **author:** Property to get the author object for that article.
- **magazine:** Property to get the magazine object for that article.
