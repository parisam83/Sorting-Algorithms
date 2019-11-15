'''This insertion sort algorithm
   is faster and much more easier to 
   understand for beginners...'''
   
   
def insertion_sort_fast(arr):
  for i in range(1, len(arr)):
      j = i - 1
      for k in range(i):
          if arr[i] < arr[j]:
              arr[i], arr[j] = arr[j], arr[i]
              i = i -1
              j = j - 1

#insertion_sort_fast(arr)
#print(arr)
