from typing import List, Any

my_list = [1, 2, "Hello", [3, 4, 5]]

def append_to_list(li: List[Any], element: Any) -> None:
    """
    Appends an element to the provided list.

    Parameters:
    li (List[Any]): The list to which the element will be appended.
    element (Any): The element to append to the list.
    """
    li.append(element)

append_to_list(my_list, "CF")

for item in my_list:
    print(item, end=", ")  # Output each element of the list
print()