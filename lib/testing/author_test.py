import pytest
from classes.many_to_many import Article, Magazine, Author

class TestAuthor:
    """Author in many_to_many.py"""

    def test_has_name(self):
        """Author is initialized with a name"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")

        assert author_1.name == "Carry Bradshaw"
        assert author_2.name == "Nathaniel Hawthorne"

    def test_name_is_immutable_string(self):
        """author name is of type str and cannot change"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")

        assert isinstance(author_1.name, str)
        assert isinstance(author_2.name, str)

        with pytest.raises(AttributeError):
            author_1.name = "ActuallyTopher"

        with pytest.raises(AttributeError):
            author_2.name = 2

        # invalid initialization
        with pytest.raises(Exception):
            Author(2)

    def test_name_len(self):
        """author name is longer than 0 characters"""
        with pytest.raises(Exception):
            Author("")

    def test_has_many_articles(self):
        """author has many articles"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author_1, magazine, "How to wear a tutu with style")
        article_2 = Article(author_1, magazine, "Dating life in NYC")
        article_3 = Article(author_2, magazine, "How to be single and happy")

        assert len(author_1.articles()) == 2
        assert len(author_2.articles()) == 1
        assert article_1 in author_1.articles()
        assert article_2 in author_1.articles()
        assert article_3 not in author_1.articles()
        assert article_3 in author_2.articles()
