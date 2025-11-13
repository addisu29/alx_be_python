# ask user for weather input

weather = ("what is the weather like today? (sunny/rainy/cold): ").lower()


# provide clothing recommendation 
if weather == "sunny":
    print("wear a t_shirt and sunglasses.")
elif weather == "rainny":
    print("don't forget umbrella and a raincoat.")
elif weather == "cold":
    print("make sure to wear a warm coat and a scarf.")
else:
    print("sorry, I don't have recommendations for this weather.")