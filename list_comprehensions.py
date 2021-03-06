{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "03f78b19",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 17 list comprehension problems in python\n",
    "\n",
    "fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']\n",
    "\n",
    "numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]\n",
    "\n",
    "# Example for loop solution to add 1 to each number in the list\n",
    "numbers_plus_one = []\n",
    "for number in numbers:\n",
    "    numbers_plus_one.append(number + 1)\n",
    "\n",
    "# Example of using a list comprehension to create a list of the numbers plus one.\n",
    "numbers_plus_one = [number + 1 for number in numbers]\n",
    "\n",
    "# Example code that creates a list of all of the list of strings in fruits and uppercases every string\n",
    "output = []\n",
    "for fruit in fruits:\n",
    "    output.append(fruit.upper())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "b85f9563",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['MANGO', 'KIWI', 'STRAWBERRY', 'GUAVA', 'PINEAPPLE', 'MANDARIN ORANGE']\n"
     ]
    }
   ],
   "source": [
    "# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]\n",
    "uppercased_fruits = [fruit.upper() for fruit in fruits]\n",
    "print(uppercased_fruits)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "bb842b15",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Mango', 'Kiwi', 'Strawberry', 'Guava', 'Pineapple', 'Mandarin orange']\n"
     ]
    }
   ],
   "source": [
    "# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]\n",
    "capitalized_fruits = []\n",
    "for fruit in fruits:\n",
    "    capitalized_fruits.append(fruit.capitalize()) \n",
    "\n",
    "print(capitalized_fruits)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "23ace73c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Mango', 'Kiwi', 'Strawberry', 'Guava', 'Pineapple', 'Mandarin orange']\n"
     ]
    }
   ],
   "source": [
    "#instructor solution\n",
    "capitalized_fruits = [fruit.capitalize() for fruit in  fruits]\n",
    "print(capitalized_fruits)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "facfa24b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['guava', 'pineapple', 'mandarin orange']\n"
     ]
    }
   ],
   "source": [
    "# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.\n",
    "fruits_with_more_than_two_vowels = []\n",
    "\n",
    "for fruit in fruits:\n",
    "    vowel_count = 0\n",
    "    for letter in fruit:\n",
    "        if letter in 'aeiou':\n",
    "            vowel_count += 1\n",
    "    if vowel_count > 2:\n",
    "        fruits_with_more_than_two_vowels.append(fruit)\n",
    "print(fruits_with_more_than_two_vowels)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "11093721",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['guava', 'pineapple', 'mandarin orange']\n"
     ]
    }
   ],
   "source": [
    "#instructor solution\n",
    "fruits_with_more_than_two_vowels = [fruit for fruit in fruits if len([letter for letter in fruit if letter.lower() in 'aeiou']) > 2]\n",
    "print(fruits_with_more_than_two_vowels)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "439c7c6d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['mango', 'kiwi', 'strawberry']\n"
     ]
    }
   ],
   "source": [
    "# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']\n",
    "fruits_with_only_two_vowels = []\n",
    "\n",
    "for fruit in fruits:\n",
    "    vowel_count = 0\n",
    "    for letter in fruit:\n",
    "        if letter in 'aeiou':\n",
    "            vowel_count += 1\n",
    "    if vowel_count == 2:\n",
    "        fruits_with_only_two_vowels.append(fruit)\n",
    "print(fruits_with_only_two_vowels)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "ef6dceaa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['mango', 'kiwi', 'strawberry']\n"
     ]
    }
   ],
   "source": [
    "#instructor solution\n",
    "fruits_with_more_than_two_vowels = [fruit for fruit in fruits if len([letter for letter in fruit if letter.lower() in 'aeiou']) == 2]\n",
    "print(fruits_with_more_than_two_vowels)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "0b39feb3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['strawberry', 'pineapple', 'mandarin orange']\n"
     ]
    }
   ],
   "source": [
    "# Exercise 5 - make a list that contains each fruit with more than 5 characters\n",
    "big_char_fruit= [fruit for fruit in fruits if len(fruit) > 5 ]\n",
    "print(big_char_fruit)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "35e8ae9d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['mango', 'guava']\n"
     ]
    }
   ],
   "source": [
    "# Exercise 6 - make a list that contains each fruit with exactly 5 characters\n",
    "five_char_fruit= [fruit for fruit in fruits if len(fruit) == 5 ]\n",
    "print(five_char_fruit)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "20cc5bdd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['kiwi']\n"
     ]
    }
   ],
   "source": [
    "# Exercise 7 - Make a list that contains fruits that have less than 5 characters\n",
    "small_char_fruit= [fruit for fruit in fruits if len(fruit) < 5 ]\n",
    "print(small_char_fruit)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "a0deee21",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5, 4, 10, 5, 9, 15]\n"
     ]
    }
   ],
   "source": [
    "# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]\n",
    "\n",
    "fruit_char_count= [len(letters) for letters in fruits]\n",
    "print(fruit_char_count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "303dabf9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['mango', 'strawberry', 'guava', 'pineapple', 'mandarin orange']\n"
     ]
    }
   ],
   "source": [
    "# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter \"a\"\n",
    "fruits_with_letter_a = [fruit for fruit in fruits if len([letter for letter in fruit if letter in 'a']) > 0 ]\n",
    "print(fruits_with_letter_a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "ab3d1ec7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['mango', 'strawberry', 'guava', 'pineapple', 'mandarin orange']\n"
     ]
    }
   ],
   "source": [
    "#instructor solution\n",
    "def contains_a(fruit):\n",
    "    #Returns True or False if the input fruit string contains an a character\n",
    "    return len([letter for letter in fruit if letter == 'a']) > 0\n",
    "\n",
    "fruits_with_letter_a = [fruit for fruit in fruits if contains_a(fruit)]\n",
    "print(fruits_with_letter_a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "5029410b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 6, 8, 10, 256, -8, -4, -2]\n"
     ]
    }
   ],
   "source": [
    "# Exercise 10 - Make a variable named even_numbers that holds only the even numbers \n",
    "even_numbers = [num for num in numbers if num % 2 == 0]\n",
    "print(even_numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "d035316b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3, 5, 7, 9, 11, 13, 17, 19, 23, 5, -9]\n"
     ]
    }
   ],
   "source": [
    "# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers\n",
    "odd_numbers = [num for num in numbers if num % 2 != 0]\n",
    "print(odd_numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "32e0090e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, 5]\n"
     ]
    }
   ],
   "source": [
    "# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers\n",
    "positive_numbers = [num for num in numbers if num >= 0]\n",
    "print(positive_numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "06301855",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[-8, -4, -2, -9]\n"
     ]
    }
   ],
   "source": [
    "# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers\n",
    "negative_numbers = [num for num in numbers if num < 0]\n",
    "print(negative_numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "8d5e9858",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10, 11, 13, 17, 19, 23, 256]\n"
     ]
    }
   ],
   "source": [
    "# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals\n",
    "big_num = [num for num in numbers if len(str(abs(num))) >= 2]\n",
    "print(big_num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "9387a6d1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 169, 289, 361, 529, 65536, 64, 16, 4, 25, 81]\n"
     ]
    }
   ],
   "source": [
    "# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]\n",
    "numbers_squared = [unicorn**2 for unicorn in numbers]\n",
    "print(numbers_squared)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "3322f7c8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[-9]\n"
     ]
    }
   ],
   "source": [
    "# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.\n",
    "odd_negative_numbers = [pumpkin for pumpkin in numbers if pumpkin %2 != 0 and pumpkin < 0]\n",
    "print(odd_negative_numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "89883e74",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 22, 24, 28, 261, -3, 1, 3, 10, -4]\n"
     ]
    }
   ],
   "source": [
    "# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. \n",
    "numbers_plus_5 = [skeletons + 5 for skeletons in numbers]\n",
    "print(numbers_plus_5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "02500f02",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 3, 5, 7, 11, 13, 17, 19, 23, 5]\n"
     ]
    }
   ],
   "source": [
    "# BONUS Make a variable named \"primes\" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.\n",
    "def is_prime(num):\n",
    "    if num > 1:\n",
    "        for i in range(2,num):\n",
    "            if (num % i) == 0:\n",
    "                return False #if found a factor, not prime\n",
    "        return True #if greater than 1 and not factors, then prime\n",
    "    return False #if not greater than one, not prime\n",
    "\n",
    "primes= [unicorn for unicorn in numbers if is_prime(unicorn)]\n",
    "print(primes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d40d96d0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
