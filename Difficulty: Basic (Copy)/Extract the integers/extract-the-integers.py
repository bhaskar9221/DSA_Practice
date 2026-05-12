class Solution:

    def extractIntegerWords(self, s):
        # code here
        num = []
        n = ''
        for i in s:
            # Checking i is digit or not
            # if digit the add i into n string
            if i.isdigit():
                n += i
            # if i not digit
            # then checking n is empty or not
            # if not then append n into num
            elif n:
                num.append(n)
                n = ''
        # Cheking n is empty or not after the loop
        # if not empty then append n into num
        if n:
            num.append(n)
        return num