############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.f_harv = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types (see types.txt for the list)."""

    all_melon_types = []

    # loop?
        # instantiates the class MelonType for each of the above melon types.
        # After you instantiate a melon, also call the add_pairing method to add necessary pairings to the instance’s pairings attribute.
        # add each MelonType instance (object) to a list

    # return a list of objects of the class MelonType


    # Fill in the rest

    return all_melon_types


def help_make_melons(filename):
    """Create and return a dictionary of current melon types using types.txt as filename."""
    the_file = open(filename)
    mydict = {}
    for line in the_file:
        print(line)
        if ':' in line:
            key, value = line.lower().rstrip().split(': ')
            print(f"key is {key} and value is {value}")
            if key == 'name':
                melon_key = value
                mydict[melon_key] = {}
                n_dict = mydict[melon_key]  # refers to nested dictionary

            # adding key-value pairs to nested dictionary (mydict[melon_key] aka n_dict)
            if key == 'pairings':
                # for pairings, split by commas
                pairing_options = value.split(', ')
                n_dict[key] = pairing_options
            else:
                n_dict[key] = value if value not in ('true', 'false') else True if value in ('true') else False
    the_file.close()
    return mydict


file = 'types.txt'
melon_dict = help_make_melons(file)



def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



