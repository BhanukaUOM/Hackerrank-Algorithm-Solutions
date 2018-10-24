# It will not possible to make all ladybugs happy
# if there is no empty cell and some ladybugs are unhappy
# or some colors have only one bug.

# Get number of game
g = int(input().strip())

# Loop for each game
for game in range (g) :

    # Get number of cell and board
    n = int(input().strip())
    b = input().strip()

    # bug_count - dictionary for storing number of ladybug in each color
    # empty_count - counter for empty cell
    # not_happy - will be True if one or more ladybugs are unhappy in the initial board
    bug_count = dict()
    empty_count = 0
    not_happy = False

    # Loop through string
    for index in range (n) :

        # If that cell is not empty
        if b[index] != "_" :

            # Count the ladybug
            if b[index] not in bug_count :
                bug_count[b[index]] = 1
            else :
                bug_count[b[index]] += 1

            # Check if it is happy or not
            if index == 0 and n > 1 :
                if b[index] != b[1] : not_happy = True
            elif index == n-1 :
                if b[index] != b[index-1] : not_happy = True
            else :
                if b[index] != b[index-1] and b[index] != b[index+1] :
                    not_happy = True

        # If cell is empty, count that cell
        else :
            empty_count += 1

    # possible - will be False if it is not possible to make all the ladybugs happy
    possible = True

    # Check if there is any color that has only one ladybug
    # If there is, then it is not possible
    for bug in bug_count :
        if bug_count[bug] == 1 : possible = False

    # If there are some ladybugs that are unhappy and no empty cell
    # Then there is no way to make them happy :(
    if empty_count == 0 and not_happy : possible = False

    # Print the result
    if possible : print("YES")
    else : print("NO")
