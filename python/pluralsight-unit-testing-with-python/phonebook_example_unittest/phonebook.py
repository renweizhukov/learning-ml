
class Phonebook:
    
    def __init__(self):
        self.entries = {}
    
    def add(self, name, number):
        self.entries[name] = number
        
    def lookup(self, name):
        return self.entries[name]
        
    def is_consistent(self):
        if len(self.entries) < 2:
            return True
        
        numbers = self.entries.values()
        sorted_numbers = sorted(numbers)
        
        for curr, next in zip(sorted_numbers, sorted_numbers[1:]):
            if next.startswith(curr):
                return False
        
        return True
