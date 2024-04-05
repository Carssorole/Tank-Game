# Jordan's Sprint 5 Documentation

### Sprint 4 Review
Sprint 4 consisted of creating a Wall class and implementing it in main. First, I created a .tmx file using "Tiled" that basically just consisted of a bunch of tiles organized into the wall structure shown in main. Each tile contains an integer called 'solid' that is <br>
set to 1, indicating that the walls are solid. (An integer was used instead of a boolean as some issues with booleans may exist in Tiled.) The Pytmx library was then imported into the tank program and utilized to incorporate the tilemap. At first, the "y" coordinates <br>
were inconsistent with what was shown on the screen. For example, some areas that the wall appeared could be driven through and some areas that no wall was shown would block the tank. After adjusting the "y" coordinates to account for the scoreboard, the walls began <br>
to work as intended. In main, logic needed to be implemented so that the tanks could not drive through walls and so they functioned as expected. I did not implement logic to prevent the tanks from driving over each other.

### Sprint 5 Goals
For Sprint 5, my goal is to create a simple start screen. Basically, the screen will just show up prior to play and give the user the option to either start the game or exit the program. If time permits, I hope to implement logic to prevent the tanks from colliding <br>
with one another. However, like last sprint, this will be a secondary priority.

