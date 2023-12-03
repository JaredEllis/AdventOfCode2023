word_nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open('calibration.txt') as f:
    lines = f.readlines()
    split = [line[:-1] for line in lines]
    nums = [[int(char) for char in line if char.isdigit()] for line in split]
    val_sum = 0
    for num_line in nums:
        val_sum += int(f'{num_line[0]}{num_line[-1]}') if len(num_line) > 1 else int(f'{num_line[0]}{num_line[0]}')
    print(val_sum)
