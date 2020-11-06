class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class LinkedList:
    def _init_(self):
        self.head = None

    def find(self, key):
        # Start at the head
        curr = self.head
        # If curr has a value check:
        while curr != None:
            # If the curr = key then return key, youre done
            if curr.key == key:
                return curr
            # Otherwise, curr now moves to next node
            curr = curr.next
        return None

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def insert_head_or_overwrite_value(self, node):
        existingNode = self.find(node.key)
        if existingNode != None:
            existingNode.key = node.key
        else:
            self.insert_at_head(node)

    def delete(self, key):
        curr = self.head

        # if we need to delete head
        if curr.key == key:
            self.head = curr.next
            curr.next = None
            return curr
        prev = None

        while curr != None:
            if curr.key == key:
                prev.next == curr.next
                curr.next = None
                return curr
            else:
                prev = curr
                curr = curr.next
        return None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # # Your code here
        # self.capacity = MIN_CAPACITY
        # # starting with 8 empty slots
        # self.storage = [None] * 8
        # self.count = 0

        self.table = [None] * MIN_CAPACITY
        self.capacity = MIN_CAPACITY

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        # return self.capacity
        return len(self.table)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        offset_basis = 2020
        FNV_prime = 1777
        # Your code here
        key = key.encode()
        hash = offset_basis
        for byte in key:
            hash = hash * FNV_prime
            hash = hash ^ byte
    # ^ represents XOR compares 2 binary numbers if both bits are same XOR is 0
    # if both bits are different XOR is 1. In python XOR syntax is ^

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = ((hash * 33)) + ord(x)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.

        to add to head: 

        def insert_at_head(self, node):
            node.next = self.head
            self.head = node 

        ______________________________

        if you need to overwrite a node not in the head:
            def instert_or_owverwrite_value(self, key):
                node = self.find(key)

                if node is None:
                    (make new node)
                    self.insert_at_head(Node(key))
                else: 
                    (overwrite old key)
                    node.key = key
        """
        # Your code here
        newNode = HashTableEntry(key, value)
        i = self.hash_index(key)
        if not self.table[i]:  # why [] and not () here
            self.table[i] = LinkedList()
        self.table[i].insert_head_or_overwrite_value(newNode)

        if self.get_load_factor() > .7:
            self.resize(self.capacity * 2)

        # new_node = HashTableEntry(key, value)
        # # # Creating new node with key value pair
        # index = self.hash_index(key)
        # # # assigning the index as within the range of hash table
        # if self.storage[index] == None:
        #     self.storage[index] = new_node
        # # If there is nothing or room in storage, enter new node
        # elif self.storage[index].key == key:
        #     self.storage[index].value = value
        # If the index already equals the key, return the value

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # index = self.hash_index(key)

        # if self.storage[index].key == key:
        #     self.storage[index] = None

        # value = self.table[self.hash_index(key)]
        # if value == None:
        #     print("value is already None")
        # self.table[self.hash_index(key)] = None

        i = self.hash_index(key)
        linkedL = self.table[i]
        deleteNode = linkedL.delete(key)

        if self.get_load_factor() < .2:
            self.resize(self.capacity / 2)

        if not deleteNode:
            print(f"{key} not found")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        i = self.hash_index(key)
        linkedL = self.table[i]
        node = linkedL.find(key)

        return node.value if node else None

        # return self.table[self.hash_index(key)]

        # # If index is equal to key, display value
        # index = self.hash_index(key)

        # if self.storage[index] != None:
        #     if self.storage[index].key == key:
        #         return self.storage[index].value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # number of items / number of slots
        # resize if over .7 downsize if under .2
        newtable = HashTable(new_capacity if new_capacity >=
                             MIN_CAPACITY else MIN_CAPACITY)
        for slot in self.table:
            if slot:
                curr = slot.head
                while curr:
                    newtable.put(curr.key, curr.value)
                    curr = curr.next

        self.capacity = new_capacity
        self.table = newtable.table

    pass


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
