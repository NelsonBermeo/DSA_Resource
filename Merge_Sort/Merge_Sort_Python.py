#Credit to Dhaval Patel from codebasics youtube channel
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge_two_sorted_lists(left,right)

def merge_two_sorted_lists(a,b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0
    while i < len_a and j < len_b:
        #Here we take the sorted lists and we go through them and start by comparing the beginning
        #   of each list and then incrementing indexes as we go along 
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    
    while i < len_a:
        sorted_list.append(a[i])
        i += 1

    while j < len_a:
        sorted_list.append(b[j])
        j += 1

    return sorted_list

if __name__ == '__main__':
    arr = [10, 3, 15, 7, 8, 23, 98, 29]

    print(merge_sort(arr))

#This code is not optimal for space because we keep on creating lists, what if we can do all this within our list? 
