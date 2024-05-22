def get_hash(key):
    h = 0
    for char in key:
        #Ord finds the ascii character translation
        h += ord(char)
    return h % 100

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h%self.MAX
    
    #now lets implement a funcion that can add an item into a hashmap and get an item from the hashmap


if __name__ == "__main__":
    t = HashTable()
    t.get_hash("march 6")
    print(t)