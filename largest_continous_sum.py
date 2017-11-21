def l_c_s(arr):

    if len(arr) == 0:
        print("zero")

    max_sum = current_sum = arr[0]

    for num in arr[1:]:

        current_sum = max(current_sum + num, current_sum)
        max_sum = max(current_sum, max_sum)
        
    print(max_sum)

ar = [1, -2, 3, -4, -5, -7, -6, -2, -1]

l_c_s(ar)
