"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    for element in result:
        if element != '@': 
            index = result.index(element)
            result.insert(index + 1, '@')
    return result  