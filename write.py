import decoder

def write():
    library = open('library.txt','a') #open the txt
    #Display a greeting for the user
    title = input('\nTo begin please enter the title of the entry or hit 0 to exit to main menu: ') #begin collecting information from user and communicating what they should do if they are finished using the program

    temp_list = []
    
    while title != '': #inclue a terminating command
        if title == '0':
            print()
            Main_Menu = 'Main Menu' #make a heading
            print(Main_Menu.center(61))
            print('-' *61)
            new_request = input('1 - Display current library\n2 - Add to the library\n3 - Display library statistics\n0 - exit the program\nWould you like to do anything else?: ')
            return new_request
        else:
            #get the rest of the information about the work from the user
            author = input('\nEnter the name of the author (or NA to skip): ')
            year = input('\nEnter the year the work was published (or NA to skip): ')
            #from this point on I thought it would be smart to convert the entries to integers to make it more simple / get fewer types of responses (and removed possible errors like 'Fantasy' vs 'fantasy' being treated differently
            genre = int(input('\n0 - NA\n1 - Romance\n2 - Fantasy\n3 - Future/Sci-Fi\n4 - Action/Adventure\n5 - Horror/Thriller\nPlease select one of the above genres: '))
            relationships = int(input('\n0 - No Relationships\n1 - Straight Relationships\n2 - Gay Relationships\n3 - Lesbian Relationships\n4 - Multiple Relationships\nPlease select one of the above relationship categories: '))
            warnings = int(input('\n0 - No Warnings\n1 - Graphic Depictions of Violence\n2 - Major Character Death\n3 - Adult Themes\nPlease select a warning level: '))
            rating = int(input('\nPlease select a rating from 1-5 for this work (or 0 for no rating): '))

            #add the information to a temporary list to first make sure it's correct before adding to the txt file
            temp_list = []
            temp_list.append(title)
            temp_list.append(author)
            temp_list.append(year)
            temp_list.append(genre)
            temp_list.append(relationships)
            temp_list.append(warnings)
            temp_list.append(rating)
        
            
            class Entry:
                def __init__(self,title,author,year,genre,relationship,warnings,rating):
                    self.title = title
                    self.author = author
                    self.year = year
                    self.genre = genre
                    self.relationship = relationship
                    self.warnings = warnings
                    self.rating = rating

            #put everything together into a class
            new_entry = Entry(temp_list[0],temp_list[1],temp_list[2],temp_list[3],temp_list[4],temp_list[5],temp_list[6])

            #decode the numbers so when displayed to the user it's easier to confirm it is the correct information
            genre_decode = decoder.genre(new_entry.genre)
            relationship_decode = decoder.relationships(new_entry.relationship)
            warning_decode = decoder.warnings(new_entry.warnings)
            rating_decode = decoder.rating(new_entry.rating)
            
            print()
            print(f'You entered the following information:\nTitle: {new_entry.title}\nAuthor: {new_entry.author}\nYear Published: {new_entry.year}\nGenre: {genre_decode}\nRelationships: {relationship_decode}\nWarnings: {warning_decode}\nPersonal Rating: {rating_decode}\n\nDoes all of this information look correct?')

            answer = input("If yes please type 'y', if not please type 'n': ")
            if answer == 'y' or answer == 'Y': #get both y and Y just to make sure no error if typed lower vs capitol
                #write all of this information down
                library.write(f'{title}\n')
                library.write(f'{author}\n')
                library.write(f'{year}\n')
                library.write(f'{genre}\n')
                library.write(f'{relationships}\n')
                library.write(f'{warnings}\n')
                library.write(f'{rating}\n')

                print('\nGreat! The above information has been entered into the library database!')
                print("Let's move on to the next entry!")
                
            else:
                print("\nOkay no worries! Please start this entry over:")

            #end the loop by asking for the next title, remember '' will end the loop!
        title = input('\nPlease start by entering the title or 0 enter to exit to main menu: ')

    library.close() #close the txt to save everything
