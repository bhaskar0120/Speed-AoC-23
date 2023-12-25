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

def day3(file):
    import string
    chars = [[i for i in j] for j in file.split("\n")]
    n = len(chars)
    m = len(chars[0])
    grid = [[False]*m for i in range(n)]

    for i in range(n):
        for j in range(m):
            if chars[i][j] != '.' and chars[i][j] not in string.digits:
                grid[i][j] = True
                for dx in range(-1,2):    
                    for dy in range(-1,2):
                        if i+dx < 0 or i+dx >= n or j+dy < 0 or j+dy >= m:
                            continue
                        grid[i+dx][j+dy] = True
    ans = 0
    num = 0
    flag = False
    for i in range(n):
        for j in range(m):
            if chars[i][j] in string.digits:
                num = num*10+int(chars[i][j])
                flag = flag or grid[i][j]
            else:
                if num > 0 and flag:
                    ans += num
                    num = 0
                flag = False
                num = 0
    print(ans)  

    grid = [[list() for j in range(m)] for i in range(n)]
    counter = 0;
    for i in range(n):
        for j in range(m):
            if chars[i][j] == '*':
                for dx in range(-1,2):
                    for dy in range(-1,2):
                        if i+dx < 0 or i+dx >= n or j+dy < 0 or j+dy >= m:
                            continue
                        grid[i+dx][j+dy].append(counter)
                counter += 1
    ans = 0
    num = 0
    relation = []
    gear_data = {}
    for i in range(n):
        for j in range(m):
            if chars[i][j] in string.digits:
                num = num*10+int(chars[i][j])
                relation += grid[i][j]
            else:
                if num > 0 and len(relation) > 0: 
                    for k in set(relation):
                        if k not in gear_data:
                            gear_data[k] = []
                        gear_data[k].append(num)
                relation = []
                num = 0

    for i in gear_data:
        if len(gear_data[i]) == 2:
            ans += gear_data[i][0]*gear_data[i][1]
    print(ans)






num_to_day = {
        '1': day1,
        '2': day2,
        '3': day3,
        }

if __name__ == "__main__":
    from sys import argv
    if len(argv) != 2:
        print("Usage: python3 Solution.py <Day>")
        exit(1)
    with open("inp.txt") as f:
        num_to_day[argv[1]](f.read())

