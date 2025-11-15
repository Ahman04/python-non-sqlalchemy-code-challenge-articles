import pytest
from classes.many_to_many import Article, Magazine, Author

class TestMagazine:
    """Magazine in many_to_many.py"""

    def test_name_is_mutable_string(self):
        """magazine name can change"""
        magazine_1 = Magazine("Vogue", "Fashion")

        magazine_1.name = "New Yorker"
        assert magazine_1.name == "New Yorker"

        with pytest.raises(Exception):
            magazine_1.name = "A"  # too short

        with pytest.raises(Exception):
            magazine_1.name = "New Yorker Plus X"  # too long

    def test_category_is_mutable_string(self):
        """magazine category can change"""
        magazine_1 = Magazine("Vogue", "Fashion")

        magazine_1.category = "Life Style"
        assert magazine_1.category == "Life Style"

        with pytest.raises(Exception):
            magazine_1.category = ""
        with pytest.raises(Exception):
            magazine_1.category = 2
