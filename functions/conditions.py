def print_numbers(n):
    numbers = range(n)
    for number in numbers:
        print(number)
        
# IF STATEMENT

def print_odd_numbers(n):
    numbers = range(n)
    for number in numbers:
        if number % 2 != 0:
            print(number)
    
    

def print_even_numbers(n):
    numbers = range(n)
    for number in numbers:
        if number % 2 == 0:
            print(number)   
            
            
def check_odd_or_even(n):
    numbers = range(n)
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is not even")    
            

# ELIF STATEMENT
 
def check_divisibility(n):
    numbers = range(n)
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is divisible by 2")
        elif number % 3 == 0:
            print(f"{number} is divisible by 3")   
        elif number % 5 == 0:
            print(f"{number} is divisible by 5")  
        else:
            print(f"{number} is not divisible by 2, 3 or 5")      
                     
            
# FAMOUS FIZZBUZZ

def fizz_buzz(n):
    numbers = range(n)
    for number in numbers:
        if number % 3 != 0 and number % 5 != 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")   
        elif number % 5 == 0:
            print("buzz")  
        else:
            print(f"{number} is not divisible by 3 and 5")    
            
 
# THE WHILE LOOP 
 
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
        
        
#THE BREAK STATEMENT 
        
def countdown_to_five(n):
    while n > 0:
        print(n)
        if n == 5:
            break
        n -= 1        
        
        
#CONTINUE STATEMENT

def divisible_by_seven(n):
    x = 0
    while(x <= n):
        x += 1
        if(x % 7 != 0):
            continue
        print(f"{x} is divisible by 7")
        
      
  
def print_odds(n):
    i = 0
    while(i < n):
        i += 1
        if(i % 2 == 0):
            continue
        print(i)