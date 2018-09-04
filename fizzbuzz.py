def fizzbuzz ():
 list_items = [1,2,3,4,5,6,7,8,9,10]
 list_items2= []
 list3 = list_items + list_items2
 x=len(list3)
 
 if x % 3 == 0 and x % 5 == 0:
  print ("fizzbuzz")

 elif x % 5== 0:
  print ("buzz")

 elif x % 3 == 0:
  print ("fizz")

 else:
  print ("x")



fizzbuzz()






