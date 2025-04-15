# style.module
Stylized Text &amp; Your Layout Engine (STYLE)

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
