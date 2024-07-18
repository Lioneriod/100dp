import os
clear = lambda: os.system('cls')

print(r'''          .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'          `98v8P'          `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             \n
''')
print("Welcome to the Death Island!\n\nHow to play:\n\nYou will need to choose your own path before the undead trials.\n\nBeware your own choices, for those who can't decide are fated to \ngreat suffering...\n")

print('Arriving by boat, you finally have reached the Death Island, in \nwhich a forbidden grimoire is located.\n')

firstRoute = input('Your objective is to find it.\nWhich route will you take? (type "cave" or "forest")\n')

if firstRoute == "cave":
  clear()
  print(r'''                ;`',                           
                `,  `,                         
                 ',   ;   ,,-""==..,           
                  \    ','          \          
          ,-""'-., ;    '    __.-="-.;         
        ," ,,_    "V      _."                  
       ;,'   ''-,          "=--,_              
              ,-''    _  _       `,            
             /   ,.-+( )( )�--.,   ;           
            ,'  /   | (_)  |    `\ ,           
            ; ,/     `-.--'       ;            
            !,'       | |                      
            V'        | |                      
                   .-`  '--.                   
                  (_/\__  , \                  
                  L_____`    >                 
                    |`-----'\                  
                    |      \_)                 
                 ___|   .  (                   
                 \   `---._`_/\                
                  /       /   |                
                 <        )   \                
                  |     ..     \               
                 /   \ /  \     `-.            
                /     \   /       /           
               /      /   \,     \              
              `_.----'     \_____ \__          
              /   \           L______]         
              \___|           ''')
  print('\nYou are confronted by the coconut man, from the coconut fruit!')
  print('''\n"WHAT ARE YOU DOING HERE MY MAN?? DO YOU EVEN KNOW THAT THE \ncoconut nut is a delicious nut but it isn't a nut it's the \ncoconut fruit??"''')
  print('''\nLooking around you see a lot of coconuts, and a hole on the \nground that leads into deep waters.\n''')
  firstRouteA = input('What do you do? Enter the hole or prove your coconut friendship?\n(type "hole" or "coconut")\n')
  if firstRouteA == "hole":
    clear()
    print('\nSubmerging inside the hole, you find an orca!\n')
    print(r'''    ~                           ~              ~
       ~~~~     ~          ~~ ~        ~      ~    ~~    
  ~~             _,-''-.     ~~        .-._       ~  ~~~
            ,---':::::::\`.            \_::`.,...__    ~ 
     ~     |::`.:::::::::::`.       ~    )::::::.--'       
           |:_:::`.::::::::::`-.__~____,'::::(        
 ~~~~       \```-:::`-.o:::::::::\:::::::::~::\       ~~~
             )` `` `.::::::::::::|:~~:::::::::|      ~   ~~
 ~~        ,',' ` `` \::::::::,-/:_:::::::~~:/           
         ,','/` ,' ` `\::::::|,'   `::~~::::/  ~~        ~
~       ( (  \_ __,.-' \:-:,-'.__.-':::::::'  ~    ~   
    ~    \`---''   __..--' `:::~::::::_:-'               
          `------''      ~~  \::~~:::'               
       ~~   `--..__  ~   ~   |::_:-'                    ~~~
   ~ ~~     /:,'   `''---.,--':::\          ~~       ~~
  ~         ``           (:::::::|  ~~~            ~~    ~
~~      ~~             ~  \:~~~:::             ~       ~~~
             ~     ~~~     \:::~::          ~~~     ~
    ~~ jrei      ~~    ~~~  ::::::                     ~~
          ~~~                \::::   ~~
                       ~   ~~ `--\n''')
    print('Talking through magical powers, she tells you about a special \nnecklace, which will help you in your adventure!')
    secondRouteA = input('Will you accept the necklace?(type "yes" or "no"\n')
    if secondRouteA == "yes":
      print(r'''\`._`--','    )   o `.    <       :     \  ( ( ,. \  \\
\\\  `-,'     /  ,-.___`-.  :      |      \  \ `' ) )  \
\\     |      |  `-.   `-'  |     ,'-._   \`._`--','    )   o
 \     :       >    `. o   (    ,',--. `.\\\  `-,'     /  ,-.
  )   o `.    <       :     \  ( ( ,. \  \\     |      |  `-.
 /  ,-.___`-.  :      |      \  \ `' ) )  \     :       >
 |  `-.   `-'  |     ,'-._   \`._`--','    )   o `.    <
  >    `. o   (    ,',--. `.\\\  `-,'     /  ,-.___`-.  :
 <       :     \  ( ( ,. \  \\     |      |  `-.   `-'  |
  :      |      \  \ `' ) )  \     :       >    `. o   (    ,
  |     ,'-._   \`._`--','    )   o `.    <       :     \  (
 (    ,',--. `.\\\  `-,'     /  ,-.___`-.  :      |      \  \
  \  ( ( ,. \  \\     |      |  `-.   `-'  |     ,'-._   \`._
   \  \ `' ) )  \     :       >    `. o   (    ,',--. `.\\\
   \`._`--','    )   o `.    <       :     \  ( ( ,. \  \\
`.\\\  `-,'     /  ,-.___`-.  :      |      \  \ `' ) )  \
  \\     |      |  `-.   `-'  |     ,'-._   \`._`--','    )
)  \     :       >    `. o   (    ,',--. `.\\\  `-,'     /  ,
    )   o `.    <       :     \  ( ( ,. \  \\     |      |  `
   /  ,-.___`-.  :      |      \  \ `' ) )  \     :       >
   |  `-.   `-'  |     ,'-._   \`._`--','    )   o `.    <
    >    `. o   (    ,',--. `.\\\  `-,'     /  ,-.___`-.  :
   <       :     \  ( ( ,. \  \\     |      |  `-.   `-'  |
-.  :      |      \  \ `' ) )  \     :       >    `. o   (
-'  |     ,'-._   \`._`--','    )   o `.    <       :     \
   (    ,',--. `.\\\  `-,'     /  ,-.___`-.  :      |      \
    \  ( ( ,. \  \\     |      |  `-.   `-'  |     ,'-._   \`
     \  \ `' ) )  \     :       >    `. o   (    ,',--. `.\\\
._   \`._`--','    )   o `.    <       :     \  ( ( ,. \  \\
. `.\\\  `-,'     /  ,-.___`-.  :      |      \  \ `' ) )  \
 \  \\     |      |  `-.   `-'  |     ,'-._   \`._`--','    )
) )  \     :       >    `. o   (    ,',--. `.\\\  `-,''')
      print("\nThe sea magic does it's effects and you turn into a orca. Enjoy your new life at the sea destroying anything in your path.\n")
      print('GAME OVER, ORCA ENDING.')
    else:
      print('The orca ate your existence away')
      print('GAME OVER, VORE ENDING')
  else:
    print("\nIT'S COCONUT EATING TIME LET'S GOOOOOOOOO\n")
    print('GAME OVER, COCONUT ENDING')
else:
  print(r'''"""::MM::===:::==="""==///==="""===:::==="""===::::===""""===:::===""""
     ::        ,-,       ::
     ::       :o~o:      ::    	
      ::.___.-:(O):--..-::;
       "=___   '='   ,..-"
            :-,    ' :__
            \  \     /  :
             \  :. .:,__:
==ltb:::::==="MM"===::MM=="""===::::===""""===:::===""""''')
  print('''\nAs you enter the forest, you soon spot a quite friendly orangutan''')
  print("\nShe extends her arm towards you, offering a fruit. What do you do?")
  firstRouteB = input('\nAre you a understander or an eater? Will you understand the froot or eat the fruuit?(type "understand" or "eat")\n')
  if firstRouteB == "understand":
    print(r'''              ._                                            ,
               (`)..                                    ,.-')
                (',.)-..                            ,.-(..`)
                 (,.' ,.)-..                    ,.-(. `.. )
                  (,.' ..' .)-..            ,.-( `.. `.. )
                   (,.' ,.'  ..')-.     ,.-( `. `.. `.. )
                    (,.'  ,.' ,.'  )-.-('   `. `.. `.. )
                     ( ,.' ,.'    _== ==_     `.. `.. )
                      ( ,.'   _==' ~  ~  `==_    `.. )
                       \  _=='   ----..----  `==_   )
                    ,.-:    ,----___.  .___----.    -..
                ,.-'   (   _--====_  \/  _====--_   )  `-..
            ,.-'   .__.'`.  `-_I0_-'    `-_0I_-'  .'`.__.  `-..
        ,.-'.'   .'      (          |  |          )      `.   `.-..
    ,.-'    :    `___--- '`.__.    / __ \    .__.' `---___'    :   `-..
  -'_________`-____________'__ \  (O)  (O)  / __`____________-'________`-
                              \ . _  __  _ . /
                               \ `V-'  `-V' |
                                | \ \ | /  /
                                 V \ ~| ~/V
                                  |  \  /|
                                   \~ | V             
                                    \  |
                                     VV\n
    ''')
    print('\nBy understanding the fruit you understand the true value and meaning of this universe: \nNone. \nTherefore your meaning and existence are pulverized by this realization.\n')
    print('\nGAME OVER, FRUIT ENDING')
  else:
    print(r'''      ^  ^  ^   ^      ___I_      ^  ^   ^  ^  ^   ^  ^
    /|\/|\/|\ /|\    /\-_--\    /|\/|\ /|\/|\/|\ /|\/|/
    /|\/|\/|\ /|\   /  \_-__\   /|\/|\ /|\/|\/|\ /|\/|/
    /|\/|\/|\ /|\   |[]| [] |   /|\/|\ /|\/|\/|\ /|\/|\/''')
    print('\nYou find yourself in a beautiful little glade, like the fruit guided you\n')
    print('\nAs you look around, you find a horse just horsing around. Which way do you go?\n')
    secondRouteB = input('Do you enter the cabin or go towards the horse?(type "cabin" or "horse"\n')
    if secondRouteB == "cabin":
      print(r'''            /;
           / |'-,.
          /  '    `"---,.__
         /  '    ,'     ,  '"--,"|
        /  '    ,     ,'     ,"::|
       /  '   ,'    ,      ,"::::|
      /  '   ,    ,'     ,"::::::L
     /  '  ,'   ,'     ,"::::::::L
    /  '  ,    ,     ,":::::::::J
    k-,._    ,'   _.":::::::::::J
     \.  `"----'"".J::::::::::::|
      \.    .-,    .L:::::::::::|
       \.  (       .J:::::::::::!
        \.  `--     .L:::::::::/
         \.   .-.   .|::::::::/
          \. (   )  .J:::::::/
           \. `-'    .L:::::/
            \.  L    .|::::/
             \. !__  .J:::/
              \.  __  .L:/
               \. L_) .|/
                `-,__,-'   \n''')
      print('You did it! You find the forbidden book! Thanks to your actions, \nnow the anti-christ can be born from your blood and reign over \nmankind for ten thousand years in agony and suffering! \nYIPEEEEEEEEE\n')
      print('\nGAME OVER, GOOD ENDING')
    else:
      print(r'''\n  (\w/)
        (00\                                     
       _/  )  \______
      (oo /'\        )`,
       `--' (v  __( / ||
             |||  ||| ||
            //_| //_|  \n
            Oh nyoo!!! You stawtled the cute lile howsie!!\n''')
      print('He was so scared that he ended up farting a bit loud.')
      print("The horsie looks at you wishing that you didn't hear it.")
      secondChoiceC = input('\nAre you gonna be a honest friend and tell him, or let it go? (type "tell" or "not tell")\n')
      if secondChoiceC == "tell":
        print("\nEven though you are a good friend, you shouldn't tell others that they farted!\n")
        print(r'''                                              ,--,  ,.-.
                ,                   \,       '-,-`,'-.' | ._
               /|           \    ,   |\         }  )/  / `-,',
               [ '          |\  /|   | |        /  \|  |/`  ,`
               | |       ,.`  `,` `, | |  _,...(   (      _',
               \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L\
                \  \_\,``,   ` , ,  /  |         )         _,/
                 \  '  `  ,_ _`_,-,<._.<        /         /
                  ', `>.,`  `  `   ,., |_      |         /
                    \/`  `,   `   ,`  | /__,.-`    _,   `\
                -,-..\  _  \  `  /  ,  / `._) _,-\`       \
                 \_,,.) /\    ` /  / ) (-,, ``    ,        |
                ,` )  | \_\       '-`  |  `(               \
               /  /```(   , --, ,' \   |`<`    ,            |
              /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
        ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
       (-, \           ) \ ('_.-._)/ /,`    /
       | /  `          `/ \\ V   V, /`     /
    ,--\(        ,     <_/`\\     ||      /
   (   ,``-     \/|         \-A.A-`|     /
  ,>,_ )_,..(    )\          -,,_-`  _--`
 (_ \|`   _,/_  /  \_            ,--`
  \( `   <.,../`     `-.._   _,-`
   `                      ```''')
        print('\nFor your inconsideration, Beelzebub himself came for your soul, \npulling your feet towards eternal despair and suffering for this \nfat snitcher\n')
        print('\nGAME OVER, FART SNITCHER ENDING')
      else:
        print('\nBy not telling the horsie, you saved his self-steem, but the potency of diabolic fart killed you\n')
        print('\nGAME OVER, FART SMELLER ENDING')