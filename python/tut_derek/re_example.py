import sys
import math
import time
import re
 
# ---------- Was a Match Found ----------
if re.search("ape", "The ape at the apex"):
    print("There's an ape")

# findall() returns a list of matches
# . is used to match any 1 character or space
allApes = re.findall("ape", "The ape at the apex")

for i in allApes:
    print(i)

# finditer returns an iterator of matching objects
# You can use span to get the location
the_str = "The ape at the apex"

for i in re.finditer("ape.", the_str):

    # Span returns a tuple
    loc_tuple = i.span()
    print(loc_tuple)
    print(the_str[loc_tuple[0]:loc_tuple[1]])
