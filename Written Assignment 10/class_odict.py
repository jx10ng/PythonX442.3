"""Question 3: (Extra Credit) Using the UserDict module, create a class called Odict, which will be just like a 
dictionary but will "remember" the order in which key/value pairs are added to the dictionary. 
(Hint: Override the built-in __setitem__ method.) 
Create a new method for the Odict object called okeys, which will return the ordered keys."""

from collections import UserDict

class Odict(UserDict):
    ordered_keys = []

    def __setitem__(self, key, item):
        # Save the key to ordered_keys, since a List will keep order.
        self.ordered_keys.append(key)

        # Put the value into the dict
        return super(Odict, self).__setitem__(key, item)

    def okeys(self):
        return self.ordered_keys

def main():
    d = Odict()

    d[1] = 'one'
    d[0] = 'zero'
    d[5] = 'five'
    d[2] = 'two'

    print('dict: {}, okeys: {}'.format(d, d.okeys()))


if __name__ == '__main__':
    main()
