def bubble_sort(arr):
    steps=[]
    a= arr.copy()
    n=len(a)
    for i in range(n):
        for j in range(0, n-i-1):

            steps.append(("compare",j,j+1,a.copy())) #record comparisions for animation or highlight
            if a[j]>a[j+1]:
                a[j],a[j+1] =a[j+1], a[j]

                steps.append(("swap",j,j+1,a.copy()))

    return steps

def display(arr):
    for i in arr:
        print(i )

arr=[1,4,2,3]
n= len(arr)

display(arr)
steps= bubble_sort(arr)
display(steps)

