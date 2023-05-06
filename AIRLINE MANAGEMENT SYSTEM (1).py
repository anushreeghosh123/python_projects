user=input("USERNAME")
password=input("PASSWORD")


#FOR SOURCE AND DESTINATION

country = [
    ('United States'),
    ('Afghanistan'),
    ('Albania'),
    ('Algeria'),
    ('American Samoa'),
    ('Andorra'),
    ('Angola'),
    ('Anguilla'),
    ('Antarctica'),
    ('Antigua And Barbuda'),
    ('Argentina'),
    ('Armenia'),
    ('Aruba'),
    ('Australia'),
    ('Austria'),
    ('Azerbaijan'),
    ('Bahamas'),
    ('Bahrain'),
    ('Bangladesh'),
    ('Barbados'),
    ('Belarus'),
    ('Belgium'),
    ('Belize'),
    ('Benin'),
    ('Bermuda'),
    ('Bhutan'),
    ('Bolivia'),
    ('Bosnia And Herzegowina'),
    ('Botswana'),
    ('Bouvet Island'),
    ('Brazil'),
    ('Brunei Darussalam'),
    ('Bulgaria'),
    ('Burkina Faso'),
    ('Burundi'),
    ('Cambodia'),
    ('Cameroon'),
    ('Canada'),
    ('Cape Verde'),
    ('Cayman Islands'),
    ('Central African Rep'),
    ('Chad'),
    ('Chile'),
    ('China'),
    ('Christmas Island'),
    ('Cocos Islands'),
    ('Colombia'),
    ('Comoros'),
    ('Congo'),
    ('Cook Islands'),
    ('Costa Rica'),
    ('Cote D`ivoire'),
    ('Croatia'),
    ('Cuba'),
    ('Cyprus'),
    ('Czech Republic'),
    ('Denmark'),
    ('Djibouti'),
    ('Dominica'),
    ('Dominican Republic'),
    ('East Timor'),
    ('Ecuador'),
    ('Egypt'),
    ('El Salvador'),
    ('Equatorial Guinea'),
    ('Eritrea'),
    ('Estonia'),
    ('Ethiopia'),
    ('Falkland Islands (Malvinas)'),
    ('Faroe Islands'),
    ('Fiji'),
    ('Finland'),
    ('France'),
    ('French Guiana'),
    ('French Polynesia'),
    ('French S. Territories'),
    ('Gabon'),
    ('Gambia'),
    ('Georgia'),
    ('Germany'),
    ('Ghana'),
    ('Gibraltar'),
    ('Greece'),
    ('Greenland'),
    ('Grenada'),
    ('Guadeloupe'),
    ('Guam'),
    ('Guatemala'),
    ('Guinea'),
    ('Guinea-bissau'),
    ('Guyana'),
    ('Haiti'),
    ('Honduras'),
    ('Hong Kong'),
    ('Hungary'),
    ('Iceland'),
    ('India'),
    ('Indonesia'),
    ('Iran'),
    ('Iraq'),
    ('Ireland'),
    ('Israel'),
    ('Italy'),
    ('Jamaica'),
    ('Japan'),
    ('Jordan'),
    ('Kazakhstan'),
    ('Kenya'),
    ('Kiribati'),
    ('Korea (North)'),
    ('Korea (South)'),
    ('Kuwait'),
    ('Kyrgyzstan'),
    ('Laos'),
    ('Latvia'),
    ('Lebanon'),
    ('Lesotho'),
    ('Liberia'),
    ('Libya'),
    ('Liechtenstein'),
    ('Lithuania'),
    ('Luxembourg'),
    ('Macau'),
    ('Macedonia'),
    ('Madagascar'),
    ('Malawi'),
    ('Malaysia'),
    ('Maldives'),
    ('Mali'),
    ('Malta'),
    ('Marshall Islands'),
    ('Martinique'),
    ('Mauritania'),
    ('Mauritius'),
    ('Mayotte'),
    ('Mexico'),
    ('Micronesia'),
    ('Moldova'),
    ('Monaco'),
    ('Mongolia'),
    ('Montserrat'),
    ('Morocco'),
    ('Mozambique'),
    ('Myanmar'),
    ('Namibia'),
    ('Nauru'),
    ('Nepal'),
    ('Netherlands'),
    ('Netherlands Antilles'),
    ('New Caledonia'),
    ('New Zealand'),
    ('Nicaragua'),
    ('Niger'),
    ('Nigeria'),
    ('Niue'),
    ('Norfolk Island'),
    ('Northern Mariana Islands'),
    ('Norway'),
    ('Oman'),
    ('Pakistan'),
    ('Palau'),
    ('Panama'),
    ('Papua New Guinea'),
    ('Paraguay'),
    ('Peru'),
    ('Philippines'),
    ('Pitcairn'),
    ('Poland'),
    ('Portugal'),
    ('Puerto Rico'),
    ('Qatar'),
    ('Reunion'),
    ('Romania'),
    ('Russian Federation'),
    ('Rwanda'),
    ('Saint Kitts And Nevis'),
    ('Saint Lucia'),
    ('St Vincent/Grenadines'),
    ('Samoa'),
    ('San Marino'),
    ('Sao Tome'),
    ('Saudi Arabia'),
    ('Senegal'),
    ('Seychelles'),
    ('Sierra Leone'),
    ('Singapore'),
    ('Slovakia'),
    ('Slovenia'),
    ('Solomon Islands'),
    ('Somalia'),
    ('South Africa'),
    ('Spain'),
    ('Sri Lanka'),
    ('St. Helena'),
    ('St.Pierre'),
    ('Sudan'),
    ('Suriname'),
    ('Swaziland'),
    ('Sweden'),
    ('Switzerland'),
    ('Syrian Arab Republic'),
    ('Taiwan'),
    ('Tajikistan'),
    ('Tanzania'),
    ('Thailand'),
    ('Togo'),
    ('Tokelau'),
    ('Tonga'),
    ('Trinidad And Tobago'),
    ('Tunisia'),
    ('Turkey'),
    ('Turkmenistan'),
    ('Tuvalu'),
    ('Uganda'),
    ('Ukraine'),
    ('United Arab Emirates'),
    ('United Kingdom'),
    ('Uruguay'),
    ('Uzbekistan'),
    ('Vanuatu'),
    ('Vatican City State'),
    ('Venezuela'),
    ('Viet Nam'),
    ('Virgin Islands (British)'),
    ('Virgin Islands (U.S.)'),
    ('Western Sahara'),
    ('Yemen'),
    ('Yugoslavia'),
    ('Zaire'),
    ('Zambia'),
    ('Zimbabwe')
]


#FOR NATIONALITY

nation=[('British'),
('Argentinian'),
('Australian'),
('Bahamian'),
('Belgian'),
('Brazilian'),
('Canadian'),
('Chinese'),
('Colombian'),
('Cuban'),
('Dominican'),
('Ecuadorean'),
('Salvadorean'),
('French'),
('German'),
('Guatemalan'),
('Haitian'),
('Honduran'),
('Indian'),
('Ireland'),
('Israeli'),
('Italian'),
('Japanese'),
('South Korean'),
('Mexican'),
('Dutch'),
('Philippine'),
('Spanish'),
('Swiss'),
('Taiwanese'),
('Venezuelan'),
('Vietnamese'),
('Afghan'),
('Albanian'),
('Algerian'),
('Samoan'),
('Andorran'),
('Angolan'),
('Armenian'),
('Austrian'),
('Azerbaijani'),
('Bahraini'),
('Bangladeshi'),
('Barbadian'),
('Belarusian'),
('Belizean'),
('Beninese'),
('Bermudian'),
('Bhutanese'),
('Bolivian'),
('Bosnian'),
('Botswanan'),
('Bulgarian'),
('Burundian'),
('Cambodian'),
('Cameroonian'),
('Cape Verdean'),
('Chadian'),
('Chilean'),
('Congolese'),
('Costa Rican'),
('Croat'),
('Cypriot'),
('Czech'),
('Danish'),
('Djiboutian'),
('Dominican'),
('Egyptian'),
('Eritrean'),
('Estonian'),
('Ethiopian'),
('Fijian'),
('Finnish'),
('Polynesian'),
('Gabonese'),
('Gambian'),
('Georgian'),
('Ghanaian'),
('Greek'),
('Grenadian'),
('Guinean'),
('Guyanese'),
('Hungarian'),
('Icelandic'),
('Indonesian'),
('Iranian'),
('Iraqi'),
('Jamaican'),
('Jordanian'),
('Kazakh'),
('Kenyan'),
('North Korean'),
('Kuwaiti'),
('Latvian'),
('Lebanese'),
('Liberian'),
('Libyan'),
('Lithuanian'),
('Luxembourg'),
('Madagascan'),
('Malawian'),
('Malaysian'),
('Maldivian'),
('Malian'),
('Maltese'),
('Mauritanian'),
('Mauritian'),
('Monacan'),
('Mongolian'),
('Montenegrin'),
('Moroccan'),
('Mozambican'),
('Namibian'),
('Nepalese'),
('New Zealand'),
('Nicaraguan'),
('Nigerien'),
('Nigerian'),
('Norwegian'),
('Omani'),
('Pakistani'),
('Panamanian'),
('Guinean'),
('Paraguayan'),
('Peruvian'),
('Polish'),
('Portuguese'),
('Qatari'),
('Romanian'),
('Rwandan'),
('Russian'),        
('Saudi Arabian'),
('Senegalese'),
('Serb Or Serbian'),
('Sierra Leonian'),
('Singaporean'),
('Slovak'),
('Slovenian'),
('Slomoni'),
('Somali'),
('South African'),
('Sri Lankan'),
('Sudanese'),
('Surinamese'),
('Swazi'),
('Tajik'),
('Thai'),
('Togolese'),
('Trinidadian'),
('Tunisian'),
('Turkish'),
('Turkoman'),
('Tuvaluan'),
('Ugandan'),
('Ukrainian'),
('Emirati'),
('American'),
('Uruguayan'),
('Uzbek'),
('Vanuatuan'),
('Yemeni'),
('Zambian'),
]


#MAIN MENU

def menu():
    c='y'
    while c=='y':
        print("\t\t---------------------------------------------------------------------")
        print("\t\t**********WELCOME TO AIRPORT MANAGEMENT SYSTEM*********")
        print("\t\t---------------------------------------------------------------------")
        print("\n\t\t#######BY ANUSHREE########")
        print("---------------------------------------------------------------------")
        print("                                  ^              ")
        print("                               /    \           ")
        print("                              |      |          ")
        print("                              |      |          ")
        print("                              |  A   |          ")
        print("                            / |  I   |\         ")
        print("                          /   |  R   |  \        ")
        print("                        /     |      |   \      ")
        print("                       /     /|  I   |\   \     ")
        print("                     /      / |  N   | \   \    ")
        print("                    /      /  |  D   |  \   \   ")
        print("                   /      /   |  I   |   \   \  ")
        print("                  /  ___ /    |  A   |    \___\  ")
        print("                             /|      |\           ")
        print("                          /   |      |  \         ")
        print("                        /     |      |    \       ")
        print("                      /       |      |     \       ")
        print("                     /        \      /      \      ")
        print("                   /______     \    /_____   \    ")
        print("                                \_/                ")


        
        print("1 : Flight_no")
        print("2 : Customer_Data")
        print("3 : Journey_details")
        print("4 : Payment_Details")
        print("5 : Exit")
        print("---------------------------------------------------------------------")
        choice=int(input("Enter Your Choice(1-5):"))
        if choice==1:
            flight_no()
        elif choice==2:
            customer_data()
        elif choice==3:
            journey()
        elif choice==4:
            payment()
        elif choice==5:
            break
        else:
            print("ERROR: invalid choice try again")
            break
    c=input("do u want to continue(y/n):")


#FLIGHT_NO TABLE

def flight_no():
    a='y'
    while a=='y':
        print("\t\t---------------------------------------------------------------------")
        print("\n\t\t#######FLIGHT NO########")
        print("---------------------------------------------------------------------")
        print("1 : add flight details")
        print("2 : show all flights details")
        print("3 : search a flight details")
        print("4 : deletion")
        print("5 : update flight information")
        print("6 : return to main_menu")
        print("\t\t----------------------------------------------------------------")
        choice=int(input("enter your Choice:1-6:"))
        if choice==1:
            flight_details()
        elif choice==2:
            show_flight_details()
        elif choice==3:
            search_flight_details()
        elif choice==4:
            delete_flight_details()
        elif choice==5:
            edit_flight_details()
        elif choice==6:
            break
        else:
            print("error : invalid choice try again")

    a=input("do u want to continue(y/n):")

#CUSTOMER TABLE

def customer_data():
    c='x'
    while c=='x':
        print("\t\t---------------------------------------------------------------------")
        print("\n\t\t#######CUSTOMER DATA########")
        print("-------------------------------------------------------------------------")
        print("1 : add customer details")
        print("2 : show all the customer details")
        print("3 : search for customer details")
        print("4 : deletion of customer data")
        print("5 : update the customer details")
        print("6 : return to main menu")
        print("-------------------------------------------------------------------------")
        choice=int(input("enter the choice(1-6):"))
        if choice==1:
            customer_details()
        elif choice==2:
            show_customer_details()
        elif choice==3:
            search_customer_details()
        elif choice==4:
            delete_customer_details()
        elif choice==5:
            edit_customer_details()
        elif choice==6:
            break
        else:
            print("error : invalid choice try again")
    c=input("do you want to continue(y/n):")

#JOURNEY TABLE

def journey():
    k='y'
    while k=='y':
        print("\t\t--------------------------------------------------------------")
        print("\n\t\t#######JOURNEY#######")
        print("-----------------------------------------------------------------")
        print("1 :add journey details")
        print("2 :show all flights going from source to destination")
        print("3 :search for a source or destination")
        print("4 :deletion")
        print("5 :update thejourney information")
        print("6 :return to main_menu")
        print("\t\t--------------------------------------------------------------")
        choice=int(input("enter the choice(1-6):"))
        if choice==1:
            journey_details()
        elif choice==2:
            show_journey_details()
        elif choice==3:
            search_journey_source_destination_details()
        elif choice==4:
            delete_journey_details()
        elif choice==5:
            edit_journey_details()
        elif choice==6:
            break
        else:
            print("error : invalid choice try again")
    k=input("do u want to continue(y/n):")
    
#PAYMENT TABLE

def payment():
    c='x'
    while c=='x':
        print("\t\t---------------------------------------------------------------------")
        print("\n\t\t#######PAYMENT########")
        print("-------------------------------------------------------------------------")
        print("1 : add payment details")
        print("2 : show all the payment details")
        print("3 : search for payment details")
        print("4 : deletion")
        print("5 : update the payment details")
        print("6 : return to main menu")
        print("-------------------------------------------------------------------------")
        choice=int(input("enter the choice(1-6):"))
        if choice==1:
            payment_details()
        elif choice==2:
            show_payment_details()
        elif choice==3:
            search_payment_details()
        elif choice==4:
            delete_payment_details()
        elif choice==5:
            edit_payment_details()
        elif choice==6:
            break
        else:
            print("error : invalid choice try again")
    c=input("do you want to continue(y/n):")



#CONNECTING WITH MYSQL

try:
    import mysql.connector
    print("type 1 existing user")
    print("type 2 new user")
    while 1==1:
        database_choice=int(input("enter your choice(1-2):"))
        if database_choice==1:
            db=mysql.connector.connect(host="localhost",user=user,passwd=password)
            cur=db.cursor()
            cur.execute("use airlinemgn")
            db.commit()
            break
        if database_choice==2:
            db=mysql.connector.connect(host="localhost",user=user,passwd=password)
            cur=db.cursor()
            cur.execute("create database if not exists airlinemgn")
            cur.execute("use airlinemgn")
            cur=db.cursor()                                #creating structure of newly created database
            cur.execute("create table flight_no(f_code int(5) primary key,f_name varchar(20),src varchar(20),dst varchar(20),cpcity int(5),class_code varchar(2),class_name varchar(20))")
            cur.execute("create table customer_data(PNRno int primary key,f_code int(5),passwrd varchar(10),address varchar(20),nationality varchar(10),name varchar(20),gender varchar(2),ph_no int(11))")
            cur.execute("create table journey(PNRno int(4) primary key,ticket_id varchar(20),f_code int(4),JNY_date date,arrtime TIME,deptime TIME,source varchar(20),destination varchar(20))")
            cur.execute("create table payment(PNRno int(4)primary key,paid_amount  int(10),pay_date  date,chequeno  int(9),cardno  int(11),phoneno  int(11))")
            db.commit()
            break
except:
    print("ERROR!, MAY BE U HAVE ENTER WRONG CHOICE")
    print("PLEASE FIRST CORRECT IT OR U WILL NOT ABLE TO USE THIS MANAGEMENT")



#FLIGHT DETAILS(FUTHER DATA OF TABLE)

def flight_details():
    import mysql.connector as con
    try:
        db=con.connect(host="localhost",user=user,passwd=password,database="airlinemgn")
        cur=db.cursor()
        f_code=int(input("enter flight no:"))
        f_name=input("enter flight name:")
        src=input("enter source of flight(FISRST LETTER IN CAPS):")
        dst=input("enter destination of flight(FISRST LETTER IN CAPS):")
        cpcity=int(input("enter the capacity:"))
        class_code=input("enter the class code(A/C/F/D/B/V):")
        class_name=input("enter the class name:")
        if src in country:
            if dst in country:
                cur.execute("insert into flight_no values('"+str(f_code)+"','"+f_name+"','"+src+"','"+dst+"','"+str(cpcity)+"','"+class_code+"','"+class_name+"')")
                db.commit()
                print("Record has been saved... in flight_no table.......")
        else:
            print("SORRY! ENTERED COUNTRY ARE NOT HAVE OUR FLIGHTS")
    except:
        print("error!(MAY BE DUE TO ENTERING WRONG DATA)")



def show_flight_details():
    import mysql.connector as con
    try:
        db=con.connect(host="localhost",user=user,passwd=password,database="airlinemgn")
        cur=db.cursor()
        cur.execute("select * from flight_no")
        rec=cur.fetchall()
        for x in rec:
            print (x)  
    except:
        print("error!(MAY BE DUE TO NO DATA PRESENT)")
                      


def search_flight_details():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        f_code=int(input("enter the flight code to be search:"))
        cur.execute("select * from flight_no where f_code='"+str(f_code)+"'")
        for x in cur:
            print(x)
        db.commit()
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER) ")



def delete_flight_details():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        f_code=int(input("enter the flight code to delete that record:"))
        cur.execute("delete from flight_no where f_code=%s",(f_code,))
        db.commit()
        print("record deleted successfully")
    except:
        print("error!(MAY BE DUE TO NO DATA PRESENT)")



def edit_flight_details():
    n='y'
    while n=='y':
        print("1: update flight name")
        print("2 : update source")
        print("3 : update destination")
        print("4 : update capacity")
        print("5 : update class code")
        print("6 : update class_name")
        print("7 : exit")
        choice=int(input("enter your choice(1-7):"))
        if choice==1:
            updatename()
        elif choice==2:
            updatesource()
        elif choice==3:
            updatedst()
        elif choice==4:
            updatecpcity()
        elif choice==5:
            updatecls_cd()
        elif choice==6:
            updatecls_nm()
        elif choice==7:
            break
        else:
            print("invalid input")
    n=input("do u want to update more records(y/n):")

def updatename():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        f_code=int(input("enter the flight code where u want to update that record:"))
        f_name=input("enter updated name:")
        cur.execute("update flight_no set f_name=%s where f_code=%s",(f_name,f_code))
        db.commit()
        print("record updated successfully")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")
  
def updatesource():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        f_code=int(input("enter the flight code where u want to update that record:"))
        src=input("enter updated source(FIRST LETTER IN CAPS):")
        if src in country:
            cur.execute("update flight_no set src=%s where f_code=%s",(src,f_code))
            db.commit()
            print("record updated successfully")
        else:
            print("SORRY! NO SUCH COUNTRY EXIST IN OUR RECORDS")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")
        

def updatedst():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        f_code=int(input("enter the flight code where u want to update that record:"))
        dst=input("enter updated destination(FIRST LETTER IN CAPS):")
        if dst in country:
            cur.execute("update flight_no set dst=%s where f_code=%s",(dst,f_code))
            db.commit()
            print("record updated successfully")
        else:
            print("SORRY! WE DONOT HAVE ANY FLIGHT FOR THIS COUNTRY")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")

def updatecpcity():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        f_code=int(input("enter the flight code where u want to update that record:"))
        cpcity=int(input("enter updated capacity:"))
        cur.execute("update flight_no set cpcity=%s where f_code=%s",(cpcity,f_code))
        db.commit()
        print("record updated successfully")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")

def updatecls_cd():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        f_code=int(input("enter the flight code where u want to update that record:"))
        class_code=input("enter updated name:")
        cur.execute("update flight_no set class_code=%s where f_code=%s",(class_code,f_code))
        db.commit()
        print("record updated successfully")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")

def updatecls_nm():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        f_code=int(input("enter the flight code where u want to update that record:"))
        class_name=input("enter updated name:")
        cur.execute("update flight_no set class_name=%s where f_code=%s",(class_name,f_code))
        db.commit()
        print("record updated successfully")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")

#CUSTOMER DATA(FUTHER DATA OF TABLE)

def customer_details():
    import mysql.connector as con
    try:
        db=con.connect(host="localhost",user=user,passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter pnr of flight(should be less that 6 digit):"))
        f_code=int(input("enter flight code:"))
        passwrd=input("enter password no:")
        address=input("enter your address:")
        nationality=input("enter your nationality(FIRST LETTER IN CAPS AFTER SPACE):")
        name=input("enter your name:")
        gender=input("enter your gender(M/F/O):")
        ph_no=int(input("enter your phone no(must be 10 digit or will not enter data):"))
        if nationality in nation:
            cur.execute("insert into customer_data values('"+str(PNRno)+"', '"+str(f_code)+"','"+passwrd+"','"+address+"','"+nationality+"','"+name+"','"+gender+"','"+str(ph_no)+"')")
            db.commit()
            print("record added successfully..... in customer data table")
        else:
            print("no such nationality exist in our records")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")

    

def show_customer_details():
    import mysql.connector as con
    try:
        db=con.connect(host="localhost",user=user,passwd=password,database="airlinemgn")
        cur=db.cursor()
        cur.execute("select * from customer_data")
        rec=cur.fetchall()
        for x in rec:
            print(x)
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")
    


def search_customer_details():
    import mysql.connector as con
    try:
        db=con.connect(host="localhost",user=user,passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno to be search:"))
        cur.execute("select * from customer_data where PNRno='"+str(PNRno)+"'")
        for x in cur:
            print(x)
        db.commit()
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")
    
    

def delete_customer_details():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno to delete that record:"))
        cur.execute("delete from customer_data where PNRno=%s",(PNRno,))
        db.commit()
        print("record deleted successfully")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")



def edit_customer_details():
    u='y'
    while u=='y':
        print("1 : update password")
        print("2 : update address")
        print("3 : update nationality")
        print("4 : update name")
        print("5 : update gender")
        print("6 : update phone no")
        print("7 : exit")
        choice=int(input("enter your choice"))
        if choice==1:
          updatepassword()
        elif choice==2:
            updateaddress()
        elif choice==3:
            updatenationality()
        elif choice==4:
            update_name()
        elif choice==5:
            updategender()
        elif choice==6:
            updateph_no()
        elif choice==7:    
            break
        else:
            print("invalid input")
    u=input("do u want to update more records(y/n)")

def updatepassword():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno where u want to update that record:"))
        passwrd=input("enter updated password:")
        cur.execute("update customer_data set passwrd=%s where PNRno =%s",(passwrd,PNRno))
        db.commit()
        print("record updated successfully")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")
  
def updateaddress():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno where u want to update that record:"))
        address=input("enter updated address:")
        cur.execute("update customer_data set address=%s where PNRno =%s",(address,PNRno))
        db.commit()
        print("record updated successfully")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")

def updatenationality():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno where u want to update that record:"))
        nationality=input("enter updated nationality(FIRST LETTER IN CAPS,eg:New Zealand):")
        if nationality in nation:
            cur.execute("update customer_data set nationality=%s where PNRno =%s",(nationality,PNRno))
            db.commit()
            print("record updated successfully")
        else:
            print("no such natioanlity exists in our record")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")

def update_name():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno where u want to update that record:"))
        name=input("enter updated name:")
        cur.execute("update customer_data set name=%s where PNRno =%s",(name,PNRno))
        db.commit()
        print("record updated successfully")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")

def updategender():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno where u want to update that record:"))
        gender=input("enter updated gender(M/F/O):")
        cur.execute("update customer_data set gender=%s where PNRno =%s",(gender,PNRno))
        db.commit()
        print("record updated successfully")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")

def updateph_no():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno where u want to update that record:"))
        ph_no=int(input("enter updated phoneno(10 DIGIT):"))
        cur.execute("update customer_data set ph_no=%s where PNRno =%s",(ph_no,PNRno))
        db.commit()
        print("record updated successfully")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")   
    
  

#JOURNEY DATA(FUTHER DATA OF TABLE)

def journey_details():
    import mysql.connector as con
    try:
        db=con.connect(host="localhost",user=user,passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the  PNRno:"))
        ticket_id=input("enter the ticket id:")
        f_code=int(input("enter the f_code:"))
        JNY_date=input("enter the flight date:")
        arrtime=input("enter the arrival time:")
        deptime=input("enter the depart time:")
        source=input("enter the source(FIRST LETTER IN CAPS):")
        destination=input("enter the destination(FIRST LETTER IN CAPS):")
        if source in country:
            if destination in country:
                cur.execute("insert into journey values('"+str(PNRno)+"','"+ticket_id+"','"+str(f_code)+"','"+JNY_date+"','"+arrtime+"','"+deptime+"','"+source+"','"+destination+"')")
                db.commit()
                print("Record has been saved...in journey table.......")
        else:
            print("SORRY! WE HAVE NO FLIGHTS FOR THIS COUNTRY")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")



def show_journey_details():
    import mysql.connector as con
    try:
        db=con.connect(host="localhost",user=user,passwd=password,database="airlinemgn")
        cur=db.cursor()
        cur.execute("select * from journey")
        rec=cur.fetchall()
        for x in rec:
            print(x)
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")



def search_journey_source_destination_details():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        source=input("enter the source to be search(FIRST LETTER IN CAPS):")
        destination=input("enter the destination to search(FIRST LETTER IN CAPS):")
        if source in country:
            if destination in country:
                cur.execute("select * from journey where source='"+source+"'and destination='"+destination+"'")
                for x in cur:
                    print(x)
                    db.commit()
        else:
            print("SORRY! NO SUCH COUNTRY PRESENT IN OUR RECORDS")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")



def delete_journey_details():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno to delete that record:"))
        cur.execute("delete  from journey where PNRno=%s",(PNRno,))
        db.commit()
        print("record deleted successfully")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")
        


def edit_journey_details():
    d='y'
    while d=='y':
        print("1 :update f_code")
        print("2 :update ticket_id")
        print("3 :update JNY_date")
        print("4 :update arrtime")
        print("5 :update deptime")
        print("6 :update source")
        print("7 :update destination")
        print("8 :exit ")
        choice=int(input("enter the choice"))
        if choice==1:
            updatef_code()
        elif choice==2:
            updateticket_id()
        elif choice==3:
            updateJNY_date()
        elif choice==4:
            updatearrtime()
        elif choice==5:
            updatedeptime()
        elif choice==6:
            updatesource()
        elif choice==7:
            updatedestination()
        elif choice==8:
            break
        else:
            print("invalid input")
    d=input("do u want to update more records(y/n)")

def updatef_code():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno where u want to update thet record:"))
        f_code=int(input("enter the updated name:"))
        cur.execute("update journey set f_code=%s where PNRno=%s",(f_code,PNRno))
        db.commit()
        print("record updated successfully")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")

def updateticket_id():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno where u want to update:"))
        ticket_id=input("enter the updated source")
        cur.execute("update journey set ticket_id=%s where PNRno=%s",(ticket_id,PNRno))
        db.commit()
        print("record updated successfully")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")

def updateJNY_date():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno where u wnt to update that record"))
        JNY_date=input("enter the updated date:")
        cur.execute("update journey set JNY_date=%s where PNRno=%s",(JNY_date,PNRno))
        db.commit()
        print("record updated successfully")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")

def updatearrtime():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno where u wnt to update that record"))
        arrtime=input("enter updated arrtime")
        cur.execute("update journey set arrtime=%s where PNRno=%s",(arrtime,PNRno))
        db.commit()
        print("record updated successfully")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")
        
def updatedeptime():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno where u wnt to update the record"))
        deptime=input("enter updated deptime:")
        cur.execute("update journey set deptime=%s where PNRno=%s",(deptime,PNRno))
        db.commit()
        print("record updated successfully")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")      
         
def updatesource():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno where u wnt to update that record:"))
        source=input("enter updated source(FIRST LETTER IN CAPS):")
        if source in country:
            cur.execute("update journey set source=%s where PNRno=%s",(source,PNRno))
            db.commit()
            print("record updated successfully")
        else:
            print("SORRY! NO SUCH COUNTRY ES=XISTS IN OUR RECORD")

    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")

def updatedestination():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno where u wnt to update that record:"))
        destination=input("enter updated destination(FISRST LETTER IN CAPS):")
        if source in country:
            cur.execute("update journey set destination=%s where PNRno=%s",(destination,PNRno))
            db.commit()
            print("record updated successfully")
        else:
            print("SORRY! NO SUCH COUNTRY EXISTS IN OUR RECORD")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")
        
#PAYMENT DATA(FUTHER DATA OF PAYMENT)

def payment_details():
    c='y'
    while c=='y':
        print("## WANT TO PAY THOUGH CHECK OR CARD##")
        print("1 :IF WANT TO PAY THROUGH CHEQUE")
        print("2 :IF WANT TO PAY THROUGH CARD")
        c=int(input("enter your choice of payment:"))
        if c==1:
            payment_check_details()
        elif c==2:
            payment_card_details()
        else:
            print("invalid choice")
    c=input("wants to continue(y/n)..")            

    
def payment_check_details():
    import mysql.connector as con
    try:
        db=con.connect(host="localhost",user=user,passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno:"))
        paid_amount=int(input("enter the paid amount:"))
        pay_date=input("enter the pay date:")
        chequeno=int(input("enter the chequeno(should be of 9 digits or error):"))
        phoneno=int(input("enter the phoneno:"))
        cur.execute("insert into payment(PNRno,paid_amount,pay_date,chequeno,phoneno) values('"+str(PNRno)+"','"+str(paid_amount)+"','"+pay_date+"','"+str(chequeno)+"','"+str(phoneno)+"')")
        db.commit()
        print("Record has been saved .....in payment table.......")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")

def payment_card_details():
    import mysql.connector as con
    try:
        db=con.connect(host="localhost",user=user,passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno:"))
        paid_amount=int(input("enter the paid amount:"))
        pay_date=input("enter the pay date:")
        cardno=int(input("enter the cardno:"))
        phoneno=int(input("enter the phoneno:"))
        cur.execute("insert into payment(PNRno,paid_amount,pay_date,cardno,phoneno) values('"+str(PNRno)+"','"+str(paid_amount)+"','"+pay_date+"','"+str(cardno)+"','"+str(phoneno)+"')")
        db.commit()
        print("Record has been saved .....in payment table.......")        
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")        
    


def show_payment_details():
    import mysql.connector as con
    try:
        db=con.connect(host="localhost",user=user,passwd=password,database="airlinemgn")
        cur=db.cursor()
        cur.execute("select * from payment")
        rec=cur.fetchall()
        for x in rec:
            print(x)
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")
    


def search_payment_details():
    import mysql.connector as con
    try:
        db=con.connect(host="localhost",user=user,passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno to be search:"))
        cur.execute("select * from payment where PNRno='"+str(PNRno)+"'")
        for x in cur:
            print(x)
        db.commit()
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")
    
    

def delete_payment_details():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno to delete that record:"))
        cur.execute("delete from payment where PNRno=%s",(PNRno,))
        db.commit()
        print("record deleted successfully")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")



def edit_payment_details():
    u='y'
    while u=='y':
        print("1 : update paid_amount")
        print("2 : update pay_date")
        print("3 : update chequeno")
        print("4 : update cardno")
        print("5 : update phoneno")
        print("6 : exit")
        choice=int(input("enter your choice"))
        if choice==1:
          updatepaid_amount()
        elif choice==2:
            updatepay_date()
        elif choice==3:
            updatechequeno()
        elif choice==4:
            updatecardno()
        elif choice==5:
            updatephoneno()
        elif choice==6:
            break
        else:
            print("invalid input")
    u=input("do u want to update more records(y/n)")
      
def updatepaid_amount():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno where u want to update that record:"))
        paid_amount=int(input("enter updated paid_amount:"))
        cur.execute("update payment set paid_amount=%s where PNRno =%s",(paid_amount,PNRno))
        db.commit()
        print("record updated successfully")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")

  
def updatepay_date():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno where u want to update that record:"))
        pay_date=input("enter updated pay_date:")
        cur.execute("update payment set pay_date=%s where PNRno =%s",(pay_date,PNRno))
        db.commit()
        print("record updated successfully")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")

    
def updatechequeno():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno where u want to update that record:"))
        chequeno=int(input("enter updated chequeno:"))
        cur.execute("update payment set chequeno=%s where PNRno =%s",(chequeno,PNRno))
        db.commit()
        print("record updated successfully")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")

def updatecardno():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno where u want to update that record:"))
        cardno=int(input("enter updated cardno:"))
        cur.execute("update payment set cardno=%s where PNRno =%s",(cardno,PNRno))
        db.commit()
        print("record updated successfully")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")

def updatephoneno():
    import mysql.connector as con
    try:
        db=con.connect(user=user,host="localhost",passwd=password,database="airlinemgn")
        cur=db.cursor()
        PNRno=int(input("enter the PNRno where u want to update that record:"))
        phoneno=int(input("enter updated phoneno:"))
        cur.execute("update payment set phoneno=%s where PNRno =%s",(phoneno,PNRno))
        db.commit()
        print("record updated successfully")
    except:
        print("error!(MAY BE DUE TO WRONG DATA ENTER OR DATA NOT PRESENT)")
    
#MAIN PROGRAM CALL       
menu()

