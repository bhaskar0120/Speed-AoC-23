def day1(file):
    import string
    ans = 0
    for i in file.split("\n"):
        nums = []
        for j in i:
            if j in string.digits:
                nums.append(int(j))
        ans += nums[0]*10 + nums[-1]
    print(ans)


    ans = 0
    nums_as_words = ['one','two','three','four','five','six','seven','eight','nine']
    words_to_nums = {i:j for j,i in enumerate(nums_as_words,1)}
    for i in file.split("\n"):
        nums = []
        for j,val in enumerate(i):
            if val in string.digits:
                nums.append(int(val))
                continue
            for k in nums_as_words:
                if i[j:j+len(k)] == k:
                    nums.append(words_to_nums[k])
                    break
        ans += nums[0]*10 + nums[-1]
    print(ans)


def day2(file):
    ans1 = 0
    ans2 = 0
    color_limits = {
            'red' : 12,
            'green' : 13,
            'blue' : 14,
            }
    for i in file.split("\n"):
        parts = i.split(':')
        gameid = int(parts[0].split(' ')[1])
        flag = True
        min_color = {
                'red' : 0,
                'green' : 0,
                'blue' : 0,
                }
        for sets in parts[1].split(';'):
            for balls in sets.split(','):
                count, color = balls.split(' ')[1:]
                count = int(count)
                min_color[color] = max(min_color[color], count)
                if count > color_limits[color]:
                    flag = False
        if flag:
            ans1 += gameid
        ans2 += min_color['red']*min_color['green']*min_color['blue']
    print(ans1)
    print(ans2)

num_to_day = {
        '1': day1,
        '2': day2,
        }

if __name__ == "__main__":
    from sys import argv
    if len(argv) != 2:
        print("Usage: python3 Solution.py <Day>")
        exit(1)
    with open("inp.txt") as f:
        num_to_day[argv[1]](f.read())

