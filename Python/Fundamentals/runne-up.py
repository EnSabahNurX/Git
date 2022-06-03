if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    first=float("-inf")
    second=float("-inf")
    for i in arr:
        if i > first:
            second= first
            first=i
        if i > second and i < first:
            second=i
        print(first,second)
    print(second)
