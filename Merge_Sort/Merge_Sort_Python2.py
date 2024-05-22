#Credit to Dhaval Patel from codebasics youtube channel
def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    return merge_two_sorted_lists(left,right,arr)

def merge_two_sorted_lists(a,b,arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0
    while i < len_a and j < len_b:
        #Here we take the sorted lists and we go through them and start by comparing the beginning
        #   of each list and then incrementing indexes as we go along 
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k+=1
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k+=1

    while j < len_a:
        arr[k] = b[j]
        j += 1
        k+=1 

    
if __name__ == '__main__':
    arr = [10, 3, 15, 7, 8, 23, 98, 29]
    merge_sort(arr)
    print(arr)