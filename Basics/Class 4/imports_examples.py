# Option 1
import main_functions

main_functions.get_action()

# Option 2
import main_functions as fns #fns- functions

fns.get_action()

# Option 3
from main_functions import get_action, greet

greet("Triinu")
get_action()

# Option dec
from main_functions import *   #* it means get everything

get_action()
greet("Triinu")
get_entry_details()
