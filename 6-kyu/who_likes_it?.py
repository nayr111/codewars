def likes(names):
    # first, we need to determine how many elements (names for this) are in the list given.
    # then, we must return the proper text depending on how many names are on the list
    # to do this, we can use conditionals, but also, the text has to have the names in it as well
    # so we can implement the names from the list into our text
    # and if there are 4 or more people, we must return the first 2 people's names, followed by the 
    # amount of people left in the list
    others_count = len(names) - 2
    if len(names) >= 4:
        return f"{names[0]}, {names[1]} and {others_count} others like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    else:
        return "no one likes this"
