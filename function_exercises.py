#!/usr/bin/env python
# coding: utf-8

# In[4]:


#1.Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(num):
    return num in ['2', 2]




# In[6]:


#2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(letter):
    return letter.lower() in 'aeiou'




# In[7]:


#3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(halloween):
    return not is_vowel(halloween)
    



# In[10]:


#4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

def capitalize_leading_consonant(word):
    if is_consonant(word[0]):
        return word.capitalize() 
    else:
        return word



# In[15]:


#5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip_percentage,bill_total):
    return bill_total * tip_percentage


# In[17]:


#6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(original_price,discount_percentage):
    return original_price - (original_price * discount_percentage)




# In[21]:


#7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(string_num):
    return int(string_num.replace(",",""))



# In[26]:


#8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(grade_num):
    """Accepts a number representing a students grade and returns the letter grade associated with that number"""
    if grade_num > 88:
        return 'A'
    elif grade_num > 80:
        return 'B'
    elif grade_num > 67:
        return 'C'
    elif grade_num > 60:
        return 'D'
    else:
        return 'F'



# In[37]:


#9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(my_string):   
    """Accepts a string and returns that string with all vowels removed"""
    for char in my_string: 
        if char in 'aeiouAEIOU':
            my_string = my_string.replace(char, '')
    return my_string



# In[35]:


def remove_vowels2 (string):
    """Different approach from my 101 Kaggle, Accepts a string and returns that string with all vowels removed"""
    vowel = set("aeiouAEIOU")# Creating a set of vowels

    for i in vowel:  #takes a letter from vowel set
        string = string.replace(i, '') #removes all char that match the current letter (i) in vowel set
    return string


# In[57]:


#10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
    #anything that is not a valid python identifier should be removed
    #leading and trailing whitespace should be removed
    #everything should be lowercase
    #spaces should be replaced with underscores

def normalize_name(possible_identifier):
    """Accepts a string and returns an altered string that is considered a valid python identifier"""
    
    valid_python_identifier= possible_identifier.strip() #remove leading/trailing whitespace
    
    valid_python_identifier= valid_python_identifier.replace(' ', '_') #Exchange middle spaces for underscores
    
    valid_python_identifier= valid_python_identifier.lower() #enforce lowercase on all letters
    
    while not valid_python_identifier[0].isalpha():
        valid_python_identifier = valid_python_identifier[1:] ##remove non-alphabetical leading char
    
    return valid_python_identifier
        


# In[12]:


#11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

def cumulative_sum(num_list):
    """Takes in a list of numbers and returns a list that is the cumulative sum of the numbers in that list."""
    sum_list=[num_list[0]]
    for i in range(1,len(num_list)):
        #print(i)
        #print("math: ", sum_list[i-1] ,"+", num_list[i] )
        sum_list.append(sum_list[i-1] + num_list[i])
    return sum_list



# In[28]:


#Bonus 1.Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. 

def twelveto24 (time12_string):
    """Takes in a time based on the 12 hour time format, and converts it to the 24 hour time format"""
    
    time12_string = time12_string.lower()
    time24_string =''
    
    if time12_string[-2:] == 'am':
        if time12_string[0:2] == '12':#if midnight replace 12 with 00
            time24_string = '00' + time12_string[2:-2] 
            return time24_string
        
        time24_string = time12_string[:-2] #if not midnight, remove end char and return string
        return time24_string
    
    else:
        if len(time12_string) < len('00:00pm'): #add zero in front for time < 10
            time12_string = '0' + time12_string
        
        if time12_string[0:2] == '12': #if noon, remove end char and return string 
            time24_string = time12_string[:-2]
            return time24_string

        #creating time24_string from scratch, used individual lines for easy reading   
        time24_string = str(int(time12_string[0:2]) + 12)
        time24_string = time24_string + ":"
        time24_string = time24_string + time12_string[3:5] 

    if time24_string[0:2] == '24':
        time24_string = '00' + time24_string[2:]
    return time24_string



# In[38]:


#Bonus 1. Bonus: write a function that does the opposite.

def twentyfourto12(time24):
    """Takes in a time based on the 24 hour time format, and converts it to the 12 hour time format"""

    if time24[0:2] == '00':
        time12= '12' + time24[2:] + 'am'
        return time12
    elif time24[0:2] == '12':
        time12= time24 + 'pm'
        return time12
    elif int(time24[0:2]) > 12: #if after noon, we have some math to do
        time12= str(int(time24[0:2])-12) + time24[2:]+ 'pm'
        return time12
    else:
        return time24 + 'am'


# In[ ]:




