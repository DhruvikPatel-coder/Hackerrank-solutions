import math


def activity_notifications(expenditure, d):
    total_notifications = 0
    is_even = True
    if d % 2 == 1:
        is_even = False
    # Write your code here
    count_array = [0] * 201
    # Fill the initial count until a minimum of days have been passed
    for index in range(0, d):
        count_array[expenditure[index]] = count_array[expenditure[index]] + 1

    oldest_transaction = 0
    for index in range(d, len(expenditure)):
        if is_even:
            median = count_even_median(count_array, d)
        else:
            median = count_odd_median(count_array, d)

        if 2 * median <= expenditure[index]:
            total_notifications = total_notifications + 1
        count_array[expenditure[oldest_transaction]] = count_array[expenditure[oldest_transaction]] - 1
        count_array[expenditure[index]] = count_array[expenditure[index]] + 1
        oldest_transaction = oldest_transaction + 1

    return total_notifications


def count_even_median(count_array, cool_down_days):
    sum_of_days = 0
    for index in range(0, len(count_array)):
        sum_of_days = sum_of_days + count_array[index]
        if sum_of_days > (cool_down_days/2):
            return index
        if sum_of_days == (cool_down_days/2):
            j = index + 1
            while count_array[j] == 0:
                j = j + 1
            return (index + j)/2


def count_odd_median(count_array, cool_down_days):
    sum_of_days = 0
    for index in range(0, len(count_array)):
        sum_of_days = sum_of_days + count_array[index]
        if sum_of_days >= math.ceil(cool_down_days/2):
            return index


if __name__ == '__main__':
    answer = input()
    answer = answer.split(" ")
    li = []
    for i in answer:
        li.append(int(i))
    print(activity_notifications(li, 10000))
