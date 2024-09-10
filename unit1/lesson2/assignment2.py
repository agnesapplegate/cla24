from unit1lesson2 import *
number_list.sort()
#.sort is a python tool to call on an object in your code
print("The smallest number is:", number_list[0])
# answer 175
number_list.sort()
for x in number_list:
    # : means you are about to tell the code you are adding a new loop
    if x > 500:
      # using an "if" statement to ask questions of the code
      print(x)
      #answer is 501
number_list.sort()
even_numbers = []
for num in number_list:
   if num % 2 == 0:
    even_numbers.append(num)
    print (even_numbers[0])
    #answer 176 
word_list.sort()
#sorting my word list - question, can I sort alphabetically in one line of code?
alphabetically_last_word = word_list[0]
for word in word_list:
   if word > alphabetically_last_word:
    alphabetically_last_word = word
    print("The last word (alphabetically) is", alphabetically_last_word)
    # answer violation
longest_word = word_list[0]
for word in word_list:
  if len(word) > len(longest_word):
    longest_word = word
    #using the = tool to assign meaning to the code
    print ("The longest word is", longest_word)
    # answer is recommendation








      

   

   









