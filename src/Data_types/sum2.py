

def sum(list , num):

    siz = len(list)
    for x in range(siz):
        for i in range(siz-1):
            adicc = list[x]+list[i+1]
            if adicc == num :
                return str(x) +" " + str(i+1)


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

if __name__ == "__main__" :

    print(sum([3, 2, 3], 6) )
    print(two_sum([3, 2, 3], 6) )