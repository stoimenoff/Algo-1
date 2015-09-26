class BirthdayRanges:

    # Return a vector with the number of people born in the specific ranges.
    # birthdays - [int]
    # ranges - [(int, int)]
    def birthdays_count(self, birthdays, ranges):
        days = [0] * 366
        for birthday in birthdays:
            days[birthday] += 1
        for i in range(1, 366):
            days[i] += days[i - 1]
        result = []
        for b_range in ranges:
            if b_range[0] == 0:
                result.append(days[b_range[1]])
            else: 
                result.append(days[b_range[1]] - days[b_range[0] - 1])
        return result

ranges = []
n_m = [int(num) for num in input().split(" ")]
m = n_m[1]
birthdays = [int(b_day) for b_day in input().split(" ")]
for i in range(m):
    b_range = [int(num) for num in input().split(" ")]
    ranges.append((b_range[0],b_range[1]))
result = BirthdayRanges().birthdays_count(birthdays, ranges)
for item in result:
    print (item)
