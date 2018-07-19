import re,sys
from operator import itemgetter
EMAIL_REGEX = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.(com|edu|org){1}$")
#above regex verifies email
#print(EMAIL_REGEX.match('rghweth@grer.com'))

class User(object):
    def __init__(self, name, email):
        self.set_email(email)
        self.name=name        
        self.books={}
    def get_email(self):
        return self.email
    def get_name(self):
        return self.name
    @classmethod
    def isValidEmail(self,email):
        if EMAIL_REGEX.match(email)==None:
            print('invalid email address, domain can end with .com or .edu or .org only')
            return False
        else:
            return True
    def set_email(self,email):
        if User.isValidEmail(email)==False:
            sys.exit()
        else:
            self.email=email
        
    def change_email(self, address):
        self.set_email(address)
        print("this user's email has been updated")

    def __repr__(self):
        return str('User: '+self.get_name()+', email: '+self.get_email()+', books read: '+
                   str(len(self.books))+', Avg rating: '+str(self.get_average_rating()))

    def __eq__(self, other_user):
        return self.name==other_user.name and self.email==other_user.email
    def read_book(self,book,rating=None):
        self.books[book]=rating
    def get_average_rating(self):
        if len(self.books)==0:
            return 0
        else:
            sum=0
            for b in self.books.items():
                if(isinstance(b[1],int)):#check for None values
                    sum=sum+b[1]                
            return sum/float(len(self.books))

    
class Book(object):
    isbn_list=[]
    def __init__(self,title,isbn,price): 
        self.set_isbn(isbn)
        self.set_price(price)
        self.title=title
        self.ratings=[]
        
    def isISBNUnique(self,isbn):
        return not(isbn in Book.isbn_list)
    def get_title(self):
        return self.title
    def get_isbn(self):
        return self.isbn
    def get_price(self):
        return self.price
    def set_price(self,price):
        if(isinstance(price,int) and price>0):
            self.price=price
        else: 
            print("enter a valid price")
            sys.exit()
    def set_isbn(self,isbn):
        if(self.isISBNUnique(isbn)):
            self.isbn=isbn
            Book.isbn_list.append(self.isbn)
            print("this book's ISBN has been updated with "+str(self.isbn))
        else: 
            print("Book with this ISBN already exists")
            sys.exit()
    def add_rating(self,rating):
        try:
            if(0<=rating<=4):
                self.ratings.append(rating)
                print("rating added successfully")
            else:
                print('invalid rating')
        except:#executed when if clause raises exception when rating is not a number
            print('invalid rating')
    def __eq__(self, other_book):
        return self.title==other_book.title and self.isbn==other_book.isbn
    def get_average_rating(self):
        if len(self.ratings)==0:
            return 0
        else:
            return sum(self.ratings)#/float(len(self.ratings))#here we are not keeping a check for None type 
            #because we have already validated it through add_rating() method
    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    
    def __init__(self,title,author,isbn,price):
        Book.__init__(self,title,isbn,price)
        self.author=author
    def get_author(self):
        return self.author
    def __repr__(self):
        return self.get_title()+' by '+self.get_author()
        
class Non_Fiction(Book):
    
    def __init__(self,title,subject,level,isbn,price):
        Book.__init__(self,title,isbn,price)#another way of calling base class constructor
        self.subject=subject
        self.level=level
    def get_subject(self):
        return self.subject
    def get_level(self):
        return self.level
    def __repr__(self):
        return self.get_title()+', a '+str(self.get_level())+' manual on '+self.get_subject()
    
    
    
class TomeRater(object):
    def __init__(self):
        self.users={}
        self.books={}
    def create_book(self,title,isbn,price):    
        return Book(title,isbn,price)
    def create_novel(self,title,author,isbn,price):
        return Fiction(title,author,isbn,price)
    def create_non_fiction(self,title,subject,level,isbn,price):
        return Non_Fiction(title,subject,level,isbn,price)
    def add_book_to_user(self,book,email,rating=None):
        if(email in self.users.keys()):
            user=self.users[email]#get user
            user.read_book(book,rating)#make the user to read book
            if rating is not None:
                book.add_rating(rating)#rating to book
            if(book in self.books.keys()):
                self.books[book] +=1#increasing value by one
            else:
                #print(book.__hash__())
                self.books[book]=1#adding a book, since it has not been read before
        else:
            print("No user with email "+email+"!")
            
    def add_user(self,name,email,books=None):
        if isinstance(name,str) and isinstance(email,str):
            if(not email in self.users.keys()):
                user=User(name,email)
                self.users[email]=user
                if(books is not None):
                    for book in books:
                        self.add_book_to_user(book,email)
            else:
                print("User with this email already exists")            
        else:
            print('enter name and email as strings')         
        
    
    def print_catalog(self):
        print("Title"+"\t"*4+"\tISBN\tAverage Rating")
        for book in self.books.keys():
            print(book.get_title()+'\t'*2+str(book.get_isbn())+'\t'+str(book.get_average_rating()))
    def print_users(self):
        for user in self.users.values():
            print(user)
           # print(user.get_name())
    def most_read_book(self):
        most=max(self.books.values())
        for book in self.books.items():
            if(book[1]==most):
                return book[0]
    def highest_rated_book(self):
        max=0
        for book in self.books.keys():
            if(book.get_average_rating()>max):
                max=book.get_average_rating()
                highest_avg_rating_book=book
        return highest_avg_rating_book
    def most_positive_user(self):
        max=0
        #l={1:None}
        for user in self.users.values():
            #print(user.get_average_rating())
            if(user.get_average_rating()>max):
                max=user.get_average_rating()
                m_p_u=user        
        return m_p_u 

    def __repr__(self):
        self.print_catalog()
        self.print_users()           
        return ""
    def __eq__(self,other_TomeRater):#if they have same users and books, they are same
        if (cmp(self.books.keys(),other_TomeRater.books.keys())
                and cmp(self.users.keys(),other_TomeRater.users.keys())==0):
            return True
        else:
            return False
        
    def get_n_most_read_books(self,n):
        if(isinstance(n,int) and n>0):
            data=self.books.items()
            if(len(data)!=0 and n<=len(data)):
                data=sorted(data,key=itemgetter(1),reverse=True)
                return [book[0] for book in data[:n]]# data is a list of tuples where 1st elemnt of tuple is book and 2nd rating
            else:
                print("No book read :(")
                return None       
        else:
            print("enter a non zero integer value for n")
            
    def get_n_most_prolific_readers(self,n):
        if(isinstance(n,int) and n>0):
            data=[(user,len(user.books)) for user in self.users.values()]
            if(len(data)!=0 and n<=len(data)):
                data=sorted(data,key=itemgetter(1),reverse=True)
                return [user[0] for user in data[:n]]# data is a list of tuples where 1st elemnt of tuple is book and 2nd rating
            else:
                print("No users :(")
                return None       
        else:
            print("enter a non zero integer value for n")

  

            
                
                
        
        



