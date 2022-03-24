#we would like to “rotate” a list, or move elements forward in a list by a number of spaces, k.

def rotate(my_list, num_rotations):
  rotated_list = [None for i in range(len(my_list))]
  
  if (num_rotations < len(my_list)):
    leng = len(my_list) - num_rotations
    for i in range(len(my_list)):
      #print(i)
      if i < leng:
        rotated_list[i+num_rotations] = my_list[i]
      else:
        rotated_list[i+num_rotations - len(my_list)] = my_list[i]  

  return rotated_list

#print(rotate([2,3,4,5,6], 3))

# given a sorted list rotated k times, return the index where the “unrotated” list would begin.
#another_rotated_list = [13, 8, 9, 10, 11] 
#rotation_point(rotated_list)
# index 1
# a sorted list would start with 8

""" def rotation_point(rotated_list):


  low = 0
  high = len(rotated_list) - 1
  while low<=high:
      mid = (low + high) // 2
      mid_next = (mid + 1) % len(ro)
    if (mid_val < rotated_list[mid_idx+1]) and (mid_val < rotated_list[mid_idx-1]):
        return mid_idx
  if (mid_val < rotated_list[mid_idx+1]) and (mid_val > rotated_list[mid_idx-1]):
    left_half = rotated_list[:mid_idx]
    return rotation_point(left_half)
  if (mid_val < rotated_list[mid_idx+1]) and (mid_val > rotated_list[mid_idx-1]):
    right_half = sorted_list[mid_idx + 1:]
    result = binary_search(right_half, target)
    if result == "value not found":
      return result
    return (result + mid_idx + 1) """
#print(rotation_point([11,8,9,11,12]))

def remove_duplicates(dupe_list):
    temp_list = []
    for i in dupe_list:
        if i not in temp_list:
            temp_list.append(i)
    return temp_list


print(remove_duplicates([4,5,5,6,6,6,7]))
