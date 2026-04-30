class HashTable:
    def __init__(self) -> None:
        self.collection = {}

    def hash(self, key: str) -> int:
        unicode_sum = 0
        for i in list(key.strip()):
            ind_unicode = ord(i)
            unicode_sum += ind_unicode
        return unicode_sum
    
    def add(self, key: str, value: str):
        key_hash = self.hash(key.strip())
        if key_hash not in self.collection:
            self.collection[key_hash] = {}
        self.collection[key_hash][key] = value

        

    def remove(self, key: str):
        key_hash = self.hash(key)
        if key_hash in self.collection:
            if key in self.collection[key_hash]:
                del self.collection[key_hash][key]
                if not self.collection[key_hash]:
                    del self.collection[key_hash]
        

    def lookup(self, key: str):
        key_hash = self.hash(key)
        if key_hash in self.collection:
            return self.collection[key_hash].get(key, None)
        return None
    

new_element = HashTable()
new_element.add('name', 'dishant')
print(new_element.lookup('name'))
