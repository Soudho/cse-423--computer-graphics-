# cse-423--computer-graphics-
The code is for a 2D game by using only OPENGL library.Here we have basically implemented the midpoint line algorithm through which we can draw line .
In this lab, students will implement a simple 2D game called “Catch the Diamonds!”.
There will be diamonds falling from the top, your goal is to catch them before they hit the
ground. The more diamonds you catch, the greater you score. But if you miss any of the
diamonds, your game is over. You then have to start over again.

Page 8 of 16

Rules:
● There is a catcher bowl at the bottom of the player screen, which can be moved
horizontally using left and right arrow keys, please make sure the catcher doesn’t get out
of the screen.
● The diamonds fall vertically from the top of the screen. For a diamond to be regarded as
“catched”, the catcher must be right beneath it at the right moment (meaning the catcher
and diamond have to collide with each other). There will be one diamond falling at a time
on the screen.
● If a diamond is “catched”, your score will increase by 1, and the current score should be
printed on the console. After that, a new diamond will start falling from the top. The
color of the diamond will be random. The horizontal position of it will be random as well.
● If a diamond is missed, the game will be over. In this state, the falling diamond will
vanish, no other diamonds will be falling from the screen, you won’t be able to move the
catcher, and the catcher will turn red instead of usual white. In the console, “Game Over”
should be printed including your last score.
● The speed of the diamond falling will gradually increase with time to ramp up the
difficulty.
● There will be 3 clickable buttons on the top of the screen (all drawn using midpoint
lines):
● A bright teal colored button on the left in the shape of a left arrow. Clicking this
will restart the game (no matter if your game is over or not). Your score and
diamond speed will also be reset. A new diamond will also start falling. You can
show a text like “Starting Over” in the console. Don’t forget to revert back the
catcher’s color to its usual one.
● An amber colored button in the middle in the shape of a play or pause icon.
Clicking this will toggle your game’s playing/paused state. The icon will depend
on the state as well. Which is, the pause icon shows when the game is in play
state, and the play icon will show when it’s the opposite. As you can guess, in the
paused state, the falling diamond will freeze, and you won’t be able to move the
catcher.

Page 9 of 16

● A red colored button on the right in the shape of a cross. Clicking this will print
“Goodbye” along with your score in the console, and terminate the application.
● You have to draw everything on screen using the midpoint line drawing algorithm.
With that being said, you’re only allowed to use the GL_POINTS primitive type.
● The size of the diamond won’t be too big. It also shouldn’t be too small that it’s barely
noticeable. Same thing for the catcher’s length, it shouldn’t be too long that it gives the
player an unfair advantage. The shape of the diamond and the catcher should be
exactly what is shown in the figure- diamond with four midpoint lines and catcher
with another four midpoint lines, maintaining the shape shown in the figure.
● As the color of the diamonds are random, the colors should be bright enough so that it
contrasts with the background.
