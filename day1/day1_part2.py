# AOC2023 https://adventofcode.com/2023/day/1#part2
#
# DAY  ONE
# --------- part 2 ------------

import re


with open('input.txt') as f:
    sum = 0
    number_strings = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for line in f:
        first_digit = ''
        last_digit = ''
        first_digit_idx = 1000 # start with fake values that are out of bounds of reasonable input
        last_digit_idx = -1

        for idx, number_string in enumerate(number_strings):
            substring_indexes = [c.start() for c in re.finditer(number_string, line)]
            if len(substring_indexes) > 0:
                min_idx = min(substring_indexes)
                max_idx = max(substring_indexes)

                if min_idx < first_digit_idx:
                    first_digit = str(idx)
                    first_digit_idx = min_idx 
                
                if max_idx > last_digit_idx:
                    last_digit = str(idx)
                    last_digit_idx = max_idx 

        digit_indexes = [c.start() for c in re.finditer(r'\d', line)]
        if len(digit_indexes) > 0:
            min_idx = min(digit_indexes)
            max_idx = max(digit_indexes)

            if min_idx < first_digit_idx:
                first_digit = line[min_idx]
                first_digit_idx = min_idx 
            
            if max_idx > last_digit_idx:
                last_digit = line[max_idx]
                last_digit_idx = max_idx 
            
        sum += int(first_digit + last_digit)

print(f'Answer is: {sum}')   