user_input = input("Enter name of your file in : ")
file = open(user_input, 'w')
text = input("Type a text : ")
text = text.casefold()
file.write(text)
file.close()

#Code to count the number of tokens
def countTokens():
    file = open(user_input, 'r')
    data = file.read()
    words = data.split()
    print('\nNumber of words in text file',",",user_input," :",len(words))

def convert(lst):
    return ''.join(lst).split()        
lst = (text)
convert(lst)

countTokens()

#code to calculate frequency of tokend
def countToken():
    lst_1 = convert(lst)
    x = []
    res = dict ()
    for i in lst_1:
        x.append(i.lower())
    a = list(set(x))
    for i in a:
            res[i] = x.count(i)
    print("\nFrequencies")       
    print(str(dict(res))) 
    
countToken()

new_list = convert(lst)

#defining normalised frequency
def normalisedFrequency():
      import random
      file = open(user_input, 'r')
      data = file.read()
      words = data.split()
      user_Token = input("\nEnter a Token to check it's normalised frequency : ")
      user_Token = user_Token.casefold()
      times = len(words)
      count = 0
      while times > 0:
          choice = random.choice(new_list)
          if choice== user_Token:
              count+=1
          else:
              count+=0   
          times-=1
          new_list.remove(choice)
      count
      #Formula for Normalised Frequency
      #n.ftoken = tokenCount/totalNumbersOfTokens
      norm_freq = count/len(words)
      print("\nNorminalised frequency for token","'",user_Token,"'","is",norm_freq)

normalisedFrequency()               
          
     
