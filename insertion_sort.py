def insertion_sort(arr)
  for i in range(1, len(arr)):
      j = i - 1
      for k in range(i):
          if arr[i] < arr[j]:
              arr[i], arr[j] = arr[j], arr[i]
              i = i -1
              j = j - 1
