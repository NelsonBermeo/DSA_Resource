
def merge_sort(ls):
    if len(ls) <= 1:
        return ls
    mid = len(ls)//2
    left = ls[:mid]
    right = ls[mid:]
    merge_sort(left)
    merge_sort(right)
    return merge_two_sorted_lists(left,right)

def merge_two_sorted_lists(ls1, ls2):

    i = j = k = 0
    while len(ls1) > i and len(ls2) > j:
        if ls1[i] <= ls2[j]:
            temp_ls.append(ls1[i])
            i += 1
            k 3
        elif ls1[i] > ls2[j]:
            temp_ls.append(ls2[j])
            j += 1
    
    while len(ls1) > i:
        temp_ls.append(ls1[i])
        i += 1

    while len(ls2) > j:
        temp_ls.append(ls2[j])
        j += 1
    
    return temp_ls

if __name__ == "__main__":
    ls1 = [2, 3, 4, 9]
    ls2 = [1, 4, 6, 10]
    ls = [1, 3, 1, 9, 3, 2, 0, 2]

    print(merge_sort(ls))

