import numpy as np
def valid_row(arr):
  for k in range(9):
    #checking wheather it is in range of 0-9
    if arr[k] not in range(0,10):
      return -1
    else: #checking for repeated values
      if arr[k]!=0:
        if arr[k] in arr[k+1:10]:
          return -1
          
def valid_col(arr,i):
  l=[]
  for k in range(9):
    #checking wheather it is in range of 0-9
    if arr[k][i] not in range(0,10):
      return -1
    else: #checking for repeated values
      if arr[k][i]!=0:
        l.append(arr[k][i])
  if len(l) != len(set(l)):
    return -1
          