import listmaker
import decoder

def display():
    list = listmaker.listmaker() #get the list of the library to work with

    #get request from user for what the would like to do
    print()
    request = input('What would you like to see?\n1 - All information\n2 - Titles\n3 - Authors\n4 - Genres\n5 - Ratings\n0 - Return to Main Menu\nYour Selection: ')
    print()

    while request != '': #set up a loop
        if request == '1': #All information
            library = open('library.txt', 'r') #open the txt to read all the information

            #set up a heading
            print(f'{"Title":<40}{"Author":<40}{"Year":<20}{"Genre":<20}{"Relationships":<30}{"Warnings":<35}{"Rating":<20}') 
            print('-' *192)

            #start reading the information
            title = library.readline()
            while title != '':
                title = title.rstrip('\n') #make sure to remove \n
                author = library.readline()
                author = author.rstrip('\n') #make sure to remove \n
                year = library.readline()
                year = year.rstrip('\n') #make sure to remove \n

                #the integers
                genre_number = int((library.readline()))
                genre = decoder.genre(genre_number)
                    
                relationships_number = int((library.readline()))
                relationships = decoder.relationships(relationships_number)
                
                warnings_number = int((library.readline()))
                warnings = decoder.warnings(warnings_number)

                rating_number = int((library.readline()))
                rating = decoder.rating(rating_number)

                #display info
                print(f'{title:<40}{author:<40}{year:<20}{genre:<20}{relationships:<30}{warnings:<35}{rating:<20}')
                title = library.readline()
            
            
        elif request == '2': #Titles
            #make a heading
            heading = "Titles"
            centered_title = heading.center(40)
            print(centered_title)
            print('-' *40)

            #get the titles
            titles_list = list[0::7]
            abc_titles = sorted(titles_list)#alphabetize 
            
            #display all the titles
            for item in abc_titles:
                title = item
                centered_title = title.center(40)
                print(centered_title)

            
        elif request == '3': #Authors
            #make a heading
            heading = "Authors"
            centered_authors = heading.center(40)
            print(centered_authors)
            print('-' *40)
            
            #get the authors
            authors_list = list[1::7]
            no_duplicates_authors_list = set(authors_list)
            abc_authors = sorted(no_duplicates_authors_list)#alphabetize 
            
            #display all the titles
            for item in abc_authors:
                author = item
                centered_author = author.center(40)
                print(centered_author)

                
        elif request == '4': #Genres
            request_number = int(input('1 - Romance\n2 - Fantasy\n3 - Future/Sci-Fi\n4 - Action/Adventure\n5 - Horror/Thriller\nWhich genre are you interested in displaying? '))
            request_genre = decoder.genre(request_number) #get the name of the genre for aesthetics

            #make a heading
            centered_request_genre = request_genre.center(175)
            print()
            print(centered_request_genre)
            print(f'{"Title":<40}{"Author":<40}{"Year":<20}{"Relationships":<30}{"Warnings":<35}{"Rating":<20}') 
            print('-' *172)

            #find all titles with that genre
            library = open('library.txt', 'r') #open the txt to read all the information
            title = library.readline()
            
            while title != '':
                title = title.rstrip('\n') #make sure to remove \n
                author = library.readline()
                author = author.rstrip('\n') #make sure to remove \n
                year = library.readline()
                year = year.rstrip('\n') #make sure to remove \n

                #the integers
                genre_number = int((library.readline()))
                
                relationships_number = int((library.readline()))
                relationships = decoder.relationships(relationships_number)
                
                warnings_number = int((library.readline()))
                warnings = decoder.warnings(warnings_number)

                rating_number = int((library.readline()))
                rating = decoder.rating(rating_number)

                if genre_number == request_number: #make an if statement so that it only prints all the info when the genre matches what is requested
                    print(f'{title:<40}{author:<40}{year:<20}{relationships:<30}{warnings:<35}{rating:<20}')
                
                title = library.readline()



        elif request == '5': #Rating
            request_number = int(input('Works of what rank are you interested in viewing? '))
            
            #make a heading
            print(f'{request_number:>85} Star Works')
            print(f'{"Title":<40}{"Author":<40}{"Year":<20}{"Genre":<20}{"Relationships":<30}{"Warnings":<35}') 
            print('-' *180)

            #find all titles with that genre
            library = open('library.txt', 'r') #open the txt to read all the information
            title = library.readline()
            
            while title != '':
                title = title.rstrip('\n') #make sure to remove \n
                author = library.readline()
                author = author.rstrip('\n') #make sure to remove \n
                year = library.readline()
                year = year.rstrip('\n') #make sure to remove \n

                #the integers
                genre_number = int((library.readline()))
                genre = decoder.rating(genre_number)
                
                relationships_number = int((library.readline()))
                relationships = decoder.relationships(relationships_number)
                
                warnings_number = int((library.readline()))
                warnings = decoder.warnings(warnings_number)

                rating_number = int((library.readline()))

                if rating_number == request_number: #make an if statement so that it only prints all the info when the rating matches what is requested
                    print(f'{title:<40}{author:<40}{year:<20}{genre:<20}{relationships:<30}{warnings:<35}')
                
                title = library.readline()
                
        elif request == '0':
            Main_Menu = 'Main Menu' #make a heading
            print(Main_Menu.center(61))
            print('-' *61)
            new_request = input('1 - Display current library\n2 - Add to the library\n3 - Display library statistics\n0 - exit the program\nWould you like to do anything else?: ')
            return new_request
        else:
            print("\nSorry, that isn't a valid entry.\n")
            
        print()
        request = input('What would you like to see?\n1 - All information\n2 - Titles\n3 - Authors\n4 - Genres\n5 - Ratings\n0 - Return to Main Menu\nYour Selection: ')
        print()
