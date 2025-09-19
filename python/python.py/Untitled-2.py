class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]  # Use list for chaining

    def hash_function(self, key):
        sum = 0
        for char in key:
            sum += ord(char)
        index = sum % self.size
        return index

    def insert(self, name, phone):
        index = self.hash_function(name)
        # Check if name already exists and update
        for i, (n, _) in enumerate(self.table[index]):
            if n == name:
                self.table[index][i] = (name, phone)
                return
        self.table[index].append((name, phone))

    def display(self):
        print("\nTelephone Book:")
        for i in range(len(self.table)):
            if not self.table[i]:
                print(f"Index {i}: Empty")
            else:
                print(f"Index {i}:", self.table[i])

    def search(self, name):
        index = self.hash_function(name)
        for n, phone in self.table[index]:
            if n == name:
                print(f"Phone number of {name}: {phone}")
                return
        print(f"\n{name} not found in telephone book.")

ht = HashTable()
ht.insert("ABCD", "1234567890")
ht.insert("DCBA", "9876543210")
ht.insert("kakde", "5656565656")
ht.insert("Shweeta", "8888888888")
ht.insert("DAC", "1111111111")

ht.display()
ht.search("kakde")
ht.search("Unknown")