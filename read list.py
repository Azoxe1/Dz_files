with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        ingredient_name = i.strip()
        eng_count = int(file.readline())
        engrid = []
        for y in range(eng_count):
            which, howmuch, value = file.readline().strip().split(' | ')
            engrid.append({'ingredient_name': which,'quantity': howmuch,'measure': value})
        file.readline()
        cook_book[ingredient_name] = engrid    
        
def get_shop_list_by_dishes(dishes, person_count):
    shop_list= {}
    for dish in dishes:
        for ingredients in cook_book[dish]:  
            ingr = ingredients['ingredient_name']
            ingr_much = (int(ingredients['quantity'])*person_count)
            if ingr not in shop_list.keys():
                shop_list[ingr] = {'quantity': ingr_much,'measure': ingredients['measure']}
            else:
                wh = shop_list[ingr]
                more_ingr = (int(wh['quantity']) + ingr_much)
                shop_list[ingr] = {'quantity': more_ingr,'measure': ingredients['measure']}
    return shop_list   
            
            
get_shop_list_by_dishes(['Омлет', 'Фахитос'], )
