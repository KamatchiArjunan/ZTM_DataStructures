# Program to find the longest word in the string
def LongestWord(sen):
  
  list = sen.split(" ")
  max = 0
  longWord = ""
  i = 0
  while (i <len(list)):
    if max < len(list[i]):
      max = len(list[i])
      longWord = list[i]
      i += 1
    else:
      i += 1
  #print(longWord, max)
  return longWord 


str = "I love India"
print(LongestWord(str));
