'''
Trying inheritance to create a more flexible dictionary type.
'''
class FlexibleDict(dict):
    '''
    This class it as dict but with more flexibility when
    searching for keys.
    '''
    def __init__(self):
        '''
        just inherit the constructor from dict.
        '''
        dict.__init__(self)


    def __getitem__(self, item):
        '''
        Try to search the keys seeing it as a string or as an integer.
        '''
        try:
            return dict.__getitem__(self, str(item))
        except KeyError:
            print("string Key not found")
            try:
                return dict.__getitem__(self, int(item))
            except (KeyError, ValueError) as tmp:
                print("Key not found or value not convertible in integer")
                return None
#---


if __name__ == '__main__':
    mydict = FlexibleDict()
    mydict['a'] = 1
    mydict[1] = 'uno'
    print(mydict['a'])
    print(mydict['1'])
    print(mydict)
