# Prompt user for current weather condition
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Provide clothing recommendations based on the input
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget yout umbrella and a raincoat.")
elif weather == "cold": 
    print("Make sure to wear a warm coat and a scraf.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
