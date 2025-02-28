class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity=1):
        """Dodaje produkt do koszyka. Jeśli już istnieje, zwiększa ilość."""
        if quantity <= 0:
            raise ValueError("Ilość musi być większa od zera")
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity=1):
        """Usuwa określoną ilość produktu z koszyka lub całkowicie go usuwa."""
        if item_name not in self.items:
            raise KeyError("Produkt nie znajduje się w koszyku")
        if quantity <= 0:
            raise ValueError("Ilość musi być większa od zera")
        if self.items[item_name] <= quantity:
            del self.items[item_name]
        else:
            self.items[item_name] -= quantity

    def total_items(self):
        """Zwraca łączną ilość wszystkich produktów w koszyku."""
        return sum(self.items.values())

    def is_empty(self):
        """Zwraca True, jeśli koszyk jest pusty, w przeciwnym razie False."""
        return len(self.items) == 0

    def clear_cart(self):
        """Czyści cały koszyk."""
        self.items.clear()