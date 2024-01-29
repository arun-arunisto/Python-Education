class StringOperations:
    def __init__(self, string):
        self.string = string
    #reverse string
    def reverse_string(self):
        return self.string[::-1]
    #upper case
    def upper_case(self):
        return self.string.upper()
    #lower case
    def lower_case(self):
        return self.string.lower()

if __name__ == '__main__':
    string_op = StringOperations('arunisto')
    print(string_op.reverse_string())
    print(string_op.upper_case())
    print(string_op.lower_case())
