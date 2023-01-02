#11. Write a Python function that takes two lists and returns True if they have at least one common member.
list_one = [1, 2, 3, 4, 5]
list_two = [8, 9, 5, 10, 11]
def common_member(li1, li2):
    for i in li1:
        if i in li2:
            return True
    else:
        return False

print(common_member(list_one, list_two))