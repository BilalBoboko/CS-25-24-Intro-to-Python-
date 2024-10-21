city_n = {
    '1': {
        'district_name': 'District A',
        'restaurants': [
            {
                'restaurant_name': 'Budget Restaurant A1',
                'price_category': 'budget',
                'menu': {
                    'Caesar Salad': 250,
                    'Margherita Pizza': 450
                }
            },
            {
                'restaurant_name': 'Mid-range Restaurant A2',
                'price_category': 'mid-range',
                'menu': {
                    'Tom Yum Soup': 350,
                    'Philadelphia Rolls': 550
                }
            }
        ]
    },
    '2': {
        'district_name': 'District B',
        'restaurants': [
            {
                'restaurant_name': 'Premium Restaurant B1',
                'price_category': 'premium',
                'menu': {
                    'Ribeye Steak': 1200,
                    'Grilled Octopus': 1500
                }
            }
        ]
    },
    '3': {
        'district_name': 'District C',
        'restaurants': [
            {
                'restaurant_name': 'Budget Restaurant C1',
                'price_category': 'budget',
                'menu': {
                    'Carbonara Pasta': 300,
                    'Four Cheese Pizza': 400
                }
            },
            {
                'restaurant_name': 'Premium Restaurant C2',
                'price_category': 'premium',
                'menu': {
                    'Tuna Tartare': 1400,
                    'Oysters': 1800
                }
            }
        ]
    }
}

price_categories = {
    '1': 'budget',
    '2': 'mid-range',
    '3': 'premium'
}

def display_districts():
    print("Districts: ")
    for key, district in city_n.items():
        print(f"{key} - {district['district_name']}")

def display_price_categories():
    print("\nPrice categories: ")
    for key, category in price_categories.items():
        print(f"{key} - {category.capitalize()}")

def find_restaurants(district, category):
    selected_district = city_n[district]['district_name']
    restaurants = city_n[district]['restaurants']
    found_restaurants = []

    for restaurant in restaurants:
        if restaurant['price_category'] == category:
            found_restaurants.append(restaurant)

    if found_restaurants:
        print(f"\nRestaurants in {selected_district}, price category '{category}':")
        for restaurant in found_restaurants:
            print(f"Name: {restaurant['restaurant_name']}")
            print("Menu:")
            for dish, price in restaurant['menu'].items():
                print(f"  {dish}: {price} rub.")
    else:
        print(f"No restaurants found in {selected_district} with price category '{category}'.")

def input_validation(prompt, valid_inputs):
    while True:
        user_input = input(prompt)
        if user_input.lower() == 'exit':
            return 'exit'
        if user_input not in valid_inputs:
            print(f"Invalid input. Please try again.\n")
        else:
            return user_input

def restaurant_finder():
    print("Welcome to the Restaurant Finder for City N!")

    while True:
        display_districts()
        district = input_validation("Enter district number (1, 2, 3) or 'exit' to quit: ", city_n.keys())
        if district == 'exit':
            break

        display_price_categories()
        price_category = input_validation("Enter price category number (1, 2, 3): ", price_categories.keys())
        if price_category == 'exit':
            break

        find_restaurants(district, price_categories[price_category])
        print()

# Run the program
restaurant_finder()


