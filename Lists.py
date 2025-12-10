numbers = [5, 8, 12, 3, 15, 7, 10]

print("Initial list of numbers:", numbers)
numbers.append(20)
print("\nList after appending 20:", numbers)

numbers.insert(2, 100)  # Insert 100 at index 2
print("\nList after inserting 100 at index 2:", numbers)

more_numbers = [30, 25, 18]
numbers.extend(more_numbers)
print("\nList after extending with more numbers:", numbers)

numbers.remove(8)
print("\nList after removing 8:", numbers)

removed_item = numbers.pop(3) 
print("\nRemoved item:", removed_item)
print("List after popping the number at index 3:", numbers)

numbers.sort()
print("\nList after sorting in ascending order:", numbers)

numbers.reverse()
print("\nList after reversing:", numbers)

numbers.clear()
print("\nList after clearing all items:", numbers)

