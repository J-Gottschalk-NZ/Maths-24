import random


    
all_swag = "πβ¨πππ§Έππππ₯¨π¦π§π«π¬π©π­πͺπ§πΏπ£ππππ¦"
swag_list = []

for item in all_swag:
    swag_list.append(item)
    
for item in range(0, 5):
    get_swag = random.choice(swag_list)
    print(get_swag)
