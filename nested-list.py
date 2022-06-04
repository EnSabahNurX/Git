def sort_key(score_list):
    return score_list[1]


if __name__ == '__main__':
    students_list = []
    name_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_list.append([name, score])
    students_list.sort(key=sort_key)
    low, slow = float("inf"), float("inf")
    for inner in students_list:
        if inner[1] < low:
            slow = low
            low = inner[1]
        if inner[1] < slow and inner[1] > low:
            slow = inner[1]
    for j in students_list:
        if j[1] == slow:
            name_list.append(j)
    name_list.sort()
    for k in name_list:
        print(k[0])


# a = [[raw_input(), float(raw_input())] for i in xrange(int(raw_input()))]
# s = sorted(set([x[1] for x in a]))
# if len(s) > 1:
#     for name in sorted(x[0] for x in a if x[1] == s[1]):
#         print name


# marksheet = []
# for _ in range(0,int(input())):
#     marksheet.append([input(), float(input())])

# second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
# print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
