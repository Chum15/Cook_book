from pprint import pprint
from collections import Counter

with open("recipes.txt", encoding='utf-8') as f:
    ST_TITLE = 1
    ST_COUNT = 2
    ST_INGREDIENTS = 3

    cook_book = {}
    state = ST_TITLE

    for line in f:
        line = line.strip()
        if not line: continue
        if state == ST_TITLE:
            title = line
            cook_book[title] = []
            state = ST_COUNT
        elif state == ST_COUNT:
            count = int(line)
            state = ST_INGREDIENTS
        elif state == ST_INGREDIENTS:
            data = [x.strip() for x in line.split('|')]
            data[1] = int(data[1])
            cook_book[title].append(dict(zip(('ingredient_name', 'quantity', 'measure'), data)))
            count -= 1
            if count == 0:
                state = ST_TITLE
    
pprint(cook_book)
def get_shop_list_by_dishes(dishes, person_count):
    counter = Counter(dishes)
    counter = dict(counter)
    print(counter)
    dish = {}
    for d in dishes:    
        dishes = cook_book[d]
            
        for di in dishes:
            for i in di:                
                dis = di['ingredient_name']
                dish[dis] = dict(list(di.items())[1:])
                key = dis 
                i = di['quantity']*person_count*int(counter[d])
                dish[key]['quantity'] = i

    return dish 
       
pprint(get_shop_list_by_dishes(['Омлет', 'Омлет','Утка по-пекински','Утка по-пекински','Омлет'], 2))