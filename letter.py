#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: November 2019
# This is a program which finds the volume of the cylinder.


# This allows me to do things with the text.
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def Address(appartement_copy, adressee_name_copy, building_number_copy,
            street_name_copy, jurisdiction_copy, city_copy, province_copy,
            postal_code_copy, apt_number_copy=None):
    # This puts the info together.
    if appartement_copy == ("YES") or appartement_copy == ("yes") or \
       appartement_copy == ("Y"):
        address = ("{0} \n  {1} {2} {3} {4} \n {5} {6} {7}"
                   .format(adressee_name_copy, apt_number_copy,
                           building_number_copy, street_name_copy,
                           jurisdiction_copy, city_copy, province_copy,
                           postal_code_copy))
    else:
        address = ("{0} \n{1} {2} {3} \n{4} {5} {6}"
                   .format(adressee_name_copy, building_number_copy,
                           street_name_copy, jurisdiction_copy, city_copy,
                           province_copy, postal_code_copy))

    return address


def main():
    # This is what gets the dimensions of the cylinder
    adressee_name = input(color.YELLOW + "Enter the name of the adressee: " +
                          color.END)

    appartement = input(color.YELLOW + "Do they have an appartement? (Y/N): " +
                        color.END)

    if appartement == ("YES") or appartement == ("yes") or \
       appartement == ("Y"):
        apt_number = input(color.YELLOW + "Enter their appartement number: " +
                           color.END)

    building_number = input(color.YELLOW + "Enter their buildings number: " +
                            color.END)

    street_name = input(color.YELLOW + "Enter their street's name: " +
                        color.END)

    jurisdiction = input(color.YELLOW + "Enter their jurisdiction: " +
                         color.END)

    city = input(color.YELLOW + "Input their city's name: " + color.END)

    province = input(color.YELLOW + "Input their province's name: " +
                     color.END)

    postal_code = input(color.YELLOW + "Input their postal code: " + color.END)

    if appartement == ("YES") or appartement == ("yes") or \
       appartement == ("Y"):
        full_address = Address(appartement_copy=appartement,
                               adressee_name_copy=adressee_name,
                               building_number_copy=building_number,
                               street_name_copy=street_name,
                               jurisdiction_copy=jurisdiction,
                               city_copy=city,
                               province_copy=province,
                               postal_code_copy=postal_code,
                               apt_number_copy=apt_number)
    else:
        full_address = Address(appartement_copy=appartement,
                               adressee_name_copy=adressee_name,
                               building_number_copy=building_number,
                               street_name_copy=street_name,
                               jurisdiction_copy=jurisdiction,
                               city_copy=city,
                               province_copy=province,
                               postal_code_copy=postal_code)
    print("")
    print(full_address)


if __name__ == "__main__":
    main()
