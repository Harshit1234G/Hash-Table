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
