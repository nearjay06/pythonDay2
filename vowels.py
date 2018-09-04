list_vowels = ['a', 'e', 'i', 'o', 'u']

new_list = []



def countVowels(string):
   for letter in string:
      if letter in list_vowels:
         new_list.append(letter) 
   new_list.append(len(new_list))
   print(new_list)
    

countVowels('banana')
     
















 