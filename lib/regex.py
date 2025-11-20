import re

my_pattern = r"[A-Z][A-Za-z' ,]*today[A-Za-z' ,]*[.?]"  # Matches sentences with capitalized start, containing 'today', ending with . or ?
my_regex = re.compile(my_pattern)

