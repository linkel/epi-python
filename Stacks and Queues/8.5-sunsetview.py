import collections

# Series of buildings have windows facing west.
# buildings are in a straight line and any building to the 
# east of a building of equal or greater height cannot
# view the sunset. 

# Describe an algorithm that processes buildings in east-to-west order
# and returns the set of buildings which view the sunset.
# Each building is specified by its height.

# Brute force approach is to store all buildings in an array,
# scan thru array reverse and track the max. Any building whose height is
# less than or equal to the max does not have a sunset view.

# Time and complexity of the above would be O(n) where n is # of buildings.

# if a new building is shorter than a building in the current set, then
# there's no blockage for buildings further to the east by that one
# so LIFO storage

# Use a stack to record buildings with a view.
# Each time building b is processed, if it is taller than the building
# at the top of the stack, pop the stack until the top
# of the stack is taller than b. 
# All the buildings removed like that lie to the east of a taller one.

# Memory used is O(n) but when buildings are in increasing height, we use O(1)
# space. BF approach always uses O(n)

def examine_buildings_with_sunset(sequence):
    BuildingWithHeight = collections.namedtuple('BuildingWithHeight',
                                                ('id', 'height'))
    candidates = []
    for building_idx, building_height in enumerate(sequence):
        while candidates and building_height >= candidates[-1].height:
            candidates.pop()
        candidates.append(BuildingWithHeight(building_idx, building_height))
    return [candidate.id for candidate in reversed(candidates)]

# Solve the problem subject to the same constraints when buildings are
# presented in west to east order

#TODO