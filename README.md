# IntroToPythonFinalProject
The code for the final project of my Intro to Python class

Here is a link to my blog with my process and thoughts: https://learning1about1python.blogspot.com/2025/07/final-project.html





**Problem:**

I am very active reader and have many close family and friends who are also very active readers. When you read a lot it can be difficult remembering everything you've read! Sometimes I want to go back and reread a book but it can be very difficult trying to find the book when all I have are disorganized links, a stack of books, or titles scribbled on a piece of paper. So I thought it would be cool to create a database for all of my books! Key features I would want to include would be: the ability to add to the database, display all the books in the database, and display statistics of the database. But I didn't just want a list of a bunch of titles of books - that wouldn't really help me solve my problem! So it was important to me that I could also include other crucial information that might help me remember the details of each book! For this reason I included other bits of information to be stored in the database like author, year published, genre, what relationships were in the book, any warnings, and my own rating for the book! In this way I ended up creating my own personal library database!






**The Code:**

Write:

To start I began working on a way of getting the information I wanted from the user. I made a greeting and prompted the user to start by entering the title for the work (I later went back and made sure to include an option for the user to back out to a main menu I hadn't yet created). Once I had the title I just had the user enter a series of information like the author, year published, etc. I originally just had the code immediately save this to the library.txt file but later realized that the user could maybe make a mistake or a typo and that they might wish to change their entry so I created a temp_list = [] to temporarily store all the information. 

I decided it would be better to store things like genre, relationships, and warnings just as an integer for a few reasons. It would make it easier for the user to just type '1' for Romance rather 'Romance' it would also ensure that I wouldn't have to worry about spelling mistakes, accidental spaces or distinguishing between 'Romance', 'romance', ' romance', 'romance ', etc. Additionally, by limiting what the user could select it limited the options and allowed for simpler data to be displayed later on. (For example, if someone was given free reign there might be 32 different genres and I felt that was a bit excessive and wouldn't result in a clear and easy to read data / display for later.)

Now that I had all the information from the user I thought it would be nice to create a class. Looking back this wasn't really necessary and I probably could have skipped this step. Overall this part was a bit frustrating but fun. I originally just printed all this information back to the user but realized it would be annoying for the user to scroll up to confirm which number corresponded with genres, relationships, warnings, etc. So I used a decoder.py program that I also use again later in the display.py portion of the project for the confirmation screen to make it easier for the user to read and confirm all the information.

Finally, to finish off the writing process I just needed to have the user confirm the information entered. I created an if-else statement so that if it was correct I had them type 'y' but I also accounted for 'Y'. If the information was correct I simply wrote it down in the library.txt file. For all other responses I defaulted to throwing away the entered information (ie if the user maybe mistyped 'h' which is directly between the 'y' and 'n' key on the keyboard I felt it was better to err on the side of caution and not add the entry to the library.txt file). I ended the entire loop by asking for the title of the next entry or presented the option to exit back to the main menu. And then of course remembered to close the library.txt file.



Decode:

As mentioned above this decoder.py was used to convert the entries from the user back into words that were consistent (ie no 'Romance' vs 'romance'). This decoder is used in the write.py and display.py programs. I feel the code is pretty straight forward. If you had the value rating = 2 and sent that 2 to the rating function: rating(2) would return the string '2 Stars' thus converting the integer input that is extracted from the temp list (write.py) or txt file (display.py) into a string to be displayed to the user.



Display:

Now that I had a way of writing (write.py)) and decoding (decoder.py) all the information in the library.txt file I wanted to have a way of displaying everything.

I started by importing decoder.py and listmaker.py. I had the listmaker.py program make me a list with all the information in the library.txt file so I could work with that. Next I displayed a menu for the user to select what they wanted displayed. I thought it would be boring to just have it display all the information in the library.txt file and should be able to do some level of filtering. I could have made this portion more advanced and extensive but I figured what I have was a good demonstration of features.

Next I set up a loop to handle all the different choices. The first option was just to display all the information. I created a header to make all the information easy to read. I made a while loop so that the the loop would just run through all the information in the library.txt file since it was requested that all information be displayed. Then I simply had to read each line from the library.txt file and strip the '\n'. I also decoded the information like the genre, relationships, and warnings in the decoder.py. Then I finished by printing all the information in one line to slowly fill in the table of information.

The next requested display option was to just show all the titles. I made a header again to make it all easy to read. Then I made a new titles_list and extracted just the titles from the list that was made with listmaker.py by slicing the list. Now this new titles_list only contained titles! Next I thought it would be nice to alphabetize this, so I sorted the list. Finally I just needed to make a loop to print all the items in the new list. The third option requested all authors to be displayed. This was almost identical in execution as the method for displaying just the titles but I realized some books might be written by the same person so I made sure to remove any duplicate names. I did some searching online and sets fit this need perfectly! Sets only store a unique item once!

The next two display options were also very similar in methodology. To display the genres and ratings I again started by making a heading followed by reading the first line of the library.txt file to get the first title. Then I set up my while loop to make sure I ran through the entire library.txt file. I stripped the '\n' from the title, author, and year. Next I needed to save either the genre or rating for later. I then used the decoder.py program to get the rest of the information. I then had to set up an if statement so that all of this stored information would only be printed if the genre number or rating I grabbed from the library.txt file matched what was requested. It would do nothing if the values didn't math. This was how I got the program to only display only the requested information in a neat table. 

Finally I needed to allow the user to return the main menu if they entered that option. I printed the same menu that is in the main.py program and simply returned the entered value to the main program. This made it so that you could run through this portion of the program as much as you wanted but only when you committed to returning to the main menu would your selection be returned. 

I also made sure to include an error message if anything other than numbers 0-5 were entered because I thought it looked nice and gave feedback to the user if a mistake was made rather than just nothing happening. And finally I ended the while loop so that it could continue to collect requests from the user.



List maker:

I use listmaker.py in both display.py and statistics.py so it made sense for it to have it's own program. First it creates an empty list to put all the information. Then it just loops through reading all the information in the library.txt file and then either removing the '\n' or making the value an integer. Then it ends by appending all of that information to the new list and returning that list.



Statistics:

The next main feature I wanted was a way for the program to display different statistics. Just like with display.py I'm sure I could have added more detailed features and fully flushed out all possible options but I felt that might have been a bit too ambitious and unnecessary since this program is mostly just for personal use. 

I imported listmaker.py to begin since I would use this program in multiple functions.

I started with a function to calculate the total number of works in the library. To do this I used listmaker.py to make a list and then I grabbed a list of just the titles by slicing the list. Then I made a loop to go through each item in the list and add one to a counter. Once that loop is done I now had a count for all the titles in the file. 

Next I wanted to make a function to give me more specific information about the genre statistics. I made a header and used listmaker.py to make a list from all the information in library.txt. Then I sliced the list to just have the genre numbers. Next I made counters for each genre and then had a loop go through all items in the list and add to the different counts. This allowed me to count all genre types at once. Originally I was going to stop here but then I remembered I had made the total_works() function and realized I could very easily display percentages.

Finally I needed to make a statistics() function to mesh everything together! This is the function that main.py calls! It was really neat having such a multilayered function calling system ie: main() -> statistics() -> ranking_stats() -> total_works() -> listmaker(). This statistics() function wasn't very complicated and is very similar to a lot of previously discussed functions. I started by requesting the user for input on what they would like to do then set up a loop and if-elif-else statements to go through all the options and run the above related statistics functions when requested. Similarly with display.py I made an error statement that would be displayed when a mistype occured. And just like in writer.py and display.py I made sure to include a way to return to the main menu by returning the new_request selected from an identical main menu.



Main:

Finally I will discuss the Main Program.py. Even though I am discussing this last it was actually constantly worked on as I finished each layer of code. 

I imported the three major programs that handle most of the work in the code: write.py, display.py, and statistics.py.

First I made sure to open the library.txt file in append mode. This would create a new file if one didn't already exist (the user's first time using the program). Then I displayed a greeting with a description of what the program does followed by displaying a main menu of options to choose from. Then just as I've done many times I made a while loop followed by if-elif statements to handle the different selected options. Then I simply had to start the corresponding function that was requested (ie if the user wanted to have the library displayed I just had to start the display() function in display.py). Because I made an option to return to the main menu in the 3 major programs I needed to store this value as the new request to allow free navigation between all the options. I also added a way of closing the program.






**Thoughts on What I Learned:**

Once I had figured out my writer program I wanted to make sure I knew how to extract all the information from the library.txt file before making anything more complicated. I had some difficulty reading the file and having each line be added to a list. I needed to make sure the entries were being properly stored in the list as either a string - the title and author's name - or an integer for all the rankings and number shortcuts I employed. To do this I did a lot of research on the web with prompts like "how to read strings and numbers in a txt file." I think this is ultimately why I ended up using the classes even though I think I could figure out a better way now.

In the statistics.py I originally just had the total_works() also print and display the total works: print(f'There are {count} total works in the library.'). But then I realized I could use the same function to easily calculate the averages in the genre and rating statistics! So I just edited it to return the count of total works instead!

display.py and statistics.py were both quite long and in depth programs that did multiple things. I wrote display.py first and it ended up just being one very long function. I think I learned from this and when I made statistics.py I made a main statistics function and individual functions to handle all the different operations I wanted to be able to execute. I think this approach was far better because it allowed me to test the code in smaller chunks. I could test genre_stats() to find errors and then once that worked I could incorporate that back into the larger statistics() function. This is what I did on a larger scale as well with making all separate programs and having them link back into main.py rather than having everything in a super long program. This made troubleshooting much easier and overall I was able to avoid a lot of frustration in finding where an error was occurring and could immediately jump into understanding why an error was occuring. This method was also nice because I could reuse total_works() in genre_stats() and ranking_stats()! It felt very satisfying to have one function or program be used in multiple places!






**Conclusion:**

I started this project just to make enjoying my own hobby easier but I can easily see how something like this could be shared with friends and family and they could have their own library databases. I also really loved the customization aspect. I could add different filters and key information that I wanted to make sure I stored. Someone else might not care much about the year of publication and I could easily edit the code to remove this aspect and perhaps add a more desirable aspect for that person!
