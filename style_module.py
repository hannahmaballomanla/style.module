'''
==========================================

Stylized Text & Your Layout Engine (STYLE)

==========================================

This module contains functions to format text output in the terminal with ANSI escape codes for colors and styles.
It includes functions for coloring text, creating headers and subheaders, and clearing the terminal screen. 

Note: MainMenuFormat, defaultSubheader, and modifiedSubheader are only that ones that directly prints out values. the rest just returns values so you need to call print(style.function_name()) to see the output.

===========================================

The functions include:

- textColor_reset: Resets the text color to default.
- textColor_red: Colors the text red.
- textColor_green: Colors the text green.
- textColor_yellow: Colors the text yellow.
- textColor_blue: Colors the text blue.
- textColor_cyan: Colors the text cyan.
- textColor_magenta: Colors the text magenta.
- textColor_white: Colors the text white.
- textColor_orange: Colors the text orange.
- textColor_purple: Colors the text purple.
- textColor_light_red: Colors the text light red.
- textColor_light_green: Colors the text light green.
- textColor_light_yellow: Colors the text light yellow.
- textColor_light_blue: Colors the text light blue.
- textColor_light_cyan: Colors the text light cyan.
- textColor_light_magenta: Colors the text light magenta.
- textColor_dark_red: Colors the text dark red.
- textColor_dark_green: Colors the text dark green.
- textColor_dark_yellow: Colors the text dark yellow.
- textColor_dark_blue: Colors the text dark blue.
- textColor_dark_cyan: Colors the text dark cyan.
- textColor_dark_magenta: Colors the text dark magenta.
- textStyle_bold: Makes the text bold.
- textStyle_italic: Makes the text italic.
- textStyle_underline: Makes the text underlined.
- clearText: Clears the terminal screen.
- cursorUp: Moves the cursor to the top of the terminal.
- defaultHeader: Prints a formatted header box with a title.
- greenHeader: Creates a header with a title in green.
- redHeader: Creates a header with a title in red.
- yellowHeader: Creates a header with a title in yellow.
- defaultSubheader: Prints a formatted subheader box with a title.
- modifiedSubheader: Prints a formatted subheader box with a title and a list of descriptions.
- MainMenuFormat: Prints a formatted main menu with a title and a list of options.

'''
def textColor_dark_red(text):
    '''
    
    Colors the string dark red.
    
    '''
    DARK_RED = "\033[38;5;124m"
    R = "\033[0m"
    return f"{DARK_RED}{text}{R}"

def textColor_dark_green(text):
    '''
    
    Colors the string dark green.
    
    '''
    DARK_GREEN = "\033[38;5;22m"
    R = "\033[0m"
    return f"{DARK_GREEN}{text}{R}"

def textColor_dark_yellow(text):
    '''
    
    Colors the string dark yellow.
    
    '''
    DARK_YELLOW = "\033[38;5;130m"
    R = "\033[0m"
    return f"{DARK_YELLOW}{text}{R}"

def textColor_dark_blue(text):
    '''
    
    Colors the string dark blue.
    
    '''
    DARK_BLUE = "\033[38;5;24m"
    R = "\033[0m"
    return f"{DARK_BLUE}{text}{R}"

def textColor_dark_cyan(text):
    '''
    
    Colors the string dark cyan.
    
    '''
    DARK_CYAN = "\033[38;5;36m"
    R = "\033[0m"
    return f"{DARK_CYAN}{text}{R}"

def textColor_dark_magenta(text):
    '''
    
    Colors the string dark magenta.
    
    '''
    DARK_MAGENTA = "\033[38;5;125m"
    R = "\033[0m"
    return f"{DARK_MAGENTA}{text}{R}"

def textColor_orange(text):
    '''
    
    Colors the string orange.
    
    '''
    ORANGE = "\033[38;5;208m"
    R = "\033[0m"
    return f"{ORANGE}{text}{R}"

def textColor_purple(text):
    '''
    
    Colors the string purple.
    
    '''
    PURPLE = "\033[38;5;55m"
    R = "\033[0m"
    return f"{PURPLE}{text}{R}"

def textColor_reset(text):
    '''
    Change the entire string back to its original color
    
    '''
    R = "\033[0m"
    return f"{R}{text}{R}"

def textColor_red(text):
    '''
    
    Colors the string red.
    
    '''
    RED = "\033[31m"
    R = "\033[0m"
    return f"{RED}{text}{R}"

def textColor_green(text):
    '''
    
    Colors the string green
    
    '''
    GREEN = "\033[32m"
    R = "\033[0m"
    return f"{GREEN}{text}{R}"

def textColor_yellow(text):
    '''
    
    Colors the string yellow
    
    '''
    YELLOW = "\033[93m"
    R = "\033[0m"
    return f"{YELLOW}{text}{R}"

def textColor_blue(text):
    '''
    
    Colors the string blue.
    
    '''
    BLUE = "\033[34m"
    R = "\033[0m"
    return f"{BLUE}{text}{R}"

def textColor_cyan(text):
    '''
    
    Colors the string cyan.
    
    '''
    CYAN = "\033[36m"
    R = "\033[0m"
    return f"{CYAN}{text}{R}"

def textColor_magenta(text):
    '''
    
    Colors the string magenta.
    
    '''
    MAGENTA = "\033[35m"
    R = "\033[0m"
    return f"{MAGENTA}{text}{R}"

def textColor_white(text):
    '''
    
    Colors the string white.
    
    '''
    WHITE = "\033[37m"
    R = "\033[0m"
    return f"{WHITE}{text}{R}"

def textColor_light_red(text):
    '''
    
    Colors the string light red.
    
    '''
    LIGHT_RED = "\033[91m"
    R = "\033[0m"
    return f"{LIGHT_RED}{text}{R}"

def textColor_light_green(text):
    '''
    
    Colors the string light green.
    
    '''
    LIGHT_GREEN = "\033[92m"
    R = "\033[0m"
    return f"{LIGHT_GREEN}{text}{R}"

def textColor_light_yellow(text):
    '''
    
    Colors the string light yellow.
    
    '''
    LIGHT_YELLOW = "\033[93m"
    R = "\033[0m"
    return f"{LIGHT_YELLOW}{text}{R}"

def textColor_light_blue(text):
    '''
    
    Colors the string light blue.
    
    '''
    LIGHT_BLUE = "\033[94m"
    R = "\033[0m"
    return f"{LIGHT_BLUE}{text}{R}"

def textColor_light_cyan(text):
    '''
    
    Colors the string light cyan.
    
    '''
    LIGHT_CYAN = "\033[96m"
    R = "\033[0m"
    return f"{LIGHT_CYAN}{text}{R}"

def textColor_light_magenta(text):
    '''
    
    Colors the string light magenta.
    
    '''
    LIGHT_MAGENTA = "\033[95m"
    R = "\033[0m"
    return f"{LIGHT_MAGENTA}{text}{R}"

def textStyle_bold(text):
    '''
    
    Makes the text bold.
    
    '''
    BOLD = "\033[1m"
    R = "\033[0m"
    return f"{BOLD}{text}{R}"

def textStyle_italic(text):
    '''
    
    Makes the text italic.
    
    '''
    ITALIC = "\033[3m"
    R = "\033[0m"
    return f"{ITALIC}{text}{R}"

def textStyle_underline(text):
    '''
    
    Makes the text underlined.
    
    '''
    UNDERLINE = "\033[4m"
    R = "\033[0m"
    return f"{UNDERLINE}{text}{R}"

def clearText(text):
    '''
    
    Clears the terminal screen
    
    '''
    CLEAR = "\033[2J"
    R = "\033[0m"
    return f"{CLEAR}{text}{R}"

def cursorUp(text):
    """
    
    Puts the cursor up to the top. Best use with clearText.

    """
    HOME = "\033[H"
    R = "\033[0m"
    return f"{HOME}{text}{R}"

GREEN = "\033[32m"
RESET = "\033[0m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RED = "\033[31m"

def defaultHeader(text, parameter):
    """
    
    Prints a formatted header box with a title.

    """
    length = parameter
    first = f"{BOLD}|{'=' * (length - 2)}|{RESET}"
    second = " "

    text_length = len(text)
    total_space = length - 2 - text_length  
    left_padding = total_space // 2 
    right_padding = total_space - left_padding  

    third = f"|{BOLD}{YELLOW}{' ' * left_padding}{text}{' ' * right_padding}{RESET}|"

    fourth = f"+{'-' * (length - 2)}+"
    
    return f"{first}\n{second}\n{third}\n{fourth}"

def greenHeader(text, parameter):
    """
    
    Prints a formatted header box with a title but the color green.

    """
    length = parameter
    first = f"{BOLD}|{'=' * (length - 2)}|{RESET}"
    second = " "

    text_length = len(text)
    total_space = length - 2 - text_length  
    left_padding = total_space // 2 
    right_padding = total_space - left_padding  

    third = f"|{BOLD}{GREEN}{' ' * left_padding}{text}{' ' * right_padding}{RESET}|"

    fourth = f"+{'-' * (length - 2)}+"
    
    return f"{first}\n{second}\n{third}\n{fourth}"

def redHeader(text, parameter):
    """
    
    Prints a formatted header box with a title but the color red.
    

    """
    length = parameter
    first = f"{BOLD}|{'=' * (length - 2)}|{RESET}"
    second = " "

    text_length = len(text)
    total_space = length - 2 - text_length  
    left_padding = total_space // 2 
    right_padding = total_space - left_padding  

    third = f"|{BOLD}{RED}{' ' * left_padding}{text}{' ' * right_padding}{RESET}|"

    fourth = f"+{'-' * (length - 2)}+"
    
    return f"{first}\n{second}\n{third}\n{fourth}"

def modifiedSubheader(title, fullParameter, subParameter, rows, descriptions):
    """
    Prints a formatted subheader box with a title and multiple rows of information.
    Full Parameter and Sub Parameter should have a twenty (20) charachter difference 
    for a full alligned box. Just call in like a function and you're good to go

    """
    text_length = len(title)
    total_space = subParameter - 2 - text_length  
    left_padding = total_space // 2 
    right_padding = total_space - left_padding
    p = round(subParameter * .33)
    p = p - 2
    r = round(subParameter* .66)
    r = r - 1
    
    sm1 = f"+{'-' * (subParameter - 2)}+"
    sm2 = f"|{' ' * left_padding}{title}{' ' * right_padding}|"
    print(f"{sm1:^{fullParameter}}")
    print(f"{BOLD}{sm2:^{fullParameter}}{RESET}")
    print(f"{sm1:^{fullParameter}}")
    
    for i in range(rows):
        number = i + 1
        number_formatted = f"[{number}]"
        if i < len(descriptions):
            description = descriptions[i] 
        else:
            description = "No description"
        sample = f"|{number_formatted:^{p}}| {description:<{r}}|"
        print(f"{sample:^{fullParameter}}")
    print(f"{sm1:^{fullParameter}}")

def defaultSubheader(title, fullParameter, subParameter):
    """
    
    Prints a formatted subheader box with a title.

    """
    text_length = len(title)
    total_space = subParameter - 2 - text_length  
    left_padding = total_space // 2 
    right_padding = total_space - left_padding
    p = round(subParameter * .33)
    p = p - 2
    r = round(subParameter* .66)
    r = r - 1
    
    sm1 = f"+{'-' * (subParameter - 2)}+"
    sm2 = f"|{' ' * left_padding}{title}{' ' * right_padding}|"
    print(f"{sm1:^{fullParameter}}")
    print(f"{BOLD}{sm2:^{fullParameter}}{RESET}")
    print(f"{sm1:^{fullParameter}}")
    
def MainMenuFormat(title, parameter, rows, descriptions):
    '''
    
    Prints a formatted menu box with a title and descriptions.
    
    The parameter should be a multiple of 5 and between 40 and 100.
    The rows should be a positive integer. The descriptions should be a list of strings.

    '''
    if parameter in [40,45,50,55,60,65,70,75,80,85,90,95,100]:
        text_length = len(title)
        total_space = parameter - 2 - text_length  
        left_padding = total_space // 2 
        right_padding = total_space - left_padding
        p = round(parameter * .33)
        p = p - 2
        if parameter in [45,60,75]:
            r = round(parameter* .66)
            r = r - 2
        else:
            r = round(parameter* .66)
            r = r - 1
        
        first = f"{BOLD}|{'=' * (parameter - 2)}|{RESET}"
        sm1 = f"+{'-' * (parameter - 2)}+"
        sm2 = f"|{' ' * left_padding}{YELLOW}{title}{RESET}{' ' * right_padding}|"
        print(f"{first:^{parameter}}")
        print(f"{first:^{parameter}}")
        print(f" ")
        print(f"{BOLD}{sm2:^{parameter}}{RESET}")
        print(f"{first:^{parameter}}")
        print()
        
        for i in range(rows):
            number = i + 1
            number_formatted = f"[{number}]"
            if i < len(descriptions):
                description = descriptions[i] 
            else:
                description = "No description"
            sample = f"|{number_formatted:^{p}}| {description:<{r}}|"
            print(f"{sample:^{parameter}}")
        print(f"{sm1:^{parameter}}")
    else: 
        print("Parameters out of range, please adjust the parameters.")




