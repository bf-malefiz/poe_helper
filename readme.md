# A little safety tool for Path of Exile item crafting

        This tool only automates checking your clipboard and blocks your input from overrolling.
        There are no inputs being made to poe-server by this tool. This tool is not an autoscroller. 
        You will still experience the pain of rolling thousand of alts GGG intended you to roll

This tool takes the iteminfo of the item you are about to roll on and will check if you already hit your desired mod. If so it will kinda block your input by moving the mouse away and report with a sound. I prefer to move the mouse away instead of blocking it, so I'm still able to use it.

##### starting
- you can either use the provided .exe to simply click and run the program or.. 
- if you want to build it yourself:
        - have python3.7+ installed
        - clone the repo
        - install required libaries and execute main via console

        py -m pip install -r requirements.txt
        py main.py

##### usage
- at this time the mod you're entering needs to be case-senstive!
        *Tip: copy the mod from [poe.db](http://poe.db)*
- the mod needs to be a full description without numbers
- activate the listener after adding your mods to the list and start rolling
- if your mod doesn't have a value just leave it empty, those mods will be taged (raw) in modlist
any occurence will trigger the block

###### Examples for Mod by removing their numbers
>
- ~~40~~ to maximum Life  = **to maximum Life**
- Unique Bosses have ~~10%~~ chance to drop an additional Silver Coin = **Unique Bosses have chance to drop an additional Silver Coin**
>

![Preview](https://i.imgur.com/Z90yRH9.png)

## Credits

- [Grinding Gear Games](http://www.grindinggear.com/) for [Path of Exile](https://www.pathofexile.com/).
- [moses-palmer](https://github.com/moses-palmer) for [pynput](https://github.com/moses-palmer/pynput).
- [asweigart](https://github.com/asweigart/) for [pyperclip](https://github.com/asweigart/pyperclip).
