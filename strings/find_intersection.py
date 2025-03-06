def FindIntersection(strArr):

  # code goes here
  i = 0
  j = 0
  left = [int(x) for x in strArr[0].split(",")]
  right = [int(x) for x in strArr[1].split(",")]

  intersection = []
  while i < len(left) and j < len(right):
    if left[i] == right[j]:
      intersection.append(left[i])
      i, j = i+1, j+1
    elif left[i] < right[j]:
      i+=1
    else:
      j+=1

  if intersection:
    return ",".join([str(x) for x in intersection])
  else:
    return "false"

# keep this function call here
print(FindIntersection(input()))