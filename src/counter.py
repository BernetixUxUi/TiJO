class Operation:
    def count(self, text):
        pass  # Brak implementacji

class Counter:
    def __init__(self, operation):
        self.operation = operation

    def count_characters(self, text):
        return self.operation.count(text)