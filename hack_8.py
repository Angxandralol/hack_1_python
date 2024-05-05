"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
    result = [1,3,5,7,9]
    for number in result:
        if number != 3 and number != 5 and number != 7: result.remove(number)
    return result  