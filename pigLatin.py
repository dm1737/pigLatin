#These functions use python 3.8 standard library
import string

#This function is used to remove punctuation from a string
#Input for this function is any string
#Output for this function is input string with punctuation removed
def removePunc(word):
    removed = ""
    #Iterate through the characters in the string
    for c in word:
        #Ensure character is not punctuation
        if c not in string.punctuation:
            #If character is not punctuation add to result string named removed
            removed += c
    #Return string with punctuation removed
    return removed

#This function is used to translate sentences from english to pig latin, while leaving numbers and punctuation intact
#The input for this function is any string (may work with languages other than english, but this was not tested)
#The output for this function is the pig latin version of the input string
def pigLatin(sentence):
    #Seperate the words in the input sentence into a list
    words = sentence.split()
    punc = False
    num = False
    for j in range(len(words)):
        k = words[j]
        x = []
        y = ""
        #Iterate through the characters of each word to check for punctuation
        for i in range(len(k)):
            if k[i] in string.punctuation:
                if i == len(k) - 1:
                    #If the punctuation is the last character in the string, store it to use later
                    x.append(k[i])
                    punc = True
                elif i < (len(k) - 1):
                    if k[i + 1] in string.punctuation:
                        #If there are multiple punctuation marks in a row (?!) this will check and store them for later use
                        x.append(k[i])
                    elif k[i + 1].isnumeric():
                        #Tracks if punctuation is found in the middle of a number (1,000)
                        num = True
                    elif i > 0:
                        #Tracks if punctuation is found at the beginning of a number (.01)
                        if k[i - 1].isnumeric():
                            num = True
        if punc:
            if num == False:
                #If punctuation was found in a word, remove it for the letter switching process
                k = removePunc(k)
                #Check if word is numeric
                if k.isnumeric():
                    #Iterate through punctuation list and concatenate to add back on to string
                    for z in x:
                        y = y + z
                    #Keep numbers and punctuation intact
                    words[j] = k + y
                else:
                    #Iterate through punctuation list and concatenate to add back on to string
                    for z in x:
                        y = y + z
                    #Append first letter to end of word, add 'ay' and punctuation
                    words[j] = k[1:] + k[0] + 'ay' + y
        elif num:
            #Punctuation in middle, but is numeric, do not alter
            words[j] = k 
        elif k.isnumeric():
            #No punctuation, but is numeric, do not alter
            words[j] = k
        else:
            #No punctuation, non-numeric so append first letter to end of word, add 'ay' 
            words[j] = k[1:] + k[0] + 'ay'
        punc = False
        num = False
    #Use join function with spacing to reconstruct and return pig latin sentence(s)
    return ' '.join(words)