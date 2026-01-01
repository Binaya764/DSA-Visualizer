def bubble_sort(arr):
    steps=[]
    a= arr.copy()
    n=len(a)
    for i in range(n-1):
        for j in range(0, n-i-1):

            steps.append(("compare",j,j+1,a.copy())) #record comparisions for animation or highlight
            if a[j]>a[j+1]:
                a[j],a[j+1] =a[j+1], a[j]

                steps.append(("swap",j,j+1,a.copy())) #provides swap signal when swapping the elements



    return steps







