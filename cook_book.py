from pprint import pprint

ST_TITLE = 1
ST_COUNT = 2
ST_INGREDIENTS = 3

cook_book = {}
state = ST_TITLE
with open("recipes.txt", encoding='utf-8') as f:
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
    #print(f.readlines())
pprint(cook_book)
def get_shop_list_by_dishes(dishes, person_count):

    dish = {}
    for d in dishes:
        dishes = cook_book[d]
        for ing in dishes:
            for i in ing:
                i = ing['quantity']*person_count  
            dis = ing['ingredient_name']
            dish[dis] = dict(list(ing.items())[1:])
            key = dis   
            dish[key]['quantity'] = i
    return dish
       
pprint(get_shop_list_by_dishes(['Фахитос'], 3))