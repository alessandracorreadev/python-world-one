num = 0
answer = ' '
count = 0
sum_num = 0
highest = 0
lowest = 0

while answer not in 'nN':
    num = int(input("Enter a number: "))

    #summing and counting the values
    count += 1
    sum_num += num

    # testing the highest and lowest values
    if count == 1:
        highest = num
        lowest = num
    else:
        if num > highest:
            highest = num
        elif num < lowest:
            lowest = num

    # asking for continue
    answer = input("Do you want to continue? [Y/N]: ").strip().lower()[0]

    # do not accept anything but y/n
    while answer not in 'nNyY':
        answer = input("Invalid option. Do you want to continue? [Y/N]: ").strip().lower()[0]

# calculating average
average = sum_num / count

print(f"You entered {count} numbers and the average is {average}.")
print(f"The highest value is {highest} and the lowest value is {lowest}.")
