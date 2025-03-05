# numbers
type_int = 20
type_float = 20.5
type_complex = 1j

# boolean
type_bool_true = True
type_bool_false = False

# text
type_string = "Hello, World!"

# sequences
type_list = ["apple", "banana", "cherry"]
type_tuple = ("apple", "banana", "cherry")
type_range = range(6)

# mappings
type_dict = {"name": "John", "age": 36}

# sets
type_set = {"apple", "banana", "cherry"}
type_frozenset = frozenset({"apple", "banana", "cherry"})

# binary
type_bytes = b"Hello"
type_bytearray = bytearray(5)
type_memoryview = memoryview(bytes(5))

# type operations

# type casting
cast_int = int("1")
cast_float = float(1)
cast_str = str(1)
cast_bool = bool(1) # true for 1 or "True"
cast_bool = bool("False") # false for 0 or "False"

# type checking
check_type = type(1) # <class 'int'>
check_int = isinstance(1, int) # True
check_float = isinstance(1.0, float) # True
check_str = isinstance("1", str) # True
