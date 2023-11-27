# 6.3-Sort-Pop-and-No-Owls
## Sort and Pop  

Create a function,sort_and_pop(), that take a list as an argument. It shoudl sort the list and remove the first and last element in the list. The function will return the modified list.

**EXAMPLE**
Function Call:
```python
sort_and_clip([10, 5, 3, 8, 12, 4, 2]) 
``` 
Output:
```
[3, 4, 5, 8, 10]
```

## Outliers
Make a new function outliers() that takes a list, min and max values as arguments. The function should remove any items less than the min value and any values greater than the max value. (*hint: you can do this by still only popping the first and last value of the list, you may just need to do it multiple times*)


**EXAMPLE**
Function Call:
```
nums = [10, 4, 8, 7, 12, 15, -1, -8]
min = 0
max = 10
outliers(nums, min, max) 
```
Output:
```
[4, 7, 8]
```
**Extra Challenge** Do this without loops. You'll make use of .append() and .index() and slice the list instead of using .pop() )

## No Owls
You have a friend who REALLY likes owls, and likes to talk about them a lot. However, you hate reading the word owl so you decide to create a funcion that will replace the letters 'owl' with "bird".

** This function, owl(), will take in a list of words. It will traverse the list and replace 'owl' with 'bird' in any word it aprears in and return the updated list. ** 

note: this will create some funny words like hbird instead of howl. this is expected.
