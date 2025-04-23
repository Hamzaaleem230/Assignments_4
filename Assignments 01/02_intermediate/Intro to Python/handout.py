#         **Intro to Python**

# handout
# Mars Weight Solution

MARS_MULTIPLE = 0.378  # Mars gravity as a percentage of Earth's gravity

def main():
    # Prompt the user for their weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))

    # Calculate the weight on Mars
    mars_weight = earth_weight * MARS_MULTIPLE
    rounded_mars_weight = round(mars_weight, 2)

    # Print the result
    print(f"The equivalent weight on Mars: {rounded_mars_weight}")

if __name__ == "__main__":
    main()



# Planetary Weight Solution

# Gravitational constants for each planet compared to Earth
GRAVITY_CONSTANTS = {
    "Mercury": 0.376,  # 37.6%
    "Venus": 0.889,    # 88.9%
    "Mars": 0.378,     # 37.8%
    "Jupiter": 2.36,   # 236.0%
    "Saturn": 1.081,   # 108.1%
    "Uranus": 0.815,   # 81.5%
    "Neptune": 1.14,   # 114.0%
    "Earth": 1.0       # 100% (just for reference)
}

def main():
    # Prompt the user for their weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))

    # Prompt the user for the name of a planet
    planet = input("Enter a planet: ")

    # Check if the planet is in the gravity constants dictionary
    if planet in GRAVITY_CONSTANTS:
        # Get the gravity constant for the selected planet
        gravity_constant = GRAVITY_CONSTANTS[planet]

        # Calculate the equivalent weight on the selected planet
        planetary_weight = earth_weight * gravity_constant
        rounded_planetary_weight = round(planetary_weight, 2)

        # Print the result
        print(f"The equivalent weight on {planet}: {rounded_planetary_weight}")
    else:
        print("Invalid planet name. Please enter a valid planet.")

if __name__ == "__main__":
    main()
