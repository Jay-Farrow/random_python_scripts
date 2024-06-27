# Task: Create a treasure island game, which ask the user to input a decision for a particular situation. 

print('''

                                                   .       .
                                                    \     /
                                                 ._  '   '  _.
                                                   '  o@o  '
                                                     o@@@o
                                                 .-'  o@o  '-.
                                                     .   .
                                                    /     \
                                                   .       .

                             'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            /ssssssss.
                      /sssssssSSSSssssssssss.
        /\         /sssssSSSSSSSSSSSSSSSssssssssssss.                  
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ''')
 
print("Welcome to East Blue! \nYour mission to find a map to the Grand Line.")
print("You set out on your journey by boat. The boat begins to sink.\nDo you jump inside a barrell or swim to stay afloat? Type Barrell or Swim.")
choice_1 = str.lower(input())

if choice_1 == 'swim':
    print("\nGame over! You drowned.")
else:
    print("\nYou Survived and get picked up by another passing ship.\n")

print("You get outside the barrell and realize your on a pirate ship. \nDo you fight for your life or sneak to find a dingy boat? Type Fight or Sneak.")
choice_2 = str.lower(input())

if choice_2 == 'sneak':
    print("\nYou are able to make it to the dingy and set sail. Soon after a sea creature attacks your boat. \nGame over! You drowned.")
else:
    print("\nYou defeat the captain. The crew makes you the new captain. You set sail for a navy base to find a map of the grand line.\n")
    
print("You get to the navy base and order your crew to attack the base. During the attack as captain you infiltrate the navy base to find the map.\nYou come across three colored doors. Which door do you open? Type Green, Red, or Yellow?")
choice_3 = str.lower(input())

if choice_3 == 'red':
    print("You fall into a pool of water. Game over! You drowned.")
elif choice_3 == 'green':
    print("You fall into a pool of water. Game over! You drowned.")
else:
    print("You find the map to the grand line. You Win!!!")