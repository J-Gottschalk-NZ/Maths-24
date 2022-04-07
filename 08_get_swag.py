import random


    
all_swag = "🎈✨👓🏆🧸🍕🍔🍟🥨🍦🧁🍫🍬🍩🍭🍪🍧🍿🍣🍀🍒🌈🦋"
swag_list = []

for item in all_swag:
    swag_list.append(item)
    
for item in range(0, 5):
    get_swag = random.choice(swag_list)
    print(get_swag)
