import listmaker
import add
import display
import statistics

def main():
    #create a file if one doesn't already exist
    library = open('library.txt','a') #put it in append mode because don't want to do write and overwrite everything

    #greet user and disply the menu
    print('Hello! This program allows you manage your own personal library!')
    print()
    Main_Menu = 'Main Menu' #make a heading
    print(Main_Menu.center(61))
    print('-' *61)
    request = input('To begin please select which of the following you would like:\n1 - Display current library\n2 - Add to the library\n3 - Display library statistics\n0 - Exit the program\nYour choice: ')

    while request != '': #set up a loop so user can do multiple things / doesn't have to restart the program each time they want to do something
        if request == '1': #Display library
            display.display()
        elif request == '2': #Add to library
            add.new()
            print('The above information has been entered into the library database!\n')
        elif request == '3': #Statistics
            statistics.statistics()
        elif request == '0': #end the program
            library.close()
            exit()

if __name__ == '__main__':
    main()
