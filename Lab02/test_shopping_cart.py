import unittest
from shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        """Tworzenie nowego koszyka przed każdym testem"""
        self.cart = ShoppingCart()

    def test_add_item(self):
        """Test dodawania produktów do koszyka"""
        self.cart.add_item("jabłko", 2)
        self.assertEqual(self.cart.items["jabłko"], 2)

    def test_add_existing_item(self):
        """Test dodawania produktu, który już jest w koszyku"""
        self.cart.add_item("banan", 1)
        self.cart.add_item("banan", 2)
        self.assertEqual(self.cart.items["banan"], 3)

    def test_remove_item(self):
        """Test usuwania produktu z koszyka"""
        self.cart.add_item("gruszka", 3)
        self.cart.remove_item("gruszka", 2)
        self.assertEqual(self.cart.items["gruszka"], 1)

    def test_remove_item_completely(self):
        """Test całkowitego usunięcia produktu z koszyka"""
        self.cart.add_item("truskawka", 3)
        self.cart.remove_item("truskawka", 3)
        self.assertNotIn("truskawka", self.cart.items)

    def test_remove_item_not_in_cart(self):
        """Test usuwania produktu, którego nie ma w koszyku"""
        with self.assertRaises(KeyError):
            self.cart.remove_item("czekolada", 1)

    def test_total_items(self):
        """Test liczenia ilości produktów w koszyku"""
        self.cart.add_item("chleb", 2)
        self.cart.add_item("mleko", 1)
        self.assertEqual(self.cart.total_items(), 3)

    def test_is_empty(self):
        """Test sprawdzania, czy koszyk jest pusty"""
        self.assertTrue(self.cart.is_empty())
        self.cart.add_item("ser", 1)
        self.assertFalse(self.cart.is_empty())

    def test_clear_cart(self):
        """Test czyszczenia koszyka"""
        self.cart.add_item("masło", 2)
        self.cart.clear_cart()
        self.assertTrue(self.cart.is_empty())

    def tearDown(self):
        """Czyszczenie zasobów po teście"""
        self.cart = None

if __name__ == "__main__":
    unittest.main()