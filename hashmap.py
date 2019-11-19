class Hashmap:
    def __init__(self, number_of_items):
        self.size = number_of_items * 2
        self.hashmap = [None] * self.size
        self.count = 0

    def hash(self, value):
        hashvalue = (value * 323) % self.size
        return hashvalue

    def add(self, value):
        if self.count != self.size:
            index = self.hash(value)
            if self.hashmap[index] == None:
                self.hashmap[index] = value
                self.count += 1
            else:
                if self.hashmap[index] != value:
                    index = (index + 1) % self.size
                    while (self.hashmap[index] != None):
                        index = (index + 1) % self.size
                    self.hashmap[index] = value
                    self.count += 1
        else:
            print("Cannot insert! Array full.")

    def printHash(self):
        print(self.hashmap)

    def find(self, value):
        ogindex = self.hash(value)
        index = ogindex
        if self.hashmap[index] == None:
            return False
        elif self.hashmap[index] == value:
            return True
        else:
            index = (index + 1) % self.size
            while (self.hashmap[index] != None and index != ogindex):
                if (self.hashmap[index] == value):
                    return True
                else:
                    index = (index + 1) % self.size
            return False

    def delete(self, value):
        index = self.hash(value)


hash = Hashmap(5)
hash.printHash()
hash.add(2)
hash.printHash()
hash.add(7)
hash.printHash()
hash.add(2)
hash.printHash()
hash.add(10)
hash.printHash()
hash.add(22)
hash.printHash()
hash.add(25)
hash.printHash()
hash.add(13)
hash.printHash()
hash.add(16)
hash.printHash()
hash.add(201)
hash.printHash()
hash.add(42)
hash.printHash()
hash.add(48)
hash.printHash()
hash.add(21)
hash.printHash()
print(hash.find(7))
print(hash.find(123))
