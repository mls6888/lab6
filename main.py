# Author: Michael Sullivan mls6888@psu.edu
# Collaborator: Brian Chette bjc5969@psu.edu
# Collaborator: Ismali Al ABdali ija5135@psu.edu
# Collaborator: Haonan Yan hpy5108@psu.edu
# Section: 11
# Breakout: 11r

def count_non_overlapping(s, substr, start):
  s2=s[start:len(s)]
  i=0
  a=len(substr)
  d=0
  while (i<=(len(s2)-1)):
    b=i+a
    if (substr==s2[i:b]):
      i=i+a
      d=d+1
    else:
      i=i+1
  return d
    

    

  

  """
  Return the number of non-overlapping occurrences of substr in s
  starting from the index start.
  You can not use str method s.count.
  """
  return 0

def count_non_overlapping_m(s, substr, start):
  for i in range (start, len(s)):
   return s.count(substr)
  
  """
  Return the number of non-overlapping occurrences of substr in s
  starting from the index start.
  You must use a one-liner implementation by using s.count().
  """
  return 0

def find_smallest(t1):
  if len(t1)>0:
    return min(t1)
  else:
    return None
  
  """
  Return the smallest element in given list t.
  Return None if t is empty
  """
  

def myfilter(t, cond):
  List2 = []
  for eachItem in t:
   if cond(eachItem):
     List2.append(eachItem)
  return List2

  """
  t is a list, cond(x) is a boolean function that returns True or False
  given an element x in t.
  Return a new list that only includes element x from t such cond(x) is True. 
  """
  

def is_palindrome(s):
  return s[::-1] == s

def is_even(n):
  return n % 2 == 0

def run():
  s = input("Enter a string: ")
  substr = input("Enter a substring to count: ")
  start = int(input("Entera starting index: "))
  c1 = count_non_overlapping(s, substr, start);
  print(f"{substr} occurred in {s} {c1} times starting from index {start}.")
  c2 = count_non_overlapping_m(s, substr, start);
  print(f"{substr} occurred in {s} {c2} times starting from index {start}.")

  print("Testing find_smallest:")
  t1 = [5, 8, 10, 2, 7] 
  print(f"min in {t1} is {find_smallest(t1)}")
  t1 = ["hello", "apple", "banana", "world"]
  print(f"min in {t1} is {find_smallest(t1)}")
  
  print("Testing myfilter:")
  t1 = ["a", "apple", "racecar", "hannah", "banana"]
  print(f"filering {t1} with is_palindrome is {myfilter(t1, is_palindrome)}")
  t2 = list(range(0, 50, 3))
  print(f"filtering {t2} with is_even is {myfilter(t2, is_even)}")
 

if __name__ == "__main__":
  run()