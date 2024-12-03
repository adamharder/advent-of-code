


from pathlib import Path


def read_input():
    # Read input
    input=Path("input/1.txt").read_text()

    # Split into lines
    input=input.split("\n")

    # Remove empty lines
    input=[i.strip() for i in input]
    input=[i for i in input if i != ""]

    # Split into two lists, the left list and the right list
    lhs=[i.split(" ")[0] for i in input]
    rhs=[i.split(" ")[-1] for i in input]

    # Convert to integers
    lhs=[int(i) for i in lhs]
    rhs=[int(i) for i in rhs]
    return (lhs, rhs)

def part_1():
    lhs, rhs = read_input()
    # Sort the lists
    lhs.sort()
    rhs.sort()
    # Make the list of distances
    deltas = [abs(lhs[i]-rhs[i]) for i in range(len(lhs))]
    return sum(deltas)


def part_2():
    lhs, rhs = read_input()


    # Get lhs as a unique set:
    # lhs=list(set(lhs))
    # rhs.sort()
    # Make the list of distances
    scores = [lhs[i] * rhs.count(lhs[i]) for i in range(len(lhs))]
    return sum(scores)



print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
# print(len(input))
# print(len(lhs))
# print(len(rhs))
# print(sum(lhs))
# print(sum(rhs))

