import re
from pprint import pprint



def order_number():  # Retrieve order number
    """
        from below sentences we need to find/retrieve the order ids
    """
    chat1='codebasics: Hello, I am having an issue with my order # 412889912'
    chat2='codebasics: I have a problem with my order number 412889912'
    chat3='codebasics: My order 412889912 is having an issue, I was charged 300$ when online it says 280$'

    chats = [chat1, chat2, chat3]
    for i in chats:
        p = re.findall(r'order[^\d]*(\d+)', i)
        print(p)


def email_phn(): # Retrieve email id and phone
    chats = ['codebasics: you ask lot of questions 😠  1235678912, abc@xyz.com', 
             'codebasics: here it is: (123)-567-8912, abc@xyz.com', 
             'codebasics: yes, phone: 1235678912 email: abc77@xyz.com']
    for i in chats:
        phn_num = re.findall(r'\d{10}|\(\d{3}\)-\d{3}-\d{4}', i)
        # (\d{10})|(\(\d{3}\)-\d{3}-\d{4})
        email = re.findall(r'[a-zA-Z0-9]+@[A-Za-z]+\.com', i)
        # [a-zA-Z0-9]+@[A-Za-z]+\.[a-zA-Z]
        print("phone: ", phn_num, "email: ", email)


def information():  # Regex for Information Extraction
    """
    extract age, name, dob, birth_place
    """
    text='''
        Born	Elon Reeve Musk
        June 28, 1971 (age 50)
        Pretoria, Transvaal, South Africa
        Citizenship	
        South Africa (1971–present)
        Canada (1971–present)
        United States (2002–present)
        Education	University of Pennsylvania (BS, BA)
        Title	
        Founder, CEO and Chief Engineer of SpaceX
        CEO and product architect of Tesla, Inc.
        Founder of The Boring Company and X.com (now part of PayPal)
        Co-founder of Neuralink, OpenAI, and Zip2
        Spouse(s)	
        Justine Wilson
        ​
        ​(m. 2000; div. 2008)​
        Talulah Riley
        ​
        ​(m. 2010; div. 2012)​
        ​
        ​(m. 2013; div. 2016)
        '''
    age = re.findall(r"age\s(\d+)", text)
    name = re.findall(r"Born(.*)", text)
    dob = re.findall(r"Born.*\n(.*)\(age", text)
    birth_place = re.findall(r"\(age.*\n(.*)", text)
    return {
        "name": name[0].strip(),
        "age": age[0],
        "dob": dob[0].strip(),
        "birth_place": birth_place[0].strip()
    }

# order_number()
# email_phn()
# pprint(information())