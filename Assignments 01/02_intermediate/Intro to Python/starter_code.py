#         **Intro to Python**

# starter_code
# Planetary Weights Project
"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.
"""

def main():
    # Gravity constants relative to Earth
    gravity_factors = {
        'Mercury': 0.38,
        'Venus': 0.91,
        'Earth': 1.00,
        'Mars': 0.38,
        'Jupiter': 2.34,
        'Saturn': 1.06,
        'Uranus': 0.92,
        'Neptune': 1.19
    }
    
    # Prompt for input
    weight = float(input("Enter your weight on Earth (in kg): "))
    planet = input("Enter the planet name: ")

    # Check if the planet exists in the dictionary
    if planet in gravity_factors:
        # Calculate equivalent weight
        planet_weight = weight * gravity_factors[planet]
        print(f"Your weight on {planet} would be: {planet_weight:.2f} kg.")
    else:
        print("Sorry, that planet is not supported.")

if __name__ == "__main__":
    main()


# Mars Weight

"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

def main():
    # Gravity constant for Mars
    mars_gravity = 0.38

    # Prompt for input
    weight = float(input("Enter your weight on Earth (in kg): "))

    # Calculate equivalent weight on Mars
    mars_weight = weight * mars_gravity
    print(f"Your weight on Mars would be: {mars_weight:.2f} kg.")

if __name__ == "__main__":
    main()
