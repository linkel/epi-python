# write a program that prints a sequence of operations that transfers 
# n rings from one peg to another.
# You have a third peg, which is initially empty. 
# Only op allowed is to take a single ring from the top of a peg and 
# putting it on the top of another peg. Cannot put a larger ring atop
# a smaller ring. 

NUM_PEGS = 3

def compute(num_rings):
    def compute_steps(num_rings_to_move, from_peg, to_peg, use_peg):
        if num_rings_to_move > 0:
            compute_steps(num_rings_to_move - 1, from_peg, use_peg, to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])
            compute_steps(num_rings_to_move - 1, use_peg, to_peg, from_peg)

    result = []
    pegs = [list(reversed(range(1, num_rings + 1)))
            ] + [[] for _ in range(1, NUM_PEGS)]
    compute_steps(num_rings, 0, 1, 2)
    return result


print(compute(3))