def merge(list_left, list_right):
    l, r = 0, 0
    new_list = []
    while l < len(list_left) and r < len(list_right):
        if list_left[l] < list_right[r]:
            new_list.append(list_left[l])
            l += 1
        else:
            new_list.append(list_right[r])
            r += 1
    new_list += list_left[l:]
    new_list += list_right[r:]

    return new_list


def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list) // 2
    list_left = merge_sort(list[:mid])
    list_right = merge_sort(list[mid:])

    return merge(list_left, list_right)


if __name__ == "__main__":
    print(merge_sort([2, 4, 1, 7, 10, 6, 8]))
