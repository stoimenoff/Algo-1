class Roots:

    # Finds the square root of a number using binary search.
    # number - int
    def square_root(self, number):
        if number < 0:
            return "NaN"
        if number == 1:
            return 1.0
        low = 0.0
        high = number
        root = low + (high-low)/2
        while abs(number - root*root) > 0.00001:
            # get better root
            if number > root*root:
                low = root
            else:
                high = root
            root = low + (high-low)/2
        return root
        
def main():
    number = int(input())
    print ("%.5f" % Roots().square_root(number))

main()