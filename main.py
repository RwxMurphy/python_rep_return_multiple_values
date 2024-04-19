def analyse_numbers(list_num):
    """
    Function runs basic analysis on a list of numbers.
    parameters:
    list_num(list): list of numbers
    returns:
    tuple: returns result of analysis
    """
    min = float("inf")
    max = float("-inf")
    avg = 0
    sum = 0

    for n in list_num:
        # find min
        if n < min:
            min = n
        # find max
        if n > max:
            max = n

        # sum
        sum += n
        # average
        avg = sum/len(list_num)

    return (sum, avg, max, min)


result = analyse_numbers([5, 10, 20, 25])
print(result)
