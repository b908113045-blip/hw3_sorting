def selection_sort(arr):

    n = len(arr)

    for i in range(n - 1):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
  def bubble_sort(arr):

    n = len(arr)

    for i in range(n - 1):

        for j in range(n - 1 - i):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
    def partition(arr, start, end):

    pivot = arr[start]

    left = start
    right = end

    while left < right:

        while left < right and arr[right] >= pivot:
            right -= 1

        while left < right and arr[left] <= pivot:
            left += 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

    arr[start], arr[right] = arr[right], arr[start]

    return right


def quick_sort(arr, start, end):

    if start >= end:
        return

    pivot_index = partition(arr, start, end)

    quick_sort(arr, start, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, end)
  
