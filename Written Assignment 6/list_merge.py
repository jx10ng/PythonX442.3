"""Quesiton 2: Write a function that accepts an arbitrary number of lists and returns a single 
list with exactly one occurrence of each element that appears in any of the input lists."""

def merge_list(*lists):
    newlist = set()

    for i in lists:
        newlist = newlist | set(i)

    print(newlist)
    return newlist


def main():
    list_one = [1, 1, 3, 5, 7, 8, 9]
    list_two = [2, 4, 6, 8, 10]
    list_three = [1, 11, 15]

    merge_list(list_one, list_two, list_three)

if __name__ == '__main__':
    main()
