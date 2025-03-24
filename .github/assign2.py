# Created by: Hiab G
# Date: Wed, Feb. 25th
# This program calculates the surface area and volume of a hexagonal prism 
import math
import colorama

# code from https://www.youtube.com/watch?v=u51Zjlnui4Y
from colorama import Fore, Style


def calculate_surface_area(a, h):
    # Surface area formula: A = 6ah + 3√3a²
    surface_area = 6 * a * h + 3 * math.sqrt(3) * (a**2)
    return surface_area


def calculate_volume(a, h):
    # Volume formula: V = (3√3 / 2) * a² * h
    volume = (3 * math.sqrt(3) / 2) * (a**2) * h
    return volume


def main():
    print("Welcome to the Hexagonal Prism Calculator!")

    # User input for base length (a), base (h), units, and color
    Base = float(input("Enter the base (a) of the hexagonal prism: "))
    height = float(input("Enter the height (h) of the hexagonal prism: "))
    units = input("Enter the units of measurement (e.g., meters, inches): ")

    # Calculate surface area and volume
    surface_area = calculate_surface_area(Base, height)
    volume = calculate_volume(Base, height)

    # Display the results
    print("\nHexagonal Prism :")
    print("Base Length (a): {Base} {units}")
    print("Height (h): {height} {units}")

    # Print results in bold red with 2 decimal places
    # code from https://www.youtube.com/watch?v=u51Zjlnui4Y
    from colorama import Fore, Style

    print(f"{Fore.RED + Style.BRIGHT}Results:")
    print(f"{Fore.RED + Style.BRIGHT}Surface Area: {surface_area:.2f} {units}")
    print(f"{Fore.RED + Style.BRIGHT}Volume: {volume:.2f} {units}")


if __name__ == "__main__":
    main()
