#!/usr/bin/env python3

# Created by: Andrew-Ten-Den
# Created on: June 2022
# This program calculates the surface area of a cube


def calculate_surface_area(length):
    # calculate surface area area

    # process
    surface_area = length * length * 6

    # output
    print("The surface area is {0} cm²".format(surface_area))


def main():
    # this function gets length

    try:
        # input
        length = int(input("Enter the length of the cube (cm): "))

        print("")

        calculate_surface_area(length)
    except Exception:
        print("\nPlease enter a valid positive integer.")


if __name__ == "__main__":
    main()
