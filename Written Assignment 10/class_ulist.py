"""Question 2: Python provides several modules to allow you to easily extend some of the basic objects in the language. 
Among these modules are UserDict, UserList, and UserString. (Refer to the chart in Topic 10.3 to see what 
the methods you need to override look like. Also, since UserDict and UserList are part of the collection module, 
you can import them using from collections import UserDict and from collections import UserList.)


Using the UserList module, create a class called Ulist, and override the __add__, append, and extend methods 
so that duplicate values will not be added to the list by any of these operations.
"""

from collections import UserList


class Ulist(UserList):
    def __add__(self, list):
        new_values = []

        for value in list:
            if value not in self:
                new_values.append(value)

        return super(Ulist, self).__add__(new_values)

    def append(self, value):
        if value not in self:
            return super(Ulist, self).append(value)

    def extend(self, list):
        for value in list:
            if value not in self:
                self.append(value)


def main():
    l = Ulist()

    l.append(1)
    l.append(2)
    l.append(1)
    l = l + [1, 2, 3, 4]
    l.extend([5, 6, 7])

    print(l)


if __name__ == '__main__':
    main()
