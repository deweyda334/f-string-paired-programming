# Dax Dewey
# Sep 10
# f-String Greeting Card 

'''
Directions:

1. Update the comment block at the top of this script.

2. Use the Python `input( )` function to prompt (ask) the user for three pieces of information for a greeting card you're making:

     - the first name of the person the greeting card is for
     - the occasion (e.g., birthday, graduation, etc.)
     - the custom message 

3. Assign each piece of information collected to a variable with a short, specific name.

4. Use the `print( )` function  and an f-string to display your personalized greeting card on the screen.

6. Execute (run) your script in Visual Studio Code and correct any errors.
'''

first_name = input ("what is their first name for the greeting card. \n")
occasion = input ("what is the occasion. \n")
custom = input ("what is the custom message. \n")

print(f"{first_name} is having a(n) {occasion} party this weekend! {custom}, {first_name}!")
