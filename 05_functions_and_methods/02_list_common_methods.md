## List Common Methods

In Python, lists are a versatile data structure that allows you to store and manipulate collections of items. There are several commonly used and important methods that you can use to work with lists effectively. Here are some of the most useful list methods:

- `append(item)`: This method adds an item to the end of the list. For example:
    ```python
    my_list = [1, 2, 3]
    my_list.append(4)
    print(my_list)  # Output: [1, 2, 3, 4]
    ```

- `extend(iterable)`: This method extends the list by appending all items from the iterable. For example:
    ```python
    my_list = [1, 2, 3]
    my_list.extend([4, 5, 6])
    print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
    ```

- `insert(index, item)`: This method inserts an item at a specified position in the list. For example:
    ```python
    my_list = [1, 2, 3]
    my_list.insert(1, 4)
    print(my_list)  # Output: [1, 4, 2, 3]
    ```

- `remove(item)`: This method removes the **first** occurrence of the specified item from the list. For example:
    ```python
    my_list = [1, 2, "cat", 2]
    my_list.remove(2)
    print(my_list)  # Output: [1, "cat", 2]
    ```

- `pop(index)`: This method removes and returns the item at the specified position in the list. For example:
    ```python
    my_list = [1, 2, 3]
    popped_item = my_list.pop(1)
    print(my_list)  # Output: [1, 3]
    print(popped_item)  # Output: 2
    ```

- `index(item)`: This method returns the index of **the first occurrence** of the specified item in the list. For example:
    ```python
    my_list = [1, 2, 3, 2]
    index = my_list.index(2)
    print(index)  # Output: 1
    ```

- `count(item)`: This method returns the number of occurrences of the specified item in the list. For example:
    ```python
    my_list = [1, 2, 3, 2]
    count = my_list.count(2)
    print(count)  # Output: 2
    ```

- `sort()`: This method sorts the list in ascending order. For example:
    ```python
    my_list = [3, 1, 2]
    my_list.sort()
    print(my_list)  # Output: [1, 2, 3]
    ```

- `reverse()`: This method reverses the order of the items in the list. For example:
    ```python
    my_list = [1, 2, 3]
    my_list.reverse()
    print(my_list)  # Output: [3, 2, 1]
    ```

[more list methods](https://www.w3schools.com/python/python_lists_methods.asp)

[some quick quizzes on lists](https://www.w3schools.com/python/python_lists_exercises.asp)