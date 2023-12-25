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




num_to_day = {
        '1': day1,
        }

if __name__ == "__main__":
    from sys import argv
    if len(argv) != 2:
        print("Usage: python3 Solution.py <Day>")
        exit(1)
    with open("inp.txt") as f:
        num_to_day[argv[1]](f.read())

