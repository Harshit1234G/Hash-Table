from typing import Hashable, NoReturn, Iterator, Self


# Type Annotations
type Key = Hashable
type Value = object | any
type KeyValuePair = tuple[Key, Value]


# Main Hash Table Class
class HashTable:
    """
    # Hash Table
    My implementation of Hash Table in python. It is a smaller version of python dictionary, including most of its functionalities.

    ## Attributes:
    - `MAX_HASH_TABLE_SIZE` (int): It represents the maximum size of hash table. Inserting after this limit will throw OverflowError.
    - `data_list` (list of KeyValuePair or None): Stores all the key value pairs.

    ## Functions:
    Look over the respective function docstrings for detailed description about them.
    - `get_index()`: Creates a hash value and determines the index at which the key should be placed in the data_list. Also implemented linear probing for minimal collision.
    - `items()`: Returns a generator of all the key value pairs.
    - `keys()`: Returns a generator of all the keys.
    - `values()`: Returns a generator of all the values.
    - `clear()`: Removes all key value pairs from the hash table.
    - `update()`: Updates a given key value pair.
    - `get()`: Return the value of given key, if key not exists then return None.
    - `to_pydict()`: Returns the hash table as a python dictionary.
    - `__setitem__()`: Item assignment.
    - `__getitem__()`: Getting a value from key, raises error if key doesn't exists.
    - `__contains__()`: For checking membership, i.e. that a key exists or not.
    - `__delitem__()`: For deleting key value pair using del keyword.
    - `__eq__()`: For checking equality of two hash tables.
    - `__iter__()`: For iteration.
    - `__len__()`: Returns the number of key value pairs in hash table.
    - `__str__()`: Returns the hash table as a dictionary like format in a string.

    ## Usage: 
    ```
    hash_table = HashTable(size= 10)
    ```

    ## Example:
    ```
    ht = HashTable(size=10)     # instantiation
    ht['hello'] = 5             # item assignment
    del ht['hello']             # item deletion
    for i in ht:                # iteration
        print(i)
    ```

    ## Note:
    - Errors might be raised when unhashable key is provided or insertion after max size is reached. Handle them if necessary.
    """
    def __init__(self, size: int) -> None:
        self.MAX_HASH_TABLE_SIZE: int = size
        self.data_list: list[KeyValuePair | None] = [None] * self.MAX_HASH_TABLE_SIZE

    def get_index(self, key: Key) -> int | None | NoReturn:
        """
        Most used function throughout this class, generate the hash value of key. Then this hash value is divided by the `MAX_HASH_TABLE_SIZE` and the remainder is used as index to insert the key.

        ## Parameters:
        - `key` (Hashable object): The key to represent the value, the value would be found from this key.

        ## Returns:
        - int: index of the key in data_list.

        ## Possible Errors:
        - `TypeError`: Thrown if unhashable object is passed in key.
        - `OverflowError`: Thrown if max size is reached.
        """
        # remainder of hash value by max size is index.
        index = hash(key) % self.MAX_HASH_TABLE_SIZE
        i = 0

        # Linear Probing
        while i <= len(self.data_list):
            kv = self.data_list[index]
            # if the index doesn't contain any key value pair
            if kv is None:
                return index
            # if the key(kv) at index is equal to key(passed to the function)
            if kv[0] == key:
                return index

            index += 1
            # if index reaches the end
            if index == len(self.data_list):
                index = 0

            i += 1
        # if value of i == length of data_list, means the hash table is full
        raise OverflowError(f'HashTable exceeded its max size, {self.MAX_HASH_TABLE_SIZE = }')

    def items(self) -> Iterator[KeyValuePair]:
        """
        Returns the generator of all key value pairs.
        """
        return (kv for kv in self.data_list if kv)

    def keys(self) -> Iterator[Key]:
        """
        Returns the generator of all keys.
        """
        return (k[0] for k in self.data_list if k)

    def values(self) -> Iterator[Value]:
        """
        Returns the generator of all values.
        """
        return (v[1] for v in self.data_list if v)

    def clear(self) -> None:
        """
        Removes all the values from hash table.
        """
        self.data_list = [None] * self.MAX_HASH_TABLE_SIZE

    def update(self, key: Key, update_value: Value) -> None:
        """
        Updates the key value pair provided by simple item assignment.
        
        ## Parameters:
        - `key` (Hashable object): Key whose value to update.
        - `update_value` (any): Value to update.
        """
        self[key] = update_value

    def to_pydict(self) -> dict[Key, Value]:
        return dict(self.items())

    def __setitem__(self, key: Key, value: Value) -> None | NoReturn:
        index = self.get_index(key)
        self.data_list[index] = (key, value)

    def __getitem__(self, key: Key) -> Value | NoReturn:
        try:
            index = self.get_index(key)
            return self.data_list[index][1]

        except TypeError:
            raise KeyError(f'{key=} is not present.')

    def get(self, key: Key) -> Value | None:
        try:
            return self[key]

        except KeyError:
            return None

    def __contains__(self, key: Key) -> bool:
        index = self.get_index(key)
        if self.data_list[index] is None:
            return False

        return True

    def __delitem__(self, key: Key) -> None:
        index = self.get_index(key)
        self.data_list[index] = None

    def __eq__(self, other: Self) -> bool:
        return list(self.items()) == list(other.items())

    def __iter__(self) -> Iterator[KeyValuePair]:
        return self.items()

    def __len__(self) -> int:
        length = 0
        for i in self.data_list:
            if i:
                length += 1

        return length

    def __str__(self) -> str:
        return '{\n\t' + "\n\t".join(f"{key}: {value}," for key, value in self.items()) + '\n}'


if __name__ == '__main__':
    ht = HashTable(size=10)
    ht['hello'] = 5
    ht['h'] = 7
    print(ht)

    ht['h'] = [1, 2, 3]
    ht[1, 3, 4] = 2
    del ht['hello']
    print(ht)

    print(ht.items(), ht.keys(), ht.values())  # generators
    for i in ht:
        print(i)
    print(list(ht.values()))

    # print(ht['hwe'])   #throws key error
    # print(ht[1:3])       #throws key error
    print(ht.get('hwe'))  # returns None
    print('h' in ht, 'a' in ht)

    h1 = HashTable(size=1)
    h2 = HashTable(size=5)

    h1[1] = 'Hello'
    # h1[2] = 'Hell'    #throws OverFlowError
    h2[1] = 'Hello'

    print(h1 == h2, h1 == ht)
    print(len(ht))
    h1.update(1, 'Harshit')
    print(h1)
    h2.clear()
    print(h2)
    print(ht.to_pydict())