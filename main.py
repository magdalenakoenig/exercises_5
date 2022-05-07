# ex. 1
def power(a,b):
    if a > 0 and b > 0:
        return (a*power(a, b-1))
    elif b == 0:
        return 1
    else:
        return -1

# ex. 2
def binary_search(numbers, num, start, end):
    if start <= end:                                # checking if end value is greater than start value
        midpoint = start + (end - start) // 2       # calculating the midpoint of the list

        if numbers[midpoint] == num:                # checking if num is the midpoint of the list and if it is,
            return midpoint                         # returning the midpoint
        elif numbers[midpoint] < num:               # checking if num is greater than the midpoint and if it is,
            return binary_search(numbers, num, midpoint + 1, end)  # calling the function again but the start value is one greater than the midpoint value, meaning we will search the right (greater) half
        else:                                       # if num is smaller than the midpoint,
            return binary_search(numbers, num, start, midpoint - 1) # we will search the left (lower) half by setting the end value to one smaller than the midpoint
    else:
        return -1                                   # if the element can't be found, we return -1

numbers = [1,2,4,5,7]
num = 2

result = binary_search(numbers, num, 0, len(numbers)-1)  # setting the start value to 0 (because the index of the first number is 0) and the end value to one smaller than the number of elements in list
if result != -1:                                         # if the result is anything except -1, we get the position of the num
    print("Element was found in list at index", str(result))
else:
    print("Element was not found in list")               # if the result is -1, the element is not in the list


# ex. 3
class HashTable():
    def __init__(self, size):
        self.size = size
        self.data = [[] for _ in range(size)]

# ex. 4
    def __my_hash(self, element):
        if type(element) is str:
            result = len(element) % self.size
            return result
        if type(element) is int:
            result = element % self.size
            return result

# ex. 5
    def insert(self, element):
        key = self.__my_hash(element)
        self.data[key].append(element)

# ex. 6
    def get_element(self, element):
        key = self.__my_hash(element)
        if element in self.data[key]:
            self.data[key].remove(element)
            return element
        else:
            return -1

# ex. 7
    def get_size(self):
        self.size = len(self.data)
        return self.size

newhash = HashTable(10)
newhash.insert(15)
newhash.insert(2)
newhash.insert("hello")
newhash.insert("wow")





