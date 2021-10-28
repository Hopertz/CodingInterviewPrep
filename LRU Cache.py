"""
     LRU Cache ☆
   Implement an LRUCache class for a Least Recently Used (LRU) cache. The class should support:
   • Inserting key-value pairs with the insertKeyValuePair method.
   • Retrieving a key's value with the getValueFromkey method.
   • Retrieving the most recently used (the most recently inserted or retrieved) key with the getMost RecentKey method.
   Each of these methods should run in constant time.
   Additionally, the LRUCache class should store a maxSize property set to the size of the cache, which is passed in as an argument
   during instantiation. This size represents the maximum number of key-value pairs that the cache can store at once. If a key-value pair is
   inserted in the cache when it has reached maximum capacity, the least recently used key-value pair should be evicted from the cache
   and no longer retrievable; the newly added key-value pair should effectively replace it.
   Note that inserting a key-value pair with an already existing key should simply replace the key's value in the cache with the new value
   and shouldn't evict a key-value pair if the cache is full. Lastly, attempting to retrieve a value from a key that isn't in the cache should
   return None / null.

       Sample Usage
   // All operations below are performed sequentially.
   LRUCache(3): - // instantiate an LRUCache of size 3
   insertKeyValuePair("b", 2): -
   insertKeyValuePair("a", 1):
   insertKeyValuePair("c", 3):
   getMostRecentKey(): "c" // "c" was the most recently inserted key
   getValueFromkey("a"): 1
   getMostRecentKey(): "a" // "a" was the most recently retrieved key
   insertKeyValuePair("d", 4): // the cache had 3 entries; the least recently used one is evicted
   getValue Fromkey("b"): None // "b" was evicted in the previous operation
   insertKeyValuePair("a", 5): // "a" already exists in the cache so its value just gets replaced
   getValue Fromkey("a"): 5
 

"""


# SOLUTION 1

# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
class LRUCache:
    def __init__(self, maxSize):
        self.cache = {}
        self.maxSize = maxSize or i
        self.currentSize = 0
        self.listOfMostRecent = DoublyLinkedList()

    # 0(1) time | 0(1) space
    def insertKeyValuePair(self, key, value):
        if key not in self.cache:
            if self.currentSize == self.maxSize:
                self.evictLeastRecent()
            else:
                self.currentSize += 1
            self.cache[key] = DoublyLinkedlistNode(key, value)
        else:
            self.replaceKey(key, value)
        self.updateMostRecent(self.cache[key])

    # 0(1) time | 0(1) space
    def getValueFromKey(self, key):
        if key not in self.cache:
            return None
        self.updateMostRecent(self.cache[key])
        return self.cache[key].value

    # 0(1) time | 0(1) space
    def getMostRecentKey(self):
        if self.listOfMostRecent.head is None:
            return None
        return self.listOfMostRecent.head.key

    def evictLeastRecent(self):
        keyToRemove = self.listOfMostRecent.tail.key
        self.listOfMostRecent.removeTail()
        del self.cache[keyToRemove]

    def updateMostRecent(self, node):
        self.listOfMostRecent.setHeadTo(node)

    def replaceKey(self, key, value):
        if key not in self.cache:
            raise Exception("The provided key isn't in the cache!")
        self.cache[key].value = value


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHeadTo(self, node):
        if self.head == node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.removeTail()
            node.removeBindings()
            self.head.prev = node
            node.next = self.head
            self.head = node

    def removeTail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None


class DoublyLinkedlistNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def removeBindings(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None
