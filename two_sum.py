list1=[3,2,4]
list2=[2,3,5,1]
len1=len(list1)
len2=len(list2)
target=6
ans=[]
for i in range(len1):
  for j in range(i+1,len1):
    if(list1[i]+list1[j]==target):
      ans.append(i)
      ans.append(j)
print(ans)
      
    
