# lib/classes/many_to_many.py

class Author:
    all = []

    def __init__(self, name: str):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Author name must be a non-empty string")
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        mags = [article.magazine for article in self.articles()]
        return list(set(mags)) if mags else None

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        areas = [mag.category for mag in self.magazines()] if self.magazines() else None
        if areas:
            return list(set(areas))
        return None


class Magazine:
    all = []

    def __init__(self, name: str, category: str):
        self._name = None
        self._category = None
        self.name = name
        self.category = category
        Magazine.all.append(self)

    def _validate_name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Name must be string 2-16 characters")

    def _validate_category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Category must be non-empty string")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._validate_name(value)
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._validate_category(value)
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        authors = [article.author for article in self.articles()]
        return list(set(authors)) if authors else None

    def article_titles(self):
        arts = [article.title for article in self.articles()]
        return arts if arts else None

    def contributing_authors(self):
        contribs = [author for author in self.contributors() if len([a for a in self.articles() if a.author == author]) > 2]
        return contribs if contribs else None

    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        max_mag = max(cls.all, key=lambda m: len(m.articles()))
        return max_mag if max_mag.articles() else None


class Article:
    all = []

    def __init__(self, author: Author, magazine: Magazine, title: str):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string 5-50 characters")
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title

