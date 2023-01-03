def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        # elements on leftside that were left "unmerged"
        # (because they are bigger than the rest)
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        # elemnts on rightside that were left "unmerged"
        # (because they are bigger than the rest)
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1


x = [14,46,43,27,57,41,45,21,70,15,1]
merge_sort(x)
print(x)
y = [5, 1, 4, 2, 8]
merge_sort(y)
print(y)