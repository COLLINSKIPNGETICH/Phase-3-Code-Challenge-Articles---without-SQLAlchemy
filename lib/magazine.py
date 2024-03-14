

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        if not isinstance(category, str):
            raise TypeError("Category must be a string")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        return self._articles

    def contributors(self):
        authors = [article.author for article in self._articles]
        return list(set(authors))

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        author_counts = {author: sum(1 for article in self._articles if article.author == author) for author in self.contributors()}
        return [author for author, count in author_counts.items() if count > 2]
