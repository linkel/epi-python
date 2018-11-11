# Write a program which takes a pathname and returns the shortest equivalent pathname
# Assume individual directories and files have names that use only alphanumeric
# characters

# subdirectory names can be combined using forward slashes, the current directory,
# and the parent directory

def shortest_equivalent_path(path):
    if not path:
        raise ValueError('Empty string is not a valid path.')
    
    path_names = []
    # Special case: / is an absolute path so we can't go up from it
    if path[0] == '/':
        path_names.append('/')
    
    for token in (token for token in path.split('/') if token not in ['.', '']):
        if token == '..':
            if not path_names or path_names[-1] == '..':
                path_names.append(token)
            else:
                if path_names[-1] == '/':
                    raise ValueError('Path error')
                path_names.pop()
        else:
            path_names.append(token)
    
    result = '/'.join(path_names)
    return result[result.startswith('//'):] # True is 1 and False is 0 so it cuts the
    # first two slashes out if it starts with //

example = "sc//./../tc/awk/././"
# from a starting folder, we go into sc. // doesn't do anything, it is just
# historical compatibility. One dot is current folder. Two dots goes up a directory.
# so we went into sc and came back out, then we went into tc/awk. 
print(shortest_equivalent_path(example))

