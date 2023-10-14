class Vector1:
    # Constructor method, called when an instance is created
    def __init__(self, x, y):
        self.x = x
        self.y = y
        value = f"Vector1: {x + y}"
        return print(value)

v1 = Vector1(22,21)

class Vector2:
    def __init__(self, value):
        self.value = value
    # String representation, called by str() and print()
    def __str__(self):
        return f"Vector2: Value is {self.value}"

v2 = Vector2(5)
print(v2)


class Vector3:
    def __init__(self, x, y, z, t, bool):
        self.x = x
        self.y = y
        self.z = z
        self.t = t
        self.bool = bool

    # Length, called by len()
    def __len__(self):
        if self.bool:
            combined = f"{self.x}{self.y}{self.z},{self.t}"  # combine and convert to string
        else:
            combined = str(self.x + self.y + self.z + self.t)  # sum the values and convert to string
        return len(combined)  # compute and return the length of the string

v3 = Vector3(6, 7, 9, 10, True)  # Don't forget to pass the fifth argument
print(f"Vector3: len = {len(v3)}")  # Output: len: 6

class Vector4:
    def __init__(self, value):
        self.value = value
    # Addition, called by +
    def __add__(self, other):
        combined_value = self.value + other.value
        return f"Vector4: {combined_value}"

v4 = Vector4(5)
ve4 = Vector4(6)

print(v4 + ve4)  # Output: Vector4(11)

class Vector5:

    def __init__(self, value):
        self.value = value
    # Equality, called by ==
    def __eq__(self, other):
        newValue = self.value == other.value
        return newValue

v5 = Vector5(1)
ve5 = Vector5(2)

print(f"Vector5: {v5 == ve5}")

class Vector6:

    def __init__(self, value):
        self.value = value
    # Called by repr(); meant for debugging and development
    def __repr__(self):
        return f"Vector6: {self.value}"

v6 = Vector6(8)

print(v6)

class Vector7:

    def __init__(self, value):
        self.value = value
        # Called by <
    def __lt__(self, other):
        return self.value < other.value

        # Called by >
    def __gt__(self, other):
        return self.value > other.value

        # Called by <=
    def __le__(self, other):
        return self.value <= other.value

        # Called by >=
    def __ge__(self, other):
        return self.value >= other.value

        # Called by !=
    def __ne__(self, other):
        return self.value != other.value

v7 = Vector7(5)
ve7 = Vector7(9)

print(f"Vector7: lt = {v7 < ve7} gt = {v7 > ve7} le = {v7 <= ve7} ge = {v7 >= ve7} ne = {v7 != ve7}")

class Vector8:

    # Called by repr(); meant for debugging and development
    def __repr__(self):
        return f"Vector8: Object: {self.__dict__}"

    # Called when an attribute is accessed
    def __getattr__(self, name):
        return f"Vector8: {name} attribute does not exist"

    # Called when an attribute is set
    def __setattr__(self, name, value):
        self.__dict__[name] = value

    # Called when an attribute is deleted
    def __delattr__(self, name):
        if name in self.__dict__:
            del self.__dict__[name]
        else:
            print(f"Vector8: No such attribute: {name} to delete")

v8 = Vector8()
v8.x = 5
v8.y = 3
print(repr(v8))
del v8.z , v8.x
print(repr(v8))

class Vector9:

    # Called by iter(); returns an iterator
    def __iter__(self):
        self.index = 0
        return self


    # Called by next(); defines next item in the iteration
    def __next__(self):
        self.index += 1
        if self.index <= 5:
            return self.index
        raise StopIteration

    # Called by hash(); returns a hash value
    def __hash__(self):
        return hash(self.value)

    # Called by bool(); returns True or False
    def __bool__(self):
        return bool(self.value)

    # Called by call(); allows the instance to be called as a function
    def __call__(self, new_value):
        self.value = new_value

v9 = Vector9()
v9.value = 9

for i in v9:
    print(i)

print(hash(v9))
print(bool(v9))
v9(20)
print(v9.value)

