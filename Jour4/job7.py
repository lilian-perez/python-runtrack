def food(type, saison):
    if type == 'fruits' and saison == 'hiver':
        return 'orange, mandarine et kiwi'
    elif type == 'fruits' and saison == 'été':
        return 'poire, fraise et cassis'
    elif type == 'légumes' and saison == 'hiver':
        return 'carotte, topinambour et endive'
    elif type == 'légumes' and saison == 'été':
        return 'artichaut, aubergine et navet'
    else:
        return False
    
print(food('fruits', 'hiver'))