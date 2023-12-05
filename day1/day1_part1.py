# AOC2023 https://adventofcode.com/2023/day/1
#
# DAY  ONE
# --------- part 1 ------------

with open('input.txt') as f:
    sum = 0
    for line in f:

        first_digit = ''
        for c in line:
            if c.isdigit():
                first_digit += c
                break

        second_digit = ''
        for c in reversed(line):
            if c.isdigit():
                second_digit += c
                break
        sum += int(first_digit + second_digit)
    
print(f'Answer is: {sum}')                
         
