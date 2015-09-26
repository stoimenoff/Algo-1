class PhoneBook:
    # Merge sort phone book
    # book - [(int, String)]
    def sort_phone_book(self, book):
        if len(book) <= 1:
            return book
        first_half = self.sort_phone_book(book[0:int(len(book)/2)])
        second_half = self.sort_phone_book(book[int(len(book)/2):])
        sorted_book = []
        while first_half != [] and second_half != []:
            if first_half[0][0] < second_half[0][0]:
                sorted_book.append(first_half[0])
                first_half.remove(first_half[0])
            else:
                sorted_book.append(second_half[0])
                second_half.remove(second_half[0])
        sorted_book += (first_half + second_half)
        return sorted_book
    # Find the names of people based on their phone numbers.
    # phone_book - [(int, String)]
    # numbers - [int]
    def lookup_names(self, phone_book, numbers):
        phone_book = self.sort_phone_book(phone_book)
        result = []
        for number in numbers:
            low = 0
            high = len(phone_book) - 1

            while low <= high:
                middle = int(low + (high - low) / 2)

                if phone_book[middle][0] == number:
                    result.append(phone_book[middle][1])
                    break
                elif phone_book[middle][0] < number:
                    low = middle + 1
                else:
                    high = middle - 1

            if phone_book[middle][0] != number:
                result.append(None)

        return result
def main():
    book = []
    nums = []
    n_m = [int(num) for num in input().split(" ")]
    n = n_m[0]
    m = n_m[1]
    for i in range(n):
        entry = [item for item in input().split(" ")]
        book.append((int(entry[0]), entry[1]))
    for i in range(m):
        num = int(input())
        nums.append(num)
    result = PhoneBook().lookup_names(book, nums)
    for item in result:
        print(item)
main()