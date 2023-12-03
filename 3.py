with open("schematic.txt", "r") as f:
    lines = f.readlines()

symbol_positions = []
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if not char.isnumeric() and char not in ".\n":
            symbol_positions.append((x, y, char))

part_numbers = []
for y, line in enumerate(lines):
    num_start = 0
    num_end = 0
    number = ""
    for x, char in enumerate(line):
        if char.isnumeric():
            if number == "":
                num_start = x
            number += char
        else:
            if number != "":
                num_end = x
                symbols_surrounding = list(
                    filter(
                        lambda s: num_start - 1 <= s[0] <= num_end and y - 1 <= s[1] <= y + 1,
                        symbol_positions,
                    )
                )
                if symbols_surrounding:
                    part_numbers.append(int(number))
            number = ""

print(sum(part_numbers))
