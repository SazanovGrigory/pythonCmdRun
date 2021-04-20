# name:         TColors
# Version:      1
# Created by:   Grigory Sazanov
# GitHub:       https://github.com/SazanovGrigory

class TerminalColors:
    # Description:  Class that can be used to color terminal output
    # Example:      print('GitHub:     '+f"{BColors.TerminalColors.UNDERLINE}https://github.com/SazanovGrigory{BColors.TerminalColors.ENDC}")
    HEADER ='\033[95m'
    OKBLUE ='\033[94m'
    OKCYAN ='\033[96m'
    OKGREEN ='\033[92m'
    WARNING ='\033[93m'
    FAIL ='\033[91m'
    ENDC ='\033[0m'
    BOLD ='\033[1m'
    UNDERLINE ='\033[4m'

def main():
    print('Name:         '+f"{TerminalColors.HEADER}TColors{TerminalColors.ENDC}")
    print('Version:      '+f"{TerminalColors.WARNING}1{TerminalColors.ENDC}")
    print('Created by:   '+f"{TerminalColors.BOLD}Grigory Sazanov{TerminalColors.ENDC}")
    print('GitHub:       '+f"{TerminalColors.UNDERLINE}https://github.com/SazanovGrigory{TerminalColors.ENDC}")
    print(f"{TerminalColors.OKGREEN}Description:  This is just a class that can be used to color terminal output{TerminalColors.ENDC}")
    print("Example:      print(\"GitHub:     \"+f\"{TColors.TerminalColors.UNDERLINE}Some text here{TColors.TerminalColors.ENDC}\")")
    print('Colors:')
    print('              '+f"{TerminalColors.HEADER}HEADER{TerminalColors.ENDC}")
    print('              '+f"{TerminalColors.OKBLUE}OKBLUE{TerminalColors.ENDC}")
    print('              '+f"{TerminalColors.OKCYAN}OKCYAN{TerminalColors.ENDC}")
    print('              '+f"{TerminalColors.OKGREEN}OKGREEN{TerminalColors.ENDC}")
    print('              '+f"{TerminalColors.WARNING}WARNING{TerminalColors.ENDC}")
    print('              '+f"{TerminalColors.FAIL}FAIL{TerminalColors.ENDC}")
    print('              '+f"{TerminalColors.BOLD}BOLD{TerminalColors.ENDC}")
    print('              '+f"{TerminalColors.UNDERLINE}UNDERLINE{TerminalColors.ENDC}")
    

if __name__ == '__main__':
    main()