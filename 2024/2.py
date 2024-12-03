


from pathlib import Path
from loguru import logger

def read_input():
    # Read input
    input=Path("input/2.txt").read_text()

    # Split into lines
    input=input.split("\n")

    # Remove empty lines
    input=[i.strip() for i in input]
    input=[i for i in input if i != ""]

    output = []
    for row in input:
        row=row.split(" ")
        row=[int(r.strip()) for r in row]
        output.append(row)
    return output


def get_error(row):
    if len(row)!=len(list(set(row))):
        return f"repeated value in {row}"

    if row[0] > row[-1]:
        # row is descending
        x=str(row)
        row.sort(reverse=True)
        if str(row) != x:
            return f"Descending row out of order: {x} -> {row}"
            return False

    else:
        # row is descending
        x=str(row)
        row.sort(reverse=False)
        if str(row) != x:
            return f"Ascending row out of order: {x} -> {row}"
    for n in range(len(row)-1):
        lhs = row[n]
        rhs = row[n+1]
        delta = abs(lhs - rhs)
        if delta > 3:
            return f"Rapid change (|{lhs}-{rhs}|={delta}) in {row}"

    return None

def is_safe(row, dampened=False):
    error = get_error(row)
    if error is None:
        return True
    if dampened:
        for n in range(len(row)):
            dampened_row = row.copy()
            removed_value = dampened_row.pop(n)
            #logger.debug(f"{n} REMOVED {removed_value}")
            if is_safe(dampened_row, dampened=False):
                logger.debug(f"Safe by removing the level {n} ({removed_value}): {row} -> {dampened_row} ")
                return True

        #logger.error(f"NEVER FOUND A SAFE VALUE {row}")
    logger.error(error)
    return False



def part_1():
    input = read_input()
    return len([row for row in input if is_safe(row)])





def part_2():
    input = read_input()
    return sum([1 for row in input if is_safe(row, dampened=True)])




print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
