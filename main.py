def count_greater_than(numbers, n):

  count = 0
  for number in numbers:
    if number > n:
      count += 1
  return count

list = [5, 12, 3, 18, 7, 22, 10, 100]
count = count_greater_than(list, 10)
print(count)
