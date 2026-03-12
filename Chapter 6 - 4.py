def calc_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

num_list = [3, 7, 17, 23, 54, 9, 13, 2]
result = calc_sum(num_list)
print(f"The sum of the list {num_list} is: {result}")