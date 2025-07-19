def listmaker():
    list = [] #create an empty list to put everything in
    library = open('library.txt','r')

    #get first line
    title = library.readline()
    
    #set up a loop
    while title != '':
        title = title.rstrip('\n') #make sure to remove \n
        
        #get the rest of the data
        #the strings
        author = library.readline()
        author = author.rstrip('\n') #make sure to remove \n
        year = library.readline()
        year = year.rstrip('\n') #make sure to remove \n

        #the integers
        genre = int((library.readline()))
        relationships = int(library.readline())
        warnings = int(library.readline())
        rating = int(library.readline())

        #add everything to the list!
        list.append(title)
        list.append(author)
        list.append(year)
        list.append(genre)
        list.append(relationships)
        list.append(warnings)
        list.append(rating)

        title = library.readline()
        
    return list
