arr = [1, 3, 4, 9, 7]
sum = 14

def hasPairSum(arr, sum):
    diff = []
    for x in arr:
        d = sum -x
        if d in diff:
            return [d, x]
        else:
            diff.append(x)
    return []

print(hasPairSum(arr, sum))


