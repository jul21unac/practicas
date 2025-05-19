from importlib.readers import remove_duplicates


def max_min(list):

    if not list:
        return [None, None]
    i=list[0]
    j=list[0]
    for x in list[1:]:

        if x >i :
            i=x
        if j > x :
            j=x
    return [i,j]


def remove_dup(arr):
    if len(arr) == 0:
        return [None]
    lis =set()

    for x in arr:
        if x not in lis:
            lis.add(x)

    return lis


def rotate_arr(arr, k):

    lis =[]
    print(len(arr))
    for x in range(len(arr)):
        lis.append(arr[x-k])

    return lis

def multiply_all_except_itself(arr):

    if len(arr) <=0 :
        return None
    j=arr[0]
    mult=1
    lis_set = []
    for x in range(len(arr)):
        mult = 1
        for i in range(len(arr)):
            if x != i :
                mult = mult * arr[i]
        lis_set.append(mult)

    return lis_set


def product_except_self(nums):
    n = len(nums)
    res = [1] * n  # Inicializa el resultado con 1s

    # Paso 1: Calcula los productos prefix (izquierda a derecha)
    prefix = 1
    for i in range(n):
        res[i] = prefix  # Almacena el producto hasta i-1
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):  # Itera desde el final
        res[i] *= suffix  # Multiplica por el producto después de i
        suffix *= nums[i]  # Actualiza suffix

    return res


    return res

if __name__ == "__main__":

    print(max_min([None]))
    a = remove_dup([1, 2, 2, 3, 4, 4,1,2,4,5] )
    for i in a:
        print(i)

    print(remove_dup([1, 2, 2, 3]))      # [1, 2, 3]
    print(remove_dup([2, 1, 2, 1]))      # [2, 1]
    print(remove_dup([]))                # []
    print(remove_dup([None, 1, None]))   # [None, 1]


    print(rotate_arr([1, 2, 3, 4, 5],2))

    #print(multiply_all_except_itself([1, 2, 3, 4]))

    print(product_except_self([1, 2, 3, 4]))