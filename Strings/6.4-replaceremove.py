# Write a program which takes as input an array of characters
# it removes each b and replaces each a with 2 d's.
# Along with the array, one is provided an integer-valued size. 
# size denotes the number of entries of the array that the operation
# is to be applied to. 

# for example, array is <a, b, a, c ...> and size is 4
# return <d, d, d, d, c>

start = ["a", "b", "a", "c"]

def shiftremover(array):
    for char in array:
        if char == "b":
            array.remove(char) # has to iterate to remove char from array
    for char in array:
        if char == "a":
            for i in range(2):
                array.insert(array.index(char), "d") # finds index
            array.remove(char)

# my solution will take a lot more time complexity than is necessary
# it modifies the orignial array but sloppily using python's methods

# I also forgot about the size thing.

shiftremover(start)
print(start)

# book says that this problem is trivial for O(n) time if result is 
# written to new array.

def writenew(array):
    newArray = []
    for char in array:
        if char == "b":
            pass
        elif char == "a":
            for i in range(2):
                newArray.append("d")
        else:
            newArray.append(char)
    return newArray

print(writenew(start))

# uses O(n) additional space

# but if we didn't want to use additional space, we can compute the
# final length of the resulting string, which is the len(array) plus
# the number of a's. Then we write the result char by char starting from
# the last char, going backwards. 

# so first, delete the b's, then compute final number of valid chars of string,
# using a forward iteration. Then replace a's by 2 d's, iterating backwards.
# if there are more b's then a's, the # of valid entries goes down, and if there
# are more a's than b's, the number goes up.

def replace_and_remove(size, s):
    write_idx, a_count = 0,0
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            a_count += 1

    cur_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1
    while cur_idx >= 0:
        if s[cur_idx] == "a":
            if s[cur_idx] == "a":
                s[write_idx - 1:write_idx+1] = "dd"
                write_idx -= 2
            else:
                s[write_idx] = s[cur_idx]
                write_idx -= 1
            cur_idx -= 1
    return final_size

print(replace_and_remove(4,start))
