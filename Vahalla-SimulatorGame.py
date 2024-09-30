print('''
*******************************************************************************
                                          zee.
        z**=.                                  .P"  $
         %   ^c                               z"   $
          b    %                             d    4"
          4     $            ....           4"    $
           F     L       .P"       "%.      $     $
           $     4     e"             "c    "     $
           $      F  z"                 *  4      $
           P      $ d                    3.$      $
           %      $d       ..eeeec..      *$      'b
          d       $%   .e$*c d" ".z**$%.   $       $
          F       $  e" $   *F   $   ^F.db.$        b
         J        $d\" ^$   4b   $    $  3/$        *
         $        $*$   $c  P *P" * ."F  .$$         b
        4F        $ $c .EeP""      ^C$$..*F F        $
        J         $ $.*"-"*.      ."    "b$ F        'r
        $         *"$   zc. ..  -"..-""\  $$%         $
        $          $      ..  L P  ebe    4$          $
        $          ^F   d%*$J%3 $ *$* "   4F          $
        *          4b       @   3 ^r      4$          $
        4          d$.          4         $3.        4F
         L         $$*.                  %$ $        J
         $        d $ $      -   ^.     P $c $       $
          r      z".$L L    .$%..*$    J  $P. *.    d
          "     z" P$$ ^%  z"      ".  L d$$"c "e  z%
           *  .P .*$$$  "*"   .$c        $$$$.b  ^$"
            *$  dL$$$$r ^4. ./" ""%..r"  $$$$$$J$e"
             *$b$$$$$$F        ""        $$$$$$$P
              ^$$$$$$$$                  $$$$$"
                 "*$$$$                  $"
                      '                 4
                       *  $         .$  F
                        % 4F       .$  "
                          *$%     .$dr
                            *.    .*
                              ".."      
*******************************************************************************
''')
print("Welcome to Your Spirit's Journey.")
print("Your mission is to reach Vallhala, to have a good afterlife.")

choice1 = input('You see two doors. Do you want to go left or right. Type "left" or "right".\n')
if choice1 == "right":
  choice2 = input('You see from afar a ferry coming towards you, do you wait for the man with the lantern or do you run across without him? Type "wait" to wait for the man. Type "run" to run across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the destination unharmed. There is a house with 3 doors. One black, one white and one red. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("You/'ve entered a room with fire'. Game Over.")
    elif choice3 == "white":
      print("You found Vallhala! You Win!")
    elif choice3 == "black":
      print("You enter with Hel. You are not going to Valhalla Game Over.")
    else:
      print("You chose a door that doesn't exist. Your stuck in limbo. Game Over.")
  else:
    print("You get taken to Nieflheim. Game Over.")
else:
  print("You fell into a hole and are now in Neiflheim. Game Over.")
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload


