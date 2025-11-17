class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        # store articles written by this author
        # we don't need an Author.all list
    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        mags = [article.magazine for article in self.articles()]
        # unique list
        return list(set(mags))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if len(self.articles()) == 0:
            return None
        categories = [article.magazine.category for article in self.articles()]
        return list(set(categories))


class Magazine:
    all = []

    def __init__(self, name, category):
        # name validation
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            self._name = name if isinstance(name, str) else None

        # category validation
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            self._category = category if isinstance(category, str) else None

        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name
        # if invalid, ignore

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_cat):
        if isinstance(new_cat, str) and len(new_cat) > 0:
            self._category = new_cat
        # invalid ignored

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        authors = [article.author for article in self.articles()]
        return list(set(authors))

    def article_titles(self):
        if len(self.articles()) == 0:
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        if len(self.articles()) == 0:
            return None

        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1

        result = [author for author, count in author_counts.items() if count > 2]

        return result if len(result) > 0 else None

    @classmethod
    def top_publisher(cls):
        if len(Article.all) == 0:
            return None

        return max(cls.all, key=lambda magazine: len(magazine.articles()))


class Article:
    all = []

    def __init__(self, author, magazine, title):
        # validate title
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title

        # author must be Author
        if isinstance(author, Author):
            self._author = author

        # magazine must be Magazine
        if isinstance(magazine, Magazine):
            self._magazine = magazine

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_mag):
        if isinstance(new_mag, Magazine):
            self._magazine = new_mag
