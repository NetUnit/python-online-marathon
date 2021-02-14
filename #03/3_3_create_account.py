import string


'''
    Create function create_account(user_name: string, password: string, secret_words: list). 
    This function should return inner function check.

    The function check compares the values of its arguments with password and secret_words:
    the password must match completely, secret_words may be misspelled (just one element).

    Password should contain at least 6 symbols including one uppercase letter, one lowercase,
    special character and one number.

    Otherwise function create_account raises ValueError.


    ## does not satisfy condition: Outer Function raises error when inappropriate
    password
'''


# Defining function
def create_account(user_name, password, secret_words):

    # this values for instance came from database
    db_secret_words = secret_words
    db_psw = password
    db_user_name = user_name

    # closure fuction

    def check(psw, secr_w):
        try:
            for i in psw:
                # psw matching condition # 1
                if not psw == db_psw:
                    raise ValueError                          
                # lowercase condition # 2
                if not any(i in psw for i in string.ascii_lowercase):
                    raise ValueError                          
                # uppercase condition # 3
                if not any(i in psw for i in string.ascii_uppercase):
                    raise ValueError                           
                # digits condition # 4
                if not any(i in psw for i in string.digits):
                    raise ValueError                         
                # special chars condition # 5
                if not any(i in psw for i in r'!#$@%^_'):     
                    raise ValueError                            
                # length condition # 6
                if not 5 < len(list(password)):
                    raise ValueError                      
                # number of secret_words condition 7 
                if not len(db_secret_words) == len(secr_w):
                    raise ValueError
                    
                # special conditions
                # 8.1 length of each word in sorted lists no more than 2 elements 8.1 
                db_secret_words.sort()
                secr_w.sort()

                zipped = list(zip([len(i) for i in db_secret_words], [len(i) for i in secr_w]))

                if not max([abs(a-b) for a, b in  zipped]) < 2:
                    raise ValueError
        
                # 8.2  case of 1 symbol from secret_words was misspelled       
                dict_zip = dict(zip(db_secret_words, secr_w))

                counter = 0
                for key, value in dict_zip.items():

                    for i in range(min(len(key), len(value))):
                            
                        if key[i] != value[i]:
                            counter = counter + 1
                                
                            if len(key) != len(value) and counter > 0:
                                raise ValueError

                            elif len(key) == len(value) and counter > 1:
                                raise ValueError

                            else:
                                pass

                    counter = 0

                else:
                    return True

        except:
            return False
    
    return check


tom = create_account('Tom', 'Qwerty1_', ["1", "word"])

check1 = tom("Qwerty1_",  ["1", "word"]) # True complete match
print(check1)
check2 = tom("Qwerty1_",  ["word"]) # False due to the number of items in the list ["1", "word"] and ["word"] 
print(check2)
check3 = tom("Qwerty1_",  ["word", "12"]) # True only 1 misspelled item
print(check3)
check4 = tom("Qwerty1!",  ["word", "1"]) # False invalid password
print(check4)



