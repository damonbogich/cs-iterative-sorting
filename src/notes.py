sum = 0 
n = 10
for i in range(n): # O(n * (1 + (log n)))
    j = 1
    while j < n:
        j *= 2
        sum += 1




#insertion sort:
def insert_sort(input_list):
    #seperate first element - think of it as sorted
        #no code require for this step

    #for all unsorted items:
    for i in range(1, len(input_list)):
        #mark current item we're considering
        current = input_list[i] 
        #look left until we find the proper place to insert the current item
        #as we look left, we need to shift items to the right
        j = i
        while j > 0 and current < input_list[j - 1]:
            input_list[j] = input_list[j - 1]
            j -= 1

         #when item to left is less than current or equal to current
        #or there are no items to the left
            #insert item
        input_list[j] = current 
    return input_list

#run this in debugger:
print(insert_sort([10, 9, 8, 7, 6, 5, 4]))
