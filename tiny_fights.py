"""
    doc comment for things
"""
class WarriorOptions:
    """
        Warrior type, good and bad
    """
    def __init__(self, title: str, weapon: str, health: int, magic: int, abilities: str) -> None:
        """
            define init parameters
        """
        self.valid_titles: list[str] =[
        "wizard", "waffle house employee", "toddler", "rogue" 
        ]

        self.title = title
        self.weapon = weapon #call to weapon class instead
        self.health = health
        self.magic = magic
        self.abilities = abilities #calls to ability class instead
        #method for printing
        #weapons class having an adding method?

def weapon_slecect_menu() -> None:
    """
        This function is for the weapon selection menu.
    """
    print("step threeeeeeee")

def character_select_menu() -> str:
    """
        This function prints the character selection. 
    """
    while True:
        menu_cs_text: str = "available warriors: wizard, waffle house employee, toddler, rogue"
        print(menu_cs_text)
        menuinput: str = input("Choose your Fighter. Enter Fighter type or \"Exit\"\n-> ").upper()
        inputcheck: list = ["WIZ", "WAF", "TO", "RO", "EX"] #checking substrings for higher chance of getting right thing
        character: str = "" #temporary variable
        try: #first layer of input validation
            if any((substring in menuinput for substring in inputcheck)) is False:
                raise ValueError
            if "EX" in menuinput: #exits program
                leave_y = input("Do you really want to leave? Type \"Y\" if so or anything else to continue.\n-> ")
                if leave_y == "Y":
                    print(".\n.\n.\nExiting Arena.")
                    exit()
            elif "WIZ" or "WAF" or "TO" or "RO" in menuinput: #continues with char select
                character = menuinput
                confirm_y = input(f"Is {character} the Fighter you want? Enter Y/N\n-> ") #or confirm
                if confirm_y == "Y":
                    weapon_slecect_menu()
                    break
                #else:
                    #kick back to prev option
            else: #this is for wrong inputs not caught
                print("You weren't supposed to see this.\n")
                raise KeyError
        except ValueError:
            print("Select a valid option.\n")
        return character

#Exiting back to larger loop which is ->

def menu_screen() -> None:
    """
        This function prints the main menu screen as well as handles all validations required from the user.
    """
    menu_text: str = "play, exit"
    print(menu_text)
    while True:
        menuinput: str = input("How do you want to proceed? Type \"Play\" or \"Exit\"\n-> ").upper()
        inputcheck: list = ["PL", "EX"] #checking substrings for higher chance of getting right thing
        try: #first layer of input validation
            if any((substring in menuinput for substring in inputcheck)) is False:
                raise ValueError
            if "PL" in menuinput: #play
                character_select_menu()
                break
            elif "EX" in menuinput: #exits program
                leave_y = input("Are you really choosing the option of cowardice? Type \"Y\" if you are paralyzed by fear, or proceed with any other input\n-> ")
                if leave_y == "Y":
                    print("The art of violent confrontation is not for the meek.")
                    print(".\n.\n.\nExiting Arena.")
                    exit()
            else: #this is for wrong inputs not caught
                print("You weren't supposed to see this.\n")
                raise KeyError
        except ValueError:
            print("Select a valid option.\n")
        except KeyError:
            exit()
    return None

if __name__ == '__main__':
    menu_screen()
