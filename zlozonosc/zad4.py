#a) O(N+K)=N+K
#
def fun1(arr1, arr2):
    for i in range(0, len(arr1)):
        print(arr1[i])
    for j in range(0, len(arr2)):
        print(arr2[j])
#b)
# O(N+K)=N*K
def fun2(arr1, arr2):
    for i in range(0, len(arr1)):
        for j in range(0, len(arr2)):
            print(arr1[i] + arr2[j])





#c) O(N) = N*K  T(N)=N*K*10
#
def fun3(arr1, arr2):
    for i in range(0, len(arr1)):
        for j in range(0, len(arr2)):
            for k in range (0, 10):
                print(arr1[i] + arr2[j] + k)

#d) O(N) = sqrt(N)
#
def fun4(n):
    i = 1
    while i * i <= n:
        print(i)

if __name__ == '__main__':

    dane1 = [3, 7, 9, 12, 19, 30, 41, 56, 71]
    dane2 = [8, 4, 2, 8, 1]

    fun1(dane1, dane2)






