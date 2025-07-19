import listmaker

def total_works():
    list = listmaker.listmaker() #get the list of the library to work with
    titles_list = list[0::7] #a list of just the titles
    count = 0 #start a counter
    for items in titles_list:
        count += 1
    return count

def genre_stats():
    #make a title
    title = 'Genre Statistics'
    centered_title = title.center(52)
    print(centered_title)
    print('-' *52)
    
    list = listmaker.listmaker() #get the list of the library to work with
    genres_list = list[3::7] #make a new list for the genres only

    #make counters for each type
    Romance_count = 0
    Fantasy_count = 0
    Future_count = 0
    ActionAdventure_count = 0
    HorrorThriller_count = 0

    #start a loop to count all the entries of the genre list and sort them and add to the respective counter
    for entry in genres_list:
        if entry == 1:
            Romance_count += 1
        elif entry == 2:
            Fantasy_count += 1
        elif entry == 3:
            Future_count += 1
        elif entry == 4:
            ActionAdventure_count += 1
        elif entry == 5:
            HorrorThriller_count += 1
    print(f'There are:\n{Romance_count} Romance Works\n{Fantasy_count} Fantasy Works\n{Future_count} Future/Sci-Fi Works\n{ActionAdventure_count} Action/Adventure Works\n{HorrorThriller_count} Horror/Thriller Works')
    print()

    #grab the total from total_works() and calculate averages!
    total = total_works()
    percent_R = Romance_count / total
    percent_Fantasy = Fantasy_count / total
    percent_Future = Future_count / total
    percent_A = ActionAdventure_count / total
    percent_H = HorrorThriller_count / total

    print(f'Percent distribution of the {total} works in the library:\n{percent_R:.2%} Romance Works\n{percent_Fantasy:.2%} Fantasy Works\n{percent_Future:.2%} Future/Sci-Fi Works\n{percent_A:.2%} Action/Adventure Works\n{percent_H:.2%} Horror/Thriller Works')
    print('-' *52)
    print('\n')

    
def ranking_stats():
    #make a title
    title = 'Ranking Statistics'
    centered_title = title.center(52)
    print(centered_title)
    print('-' *52)
    
    list = listmaker.listmaker() #get the list of the library to work with
    ranking_list = list[3::7] #make a new list to store the rankings only

    #make counters for each type
    one_count = 0
    two_count = 0
    three_count = 0
    four_count = 0
    five_count = 0

    #start a loop to count all the entries of the genre list and sort them and add to the respective counter
    for entry in ranking_list:
        if entry == 1:
            one_count += 1
        elif entry == 2:
            two_count += 1
        elif entry == 3:
            three_count += 1
        elif entry == 4:
            four_count += 1
        elif entry == 5:
            five_count += 1
    print(f'There are:\n{one_count} One Star Works\n{two_count} Two Star Works\n{three_count} Three Star Works\n{four_count} Four Star Works\n{five_count} Five Star Works')
    print()

    #grab the total from total_works() and calculate averages!
    total = total_works()
    percent_1 = one_count / total
    percent_2 = two_count / total
    percent_3 = three_count / total
    percent_4 = four_count / total
    percent_5 = five_count / total

    print(f'Percent distribution of the {total} works in the library:\n1 Star Works - {percent_1:.2%}\n2 Star Works - {percent_2:.2%}\n3 Star Works - {percent_3:.2%}\n4 Star Works - {percent_4:.2%}\n5 Star Works - {percent_5:.2%}')
    print('-' *52)
    print('\n')
    

def statistics():
    request = int(input('\nWhat statistics are you interested in?:\n1 - Display the total number of works in the library\n2 - Stats by Genre\n3 - Stats by Ranking\n0 - Return to Main Menu\nYour Selection: '))
    print('\n')
    while request != '':
        if request == 1: #total works
            count = total_works()
            print(f'There are {count} total works in the library.')
            print('\n')
        elif request == 2: #genre
            print()
            genre_stats()
        elif request == 3: #ranking
            print()
            ranking_stats()            
        elif request == 0: #return to Main Menu
            Main_Menu = 'Main Menu' #make a heading
            print(Main_Menu.center(61))
            print('-' *61)
            new_request = input('1 - Display current library\n2 - Add to the library\n3 - Display library statistics\n0 - exit the program\nWould you like to do anything else?: ')
            return new_request
            print(new_request)
        else:
            print("Sorry, that isn't a valid entry.\n\n")
        request = int(input('What statistics are you interested in?:\n1 - Display the total number of works in the library\n2 - Stats by Genre\n3 - Stats by Ranking\n0 - Return to Main Menu\nYour Selection: '))
        print()
