def counterClockwise(a):
   if not a or not a[0]:
      return []
   b = len(a)
   for c in a:
      c.reverse()
   for d in range(b):
      for e in range(d):
         a[d][e], a[e][d] = a[e][d], a[d][e]
   for b in a:
      print(b)
   return a

list_awal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

counterClockwise(list_awal)