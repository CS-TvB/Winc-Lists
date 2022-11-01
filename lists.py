# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
from logging import StringTemplateStyle
from operator import contains
from os import remove

def alphabetical_order (x):
    strings = x
    #print (sorted(strings))
    return (sorted(strings))

def won_golden_globe(y):
    result_y = ''
    for i in range(0,len(y)):
        result_y += y[i].lower()
    #print(result_y)
    awards_won = 'Jaws' 'Star Wars: Episode IV – A New Hope' 'E.T. the Extra-Terrestrial' 'Memoirs of a Geisha'
    lower_awards_won = (awards_won.lower())
    if result_y in lower_awards_won:
        #print('i found one!')
        return True
    else:
        return False

def remove_toto_albums(u):
    toto_albums = ['Fahrenheit', 'The Seventh One', 'Toto XX', 'Falling in Between', 'Toto XIV', 'Old Is New']
    newlist = []
    for i in u:
        if i  not in toto_albums:
            newlist.append(i)
    else:
        print (newlist)
        return (newlist)

u = ['Old Is New']
x = ['a', 'c', 'b', 'e', 'd']
y = 'JAWS'
alphabetical_order (x)
won_golden_globe(y)
remove_toto_albums(u)
