class str_operations:
    def __init__(self, str):
        self.str = str

    #for reversing a string
    def reverse_str(self):
        return self.str[::-1]
    #upper case
    def upper_str(self):
        return self.str.upper()
    #lower case
    def lower_str(self):
        return self.str.lower()
