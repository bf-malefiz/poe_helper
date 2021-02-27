# A little safety tool for Path of Exile item crafting

*First: This tool only automates checking your clipboard and blocks your input from overrolling. There are no inputs being made to poe-server by this tool.*

This tool takes the iteminfo of the item you are about to roll on and will check if you already hit your desired mod. If so it will kinda block your input by moving the mouse away and report with a sound.

##### starting
- you can either use the provided .exe to simply click and run the program or.. 
- if you want to build it yourself or run it raw make sure you have python3.7+ installed
        - clone the repo

        py -m pip install -r requirements.txt
        py main.py

##### usage
- You need to specify amounts of sections you want to skip (depth) because every Iteminfo has a different amount of sections. On the following Watchstone the Depth is [2] 
I tried to add the respective items to the depths but there are many missing or differ because of implicites. If you notice major mistakes please let me know.

###### Watchstone Clipboard
>Rarity: Magic\
Platinum Tirn's End Watchstone of the Prophet\
-------- [Depth = 1]\
Item Level: 85\
-------- [Depth = 2]\
Unique Bosses have 10.2% chance to drop an additional Silver Coin\
-------- [Depth = 3]\
Only the souls trapped within can bear witness to the Maven's dark proclivities, and they dare not speak up.\
-------- [Depth = 4]\
Socket this into a Citadel on your Atlas to increase the Tier of Maps and reveal hidden Maps in that Citadel's Region. You can only socket one Crimson, Viridian, Cobalt or Golden Watchstone into each Citadel.
>

- at this time the mod you're entering needs to be case-senstive!
- the mod needs to be a full description without numbers
- activate the listener after adding your mods to the list and wait for the beep

###### Examples for Mods
>
- ~~40~~ to maximum Life  
= **to maximum Life**
- Unique Bosses have ~~10%~~ chance to drop an additional Silver Coin 
= **Unique Bosses have chance to drop an additional Silver Coin**
>

![Preview](https://imgur.com/F08yj7n)

## Credits

- [Grinding Gear Games](http://www.grindinggear.com/) for [Path of Exile](https://www.pathofexile.com/).
- [moses-palmer](https://github.com/moses-palmer) for [pynput](https://github.com/moses-palmer/pynput).
- [asweigart](https://github.com/asweigart/) for [pyperclip](https://github.com/asweigart/pyperclip).