#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    - boxes (list of lists): Represents a list of boxes where each box is a list of keys.

    Returns:
    - bool: Returns True if all boxes can be opened, else returns False.
    """

    if not boxes or len(boxes) == 0:
        return False
    
    keys = set()
    keys.update(boxes[0])  
    
    opened = {0} 
    to_open = [0]  
    while to_open:
        box = to_open.pop()
        opened.add(box)
        for key in boxes[box]:
            keys.add(key)
            if key < len(boxes) and key not in opened:
                to_open.append(key)
    
    return len(opened) == len(boxes)
