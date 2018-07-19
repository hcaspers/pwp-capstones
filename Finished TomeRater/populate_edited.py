from TomeRater_edited import *

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678,10)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345,500)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452,900)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938,4500)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010,450)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000,650)
#novel5 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")#

#Add a user with three books already read:
user_books=[book1, novel1, nonfiction1]
#user_books1=[book1, novel1, nonfiction1]
#print(cmp(user_books,user_books1))
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu",user_books)

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.most_read_book())
print(Tome_Rater)

for x in Tome_Rater.get_n_most_read_books(2):print(x)
for x in Tome_Rater.get_n_most_prolific_readers(2):print(x)
#print("Total worth: "+str(Tome_Rater.get_worth_of_user("alan@turing.com")))


#####################################################################
Tome_Rater2 = TomeRater()
#
##Create some books:
book1 = Tome_Rater2.create_book("Society of Mind", 12345658, 10)
novel1 = Tome_Rater2.create_novel("Alice In Wonderland", "Lewis Carroll", 123456,5)
novel1.set_isbn(9781536831134)
nonfiction1 = Tome_Rater2.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929453,3)
nonfiction2 = Tome_Rater2.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111939,2)
novel2 = Tome_Rater2.create_novel("The Diamond Age", "Neal Stephenson", 10101011,20)
novel3 = Tome_Rater2.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001001,6)
novel5 = Tome_Rater2.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000,7)
#
##Create users:
Tome_Rater2.add_user("Alan Turing", "alan@turing.com")
Tome_Rater2.add_user("David Marr", "david@computation.org")#
#
##Add a user with three books already read:
user_books=[book1, novel1, nonfiction1]
user_books1=[book1, novel1, nonfiction1]
Tome_Rater2.add_user("Marvin Minsky", "marvin@mit.edu",user_books)
#
##Add books to a user one by one, with ratings:
Tome_Rater2.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater2.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater2.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater2.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater2.add_book_to_user(novel3, "alan@turing.com", 1)
#
Tome_Rater2.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater2.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater2.add_book_to_user(novel3, "david@computation.org", 4)
print(Tome_Rater2==Tome_Rater)