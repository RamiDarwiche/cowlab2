from heifer_generator import HeiferGenerator
import sys
from ice_dragon import IceDragon
from dragon import Dragon

# a list of cow objects
def list_cows(cows):
    for i in range(len(HeiferGenerator.cow_names)):
        print(HeiferGenerator.cow_names[i], end=" ")
    for i in range(len(HeiferGenerator.dragon_names)):
        print(HeiferGenerator.dragon_names[i], end=" ")

# searches for corresponding cow and prints their name and image
def find_cow(name, cows):
    cowFound = False
    # iterates through cows if found, prints their image
    for i in range(len(HeiferGenerator.cow_names)):
        if HeiferGenerator.cow_names[i] == name:
            cowFound = True # used to avoid error message
            for j in range(3, len(args)):
                print(args[j], end=" ") # print user message
            print("\n" + HeiferGenerator.quote_lines, end="")
            print(HeiferGenerator.cowImages[i])
    # iterates through dragons if found, prints their image
    for i in range(len(HeiferGenerator.dragon_names)):
        if HeiferGenerator.dragon_names[i] == name:
            cowFound = True # used to avoid error message
            for j in range(3, len(args)):
                print(args[j], end=" ") # print user message
            print("\n" + HeiferGenerator.quote_lines, end="")
            print(HeiferGenerator.dragon_image)
            # uses respective can_breate_fire() methods to determine if dragon type can breathe fire
            if HeiferGenerator.dragon_types[i].can_breathe_fire():
                print("This dragon can breathe fire.")
            else:
                print("This dragon cannot breathe fire.")

    # prints error if specified cow is not found
    if cowFound == False:
        print(f"Could not find {name} cow!")


cows = HeiferGenerator.get_cows()

# list out available cows
args = sys.argv
if args[1] == '-l':
    print(f"Cows available: ", end="")
    list_cows(HeiferGenerator.get_cows())
    # search for a specific cow
elif args[1] == '-n':
    find_cow(args[2], cows)
# default cow
elif args[1] != '-n' and args[1] != '-l':
    for i in range(1, len(args)):
        print(args[i], end=" ")
    print("\n" + HeiferGenerator.quote_lines, end="")
    print(HeiferGenerator.cowImages[0])
