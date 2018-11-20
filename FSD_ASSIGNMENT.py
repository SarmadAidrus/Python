import datetime
def seatingmodule(Customer_Ferry_Id,Customer_Trip_Time):
        
        now = datetime.datetime.now()
        myfile= open("FERRYTICKETINGDATA.txt","a+")
        myfile.write("****************************************\n")
        myfile.write("*  SEATING ARRANGEMENT MODULE          *\n")
        myfile.write("****************************************\n")                                      #**********************************************************
        myfile.write("*  DATE:")                                                                        #FILE WRITING MODULE. THIS MODULE WRITES  INTO THE FILE 
        day=str(now.day)                                                                                #FERRTICKETINGDATA.txt. IT STORES INFORMATION OF THE DATE
        myfile.write(day+" ")                                                                           #CUSTOMER ID AND TRIPTIME. IT SHOWS THE FERRY DETAILS OF THE                                                         
        time=str(now.strftime("%B"))                                                                    #SEAT THAT HAS BEEN BOOKED.
        myfile.write(time+" ")                                                                          #**********************************************************
        year=str(now.year)
        myfile.write(year+"                 *\n")
        myfile.write("****************************************\n")
        myfile.write("*  FERRY ID: ")
        myfile.write(Customer_Ferry_Id+"")
        myfile.write("    *\n")
        myfile.write("****************************************\n")
        myfile.write("*  TRIPTIME: ")
        myfile.write(Customer_Trip_Time+"")
        myfile.write("   *\n")
        myfile.write("****************************************\n")
        myfile.write("*  BUSINESS CLASS                      *\n")
        myfile.write("****************************************\n")
        
        
        print("****************************************")
        print("*  SEATING ARRANGEMENT MODULE          *")
        print("****************************************")                                               #**********************************************                        
        print("*  DATE:","%d" % now.day,now.strftime("%B"),"%d" % now.year,"               *")          #DISPLAY OF DATE, CUSTOMER FERRYID AND TRIPTIME
        print("****************************************")                                               #STORES CURRENT DATE FROM THE SYSTEM.THIS IS A                                        
        print("*  FERRY ID: ",Customer_Ferry_Id,"  *")                                                  #CONSOLE DISPLAY.                                
        print("****************************************")                                               #**********************************************
        print("*  TRIPTIME: ",Customer_Trip_Time," *")
        print("****************************************")
        print("*  BUSINESS CLASS                      *")
        print("****************************************")
        print("*  ",end="")
        myfile.write("*  ")
        if(Customer_Ferry_Id=="001-PENANG TO LANGKAWI"):                                                #**********************************************************                                                       
                x=0                                                                                     #THIS MODULE CHECKS IF THE FERRY ID SELECTED BY THE USER IS
                while(x<10):                                                                            #EQUAL TO THE ACTUAL ONES IN THE FERRYID LIST, IT THEN 
                    print(Ferry1[0][x],end="   *   ")                                                   #DISPLAYS THE BUISNESS CLASS OF THAT FERRY.THIS MODULE IS
                    ferrydata=str(Ferry1[0][x])                                                         #COMPRISED OF INDEXING OF THE LIST, TRANSVERSING AND
                    myfile.write(ferrydata+"   *   ")                                                   #PRINTING IN A WHILE LOOP THAT WORKS UPTO THE TOTAL NUMBER              
                    if(x==4):                                                                           #OF SEATS OF THE BUISNESS CLASS OF THE FERRY. 
                        print("\t")                                                                     #**********************************************************
                        myfile.write(" \n")                                                                                
                        print("*  ",end="")
                        myfile.write("* ")
                        myfile.write(" ")                                                            
                    x=x+1                                                                               
        elif(Customer_Ferry_Id=="002-PENANG TO LANGKAWI"):                                              
                x=0
                while(x<10):
                    print(Ferry2[0][x],end="   *   ")
                    ferrydata=str(Ferry2[0][x])
                    myfile.write(ferrydata+"   *   ")
                    if(x==4):
                        print("\t")                                                                     
                        myfile.write(" \n")                                                                                
                        print("*  ",end="")
                        myfile.write("* ")
                        myfile.write(" ")
                    x=x+1
             
        elif(Customer_Ferry_Id=="003-PENANG TO LANGKAWI"):
                x=0
                while(x<10):
                    print(Ferry3[0][x],end="   *   ")
                    ferrydata=str(Ferry3[0][x])
                    myfile.write(ferrydata+"   *   ")
                    if(x==4):
                        print("\t")                                                                     
                        myfile.write(" \n")                                                                                
                        print("*  ",end="")
                        myfile.write("* ")
                        myfile.write(" ")
                    x=x+1
            
        elif(Customer_Ferry_Id=="004-PENANG TO LANGKAWI"):
                x=0
                while(x<10):
                    print(Ferry4[0][x],end="   *   ")
                    ferrydata=str(Ferry4[0][x])
                    myfile.write(ferrydata+"   *   ")
                    if(x==4):
                        print("\t")                                                                     
                        myfile.write(" \n")                                                                                
                        print("*  ",end="")
                        myfile.write("* ")
                        myfile.write(" ")
                    x=x+1
            
        elif(Customer_Ferry_Id=="005-LANGKAWI TO PENANG"):
                x=0
                while(x<10):
                    print(Ferry5[0][x],end="   *   ")
                    ferrydata=str(Ferry5[0][x])
                    myfile.write(ferrydata+"   *   ")
                    if(x==4):
                        print("\t")                                                                     
                        myfile.write(" \n")                                                                                
                        print("*  ",end="")
                        myfile.write("* ")
                        myfile.write(" ")
                    x=x+1
            
        elif(Customer_Ferry_Id=="006-LANGKAWI TO PENANG"):
                x=0
                while(x<10):
                    print(Ferry6[0][x],end="   *   ")
                    ferrydata=str(Ferry6[0][x])
                    myfile.write(ferrydata+"   *   ")
                    if(x==4):
                        print("\t")                                                                     
                        myfile.write(" \n")                                                                                
                        print("*  ",end="")
                        myfile.write("* ")
                        myfile.write(" ")
                    x=x+1
            
        elif(Customer_Ferry_Id=="007-LANGKAWI TO PENANG"):
                x=0
                while(x<10):
                    print(Ferry7[0][x],end="   *   ")
                    ferrydata=str(Ferry7[0][x])
                    myfile.write(ferrydata+"   *   ")
                    if(x==4):
                        print("\t")                                                                     
                        myfile.write(" \n")                                                                                
                        print("*  ",end="")
                        myfile.write("* ")
                        myfile.write(" ")
                    x=x+1
           
        elif(Customer_Ferry_Id=="008-LANGKAWI TO PENANG"):
                x=0
                while(x<10):
                    print(Ferry8[0][x],end="   *   ")
                    ferrydata=str(Ferry7[0][x])
                    myfile.write(ferrydata+"   *   ")
                    if(x==4):
                        print("\t")                                                                     
                        myfile.write(" \n")                                                                                
                        print("*  ",end="")
                        myfile.write("* ")
                        myfile.write(" ")
                    x=x+1
        print("\t")
        myfile.write("\n")
        myfile.write("****************************************\n")
        myfile.write("*  ECONOMY CLASS                       *\n")
        myfile.write("****************************************\n")                                      #**********************************************************      
        print("****************************************")                                               #THIS MODULE CHECKS IF THE FERRY ID SELECTED BY THE USER IS
        print("*  ",end="")                                                                             #EQUAL TO THE ACTUAL ONES IN THE FERRYID LIST, IT THEN
        print("ECONOMY CLASS                       *")                                                  #DISPLAYS THE ECONOMY CLASS OF THAT FERRY.THIS MODULE IS 
        print("****************************************")                                               #COMPRISED OF INDEXING OF THE LIST, TRANSVERSING AND
        print("*  ",end="")                                                                             #PRINTING IN A WHILE LOOP THAT WORKS UPTO THE TOTAL NUMBER
        myfile.write("*  ")                                                                             #OF SEATS OF THE ECONOMY CLASS OF THE FERRY.
        if(Customer_Ferry_Id=="001-PENANG TO LANGKAWI"):                                                #THIS MODULE ALSO WRITES THE ELEMENTS OF THE LISTS TO THE 
                x=1                                                                                     #FERRYTICKETINGDATA.txt.                                                                                   
                while(x<=40):                                                                           #**********************************************************
                    print(Ferry1[1][x-1],end="   *   ")
                    ferrydata=str(Ferry1[1][x-1])
                    myfile.write(ferrydata+"   *  ")
                    myfile.write(" ")
                    
                    if(x==40 and x%5==0):
                        print("\t")
                        myfile.write("\n")
                    elif(x%5==0):
                        print("\t")                                                                     
                        myfile.write(" \n")                                                                                
                        print("*  ",end="")
                        myfile.write("* ")
                        myfile.write(" ")
                    x=x+1
        elif(Customer_Ferry_Id=="002-PENANG TO LANGKAWI"):
                x=1
                while(x<=40):
                    print(Ferry2[1][x-1],end="   *   ")
                    ferrydata=str(Ferry2[1][x-1])
                    myfile.write(ferrydata+"   *  ")
                    myfile.write(" ")
                    if(x==40 and x%5==0):
                        print("\t")
                    elif(x%5==0):
                        print("\t")                                                                     
                        myfile.write(" \n")                                                                                
                        print("*  ",end="")
                        myfile.write("* ")
                        myfile.write(" ")
                    x=x+1
        elif(Customer_Ferry_Id=="003-PENANG TO LANGKAWI"):
                x=1
                while(x<=40):
                    print(Ferry3[1][x-1],end="   *   ")
                    ferrydata=str(Ferry3[1][x-1])
                    myfile.write(ferrydata+"   *  ")
                    myfile.write(" ")
                    if(x==40 and x%5==0):
                        print("\t")
                    elif(x%5==0):
                        print("\t")                                                                     
                        myfile.write(" \n")                                                                                
                        print("*  ",end="")
                        myfile.write("* ")
                        myfile.write(" ")
                    x=x+1
        elif(Customer_Ferry_Id=="004-PENANG TO LANGKAWI"):
                x=1
                while(x<=40):
                    print(Ferry4[1][x-1],end="   *   ")
                    ferrydata=str(Ferry4[1][x-1])
                    myfile.write(ferrydata+"   *  ")
                    myfile.write(" ")
                    if(x==40 and x%5==0):
                        print("\t")
                    elif(x%5==0):
                        print("\t")                                                                     
                        myfile.write(" \n")                                                                                
                        print("*  ",end="")
                        myfile.write("* ")
                        myfile.write(" ")
                    x=x+1
        elif(Customer_Ferry_Id=="005-LANGKAWI TO PENANG"):
                x=1
                while(x<=40):
                    print(Ferry5[1][x-1],end="   *   ")
                    ferrydata=str(Ferry5[1][x-1])
                    myfile.write(ferrydata+"   *  ")
                    myfile.write(" ")
                    if(x==40 and x%5==0):
                        print("\t")
                    elif(x%5==0):
                        print("\t")                                                                     
                        myfile.write(" \n")                                                                                
                        print("*  ",end="")
                        myfile.write("* ")
                        myfile.write(" ")
                    x=x+1
        elif(Customer_Ferry_Id=="006-LANGKAWI TO PENANG"):
                x=1
                while(x<=40):
                    print(Ferry6[1][x-1],end="   *   ")
                    ferrydata=str(Ferry6[1][x-1])
                    myfile.write(ferrydata+"   *  ")
                    myfile.write(" ")
                    if(x==40 and x%5==0):
                        print("\t")
                    elif(x%5==0):
                        print("\t")                                                                     
                        myfile.write(" \n")                                                                                
                        print("*  ",end="")
                        myfile.write("* ")
                        myfile.write(" ")
                    x=x+1
        elif(Customer_Ferry_Id=="007-LANGKAWI TO PENANG"):
                x=1
                while(x<=40):
                    print(Ferry7[1][x-1],end="   *   ")
                    ferrydata=str(Ferry7[1][x-1])
                    myfile.write(ferrydata+"   *  ")
                    myfile.write(" ")
                    if(x==40 and x%5==0):
                        print("\t")
                    elif(x%5==0):
                        print("\t")                                                                     
                        myfile.write(" \n")                                                                                
                        print("*  ",end="")
                        myfile.write("* ")
                        myfile.write(" ")
                    x=x+1
        elif(Customer_Ferry_Id=="008-LANGKAWI TO PENANG"):
                x=1
                while(x<=40):
                    print(Ferry8[1][x-1],end="   *   ")
                    ferrydata=str(Ferry8[1][x-1])
                    myfile.write(ferrydata+"   *  ")
                    myfile.write(" ")
                    if(x==40 and x%5==0):
                        print("\t")
                    elif(x%5==0):
                        print("\t")                                                                     
                        myfile.write(" \n")                                                                                
                        print("*  ",end="")
                        myfile.write("* ")
                        myfile.write(" ")
                    x=x+1
        print("****************************************")
        myfile.write("****************************************\n")
        print("\t")

def purchasemodule(Customer_Ferry_Id,Customer_Trip_Time):                                               #**********************************************************
    while True:                                                                                         #PURCHASE MODULE IS ACCESSED TO BOOK TICKETS.IT GIVES THE 
        print("PURCHASING TICKET MODULE")                                                               #USER THE CHOICE TO SELECT BETWEEN BUISNESS CLASS OR         
        print("\t B-Business Class")                                                                    #ECONOMY OF THE FERRY HE HAS SELECTED.THE LOOP CHECKS        
        print("\t E-Economy Class")                                                                     #IF THE ELEMENTS OF THE SELECTED CLASS IS 0.THEN IT MAKES                         
        print("\t M-Main Menu")                                                                         #IT TO 1.THE COUNTER IN THIS MODULE CHECKS IF ALL SEATS OF                                        
        choice2=input("Please Enter Your Selection: ")                                                  #A CERTAIN CLASS ARE BOOKED THEN IT GIVES USEE A MESSAGE TO
        if(choice2=="B"):                                                                               #THAT ALL SEATS ARE BOOKED AND SELECT THE OTHER CLASS TO 
            if(Customer_Ferry_Id=="001-PENANG TO LANGKAWI"):                                            #BOOK A SEAT.                                
                x=0                                                                                     #**********************************************************
                while(x<10):
                    if(Ferry1[0][x]==0):
                        Ferry1[0][x]=1
                        print("****************************************")
                        print("* YOUR DESIRED SEAT HAS BEEN BOOKED    *")
                        print("****************************************")
                        counter=0
                        break
                    elif(Ferry1[0][x]==1):
                        counter=1
                        x=x+1
                if(counter==0):
                    x=x+1
                elif(counter==1):
                    print("****************************************")
                    print("* ALL SEATS ARE BOOKED                 *")
                    print("* TAKING YOU TO THE MAIN MENU          *")
                    print("* CHOOSE ECONOMY CLASS TO BOOK A SEAT  *")
                    print("****************************************")
                x=x+1
            
            elif(Customer_Ferry_Id=="002-PENANG TO LANGKAWI"):
                x=0
                while(x<10):
                    if(Ferry2[0][x]==0):
                        Ferry2[0][x]=1
                        print("****************************************")
                        print("* YOUR DESIRED SEAT HAS BEEN BOOKED    *")
                        print("****************************************")
                        counter=0
                        break
                    elif(Ferry2[0][x]==1):
                        counter=1
                        x=x+1
                if(counter==0):
                    x=x+1
                elif(counter==1):
                    print("****************************************")
                    print("* ALL SEATS ARE BOOKED                 *")
                    print("* TAKING YOU TO THE MAIN MENU          *")
                    print("* CHOOSE ECONOMY CLASS TO BOOK A SEAT  *")
                    print("****************************************")
                x=x+1
             
            elif(Customer_Ferry_Id=="003-PENANG TO LANGKAWI"):
                x=0
                while(x<10):
                    if(Ferry3[0][x]==0):
                        Ferry3[0][x]=1
                        print("****************************************")
                        print("* YOUR DESIRED SEAT HAS BEEN BOOKED    *")
                        print("****************************************")
                        counter=0
                        break
                    elif(Ferry3[0][x]==1):
                        counter=1
                        x=x+1
                if(counter==0):
                    x=x+1
                elif(counter==1):
                    print("****************************************")
                    print("* ALL SEATS ARE BOOKED                 *")
                    print("* TAKING YOU TO THE MAIN MENU          *")
                    print("* CHOOSE ECONOMY CLASS TO BOOK A SEAT  *")
                    print("****************************************")
                x=x+1
            
            elif(Customer_Ferry_Id=="004-PENANG TO LANGKAWI"):
                x=0
                while(x<10):
                    if(Ferry4[0][x]==0):
                        Ferry4[0][x]=1
                        print("****************************************")
                        print("* YOUR DESIRED SEAT HAS BEEN BOOKED    *")
                        print("****************************************")
                        counter=0
                        break
                    elif(Ferry4[0][x]==1):
                        counter=1
                        x=x+1
                if(counter==0):
                    x=x+1
                elif(counter==1):
                    print("****************************************")
                    print("* ALL SEATS ARE BOOKED                 *")
                    print("* TAKING YOU TO THE MAIN MENU          *")
                    print("* CHOOSE ECONOMY CLASS TO BOOK A SEAT  *")
                    print("****************************************")
                x=x+1
            
            elif(Customer_Ferry_Id=="005-LANGKAWI TO PENANG"):
                x=0
                while(x<10):
                    if(Ferry5[0][x]==0):
                        Ferry5[0][x]=1
                        print("****************************************")
                        print("* YOUR DESIRED SEAT HAS BEEN BOOKED    *")
                        print("****************************************")
                        counter=0
                        break
                    elif(Ferry5[0][x]==1):
                        counter=1
                        x=x+1
                if(counter==0):
                    x=x+1
                elif(counter==1):
                    print("****************************************")
                    print("* ALL SEATS ARE BOOKED                 *")
                    print("* TAKING YOU TO THE MAIN MENU          *")
                    print("* CHOOSE ECONOMY CLASS TO BOOK A SEAT  *")
                    print("****************************************")
                x=x+1
            
            elif(Customer_Ferry_Id=="006-LANGKAWI TO PENANG"):
                x=0
                while(x<10):
                    if(Ferry6[0][x]==0):
                        Ferry6[0][x]=1
                        print("****************************************")
                        print("* YOUR DESIRED SEAT HAS BEEN BOOKED    *")
                        print("****************************************")
                        counter=0
                        break
                    elif(Ferry6[0][x]==1):
                        counter=1
                        x=x+1
                if(counter==0):
                    x=x+1
                elif(counter==1):
                    print("****************************************")
                    print("* ALL SEATS ARE BOOKED                 *")
                    print("* TAKING YOU TO THE MAIN MENU          *")
                    print("* CHOOSE ECONOMY CLASS TO BOOK A SEAT  *")
                    print("****************************************")
                x=x+1
            
            elif(Customer_Ferry_Id=="007-LANGKAWI TO PENANG"):
                x=0
                while(x<10):
                    if(Ferry7[0][x]==0):
                        Ferry7[0][x]=1
                        print("****************************************")
                        print("* YOUR DESIRED SEAT HAS BEEN BOOKED    *")
                        print("****************************************")
                        counter=0
                        break
                    elif(Ferry7[0][x]==1):
                        counter=1
                        x=x+1
                if(counter==0):
                    x=x+1
                elif(counter==1):
                    print("****************************************")
                    print("* ALL SEATS ARE BOOKED                 *")
                    print("* TAKING YOU TO THE MAIN MENU          *")
                    print("* CHOOSE ECONOMY CLASS TO BOOK A SEAT  *")
                    print("****************************************")
                x=x+1
           
            elif(Customer_Ferry_Id=="008-LANGKAWI TO PENANG"):
                x=0
                while(x<10):
                    if(Ferry8[0][x]==0):
                        Ferry8[0][x]=1
                        print("****************************************")
                        print("* YOUR DESIRED SEAT HAS BEEN BOOKED    *")
                        print("****************************************")
                        counter=0
                        break
                    elif(Ferry8[0][x]==1):
                        counter=1
                        x=x+1
                if(counter==0):
                    x=x+1
                elif(counter==1):
                    print("****************************************")
                    print("* ALL SEATS ARE BOOKED                 *")
                    print("* TAKING YOU TO THE MAIN MENU          *")
                    print("* CHOOSE ECONOMY CLASS TO BOOK A SEAT  *")
                    print("****************************************")
                x=x+1
            
            
        elif(choice2=="E"):
                                                                                                        #**********************************************************
            print("ECONOMY CLASS")                                                                      #PURCHASE MODULE IS ACCESSED TO BOOK TICKETS.IT GIVES THE
            if(Customer_Ferry_Id=="001-PENANG TO LANGKAWI"):                                            #USER THE CHOICE TO SELECT BETWEEN BUISNESS CLASS OR
                    x=0                                                                                 #ECONOMY OF THE FERRY HE HAS SELECTED.THE LOOP CHECKS
                    while(x<40):                                                                        #IF THE ELEMENTS OF THE SELECTED CLASS IS 0.THEN IT MAKES
                        if(Ferry1[1][x]==0):                                                            #IT TO 1.THE COUNTER IN THIS MODULE CHECKS IF ALL SEATS OF
                            Ferry1[1][x]=1                                                              #A CERTAIN CLASS ARE BOOKED THEN IT GIVES USEE A MESSAGE TO
                            print("****************************************")                           #THAT ALL SEATS ARE BOOKED AND SELECT THE OTHER CLASS TO
                            print("* YOUR DESIRED SEAT HAS BEEN BOOKED    *")                           #BOOK A SEAT.
                            print("****************************************")                           #**********************************************************
                            counter=0
                            break
                        elif(Ferry1[1][x]==1):
                            counter=1
                            x=x+1
                    if(counter==0):
                        x=x+1
                    elif(counter==1):
                        print("*****************************************")
                        print("* ALL SEATS ARE BOOKED                  *")
                        print("* TAKING YOU TO THE MAIN MENU           *")
                        print("* CHOOSE BUISNESS CLASS TO BOOK A SEAT  *")
                        print("*****************************************")
                    x=x+1
            elif(Customer_Ferry_Id=="002-PENANG TO LANGKAWI"):
                    x=0
                    while(x<40):
                        if(Ferry2[1][x]==0):
                            Ferry2[1][x]=1
                            print("****************************************")
                            print("* YOUR DESIRED SEAT HAS BEEN BOOKED    *")
                            print("****************************************")
                            counter=0
                            break
                        elif(Ferry2[1][x]==1):
                            counter=1
                            x=x+1
                    if(counter==0):
                        x=x+1
                    elif(counter==1):
                        print("*****************************************")
                        print("* ALL SEATS ARE BOOKED                  *")
                        print("* TAKING YOU TO THE MAIN MENU           *")
                        print("* CHOOSE BUISNESS CLASS TO BOOK A SEAT  *")
                        print("*****************************************")
                    x=x+1
            elif(Customer_Ferry_Id=="003-PENANG TO LANGKAWI"):
                    x=0
                    while(x<40):
                        if(Ferry3[1][x]==0):
                            Ferry3[1][x]=1
                            print("****************************************")
                            print("* YOUR DESIRED SEAT HAS BEEN BOOKED    *")
                            print("****************************************")
                            counter=0
                            break
                        elif(Ferry3[1][x]==1):
                            counter=1
                            x=x+1
                    if(counter==0):
                        x=x+1
                    elif(counter==1):
                        print("*****************************************")
                        print("* ALL SEATS ARE BOOKED                  *")
                        print("* TAKING YOU TO THE MAIN MENU           *")
                        print("* CHOOSE BUISNESS CLASS TO BOOK A SEAT  *")
                        print("*****************************************")
                    x=x+1
            elif(Customer_Ferry_Id=="004-PENANG TO LANGKAWI"):
                    x=0
                    while(x<40):
                        if(Ferry4[1][x]==0):
                            Ferry4[1][x]=1
                            print("****************************************")
                            print("* YOUR DESIRED SEAT HAS BEEN BOOKED    *")
                            print("****************************************")
                            counter=0
                            break
                        elif(Ferry4[1][x]==1):
                            counter=1
                            x=x+1
                    if(counter==0):
                        x=x+1
                    elif(counter==1):
                        print("*****************************************")
                        print("* ALL SEATS ARE BOOKED                  *")
                        print("* TAKING YOU TO THE MAIN MENU           *")
                        print("* CHOOSE BUISNESS CLASS TO BOOK A SEAT  *")
                        print("*****************************************")
                    x=x+1
            elif(Customer_Ferry_Id=="005-LANGKAWI TO PENANG"):
                    x=0
                    while(x<40):
                        if(Ferry5[1][x]==0):
                            Ferry5[1][x]=1
                            print("****************************************")
                            print("* YOUR DESIRED SEAT HAS BEEN BOOKED    *")
                            print("****************************************")
                            counter=0
                            break
                        elif(Ferry5[1][x]==1):
                            counter=1
                            x=x+1
                    if(counter==0):
                        x=x+1
                    elif(counter==1):
                        print("*****************************************")
                        print("* ALL SEATS ARE BOOKED                  *")
                        print("* TAKING YOU TO THE MAIN MENU           *")
                        print("* CHOOSE BUISNESS CLASS TO BOOK A SEAT  *")
                        print("*****************************************")
                    x=x+1
            elif(Customer_Ferry_Id=="006-LANGKAWI TO PENANG"):
                    x=0
                    while(x<40):
                        if(Ferry6[1][x]==0):
                            Ferry6[1][x]=1
                            print("****************************************")
                            print("* YOUR DESIRED SEAT HAS BEEN BOOKED    *")
                            print("****************************************")
                            counter=0
                            break
                        elif(Ferry6[1][x]==1):
                            counter=1
                            x=x+1
                    if(counter==0):
                        x=x+1
                    elif(counter==1):
                        print("*****************************************")
                        print("* ALL SEATS ARE BOOKED                  *")
                        print("* TAKING YOU TO THE MAIN MENU           *")
                        print("* CHOOSE BUISNESS CLASS TO BOOK A SEAT  *")
                        print("*****************************************")
                    x=x+1
            elif(Customer_Ferry_Id=="007-LANGKAWI TO PENANG"):
                    x=0
                    while(x<40):
                        if(Ferry7[1][x]==0):
                            Ferry7[1][x]=1
                            print("****************************************")
                            print("* YOUR DESIRED SEAT HAS BEEN BOOKED    *")
                            print("****************************************")
                            counter=0
                            break
                        elif(Ferry7[1][x]==1):
                            counter=1
                            x=x+1
                    if(counter==0):
                        x=x+1
                    elif(counter==1):
                        print("*****************************************")
                        print("* ALL SEATS ARE BOOKED                  *")
                        print("* TAKING YOU TO THE MAIN MENU           *")
                        print("* CHOOSE BUISNESS CLASS TO BOOK A SEAT  *")
                        print("*****************************************")
                    x=x+1
            elif(Customer_Ferry_Id=="008-LANGKAWI TO PENANG"):
                    x=0
                    while(x<40):
                        if(Ferry8[1][x]==0):
                            Ferry8[1][x]=1
                            print("****************************************")
                            print("* YOUR DESIRED SEAT HAS BEEN BOOKED    *")
                            print("****************************************")
                            counter=0
                            break
                        elif(Ferry8[1][x]==1):
                            counter=1
                            x=x+1
                    if(counter==0):
                        x=x+1
                    elif(counter==1):
                        print("*****************************************")
                        print("* ALL SEATS ARE BOOKED                  *")
                        print("* TAKING YOU TO THE MAIN MENU           *")
                        print("* CHOOSE BUISNESS CLASS TO BOOK A SEAT  *")
                        print("*****************************************")
                    x=x+1
        elif(choice2=="M"):
            mainmodule(Customer_Ferry_Id,Customer_Trip_Time)
        else:
            print("INVALID INPUT")
            
        
def infomodule():                                                                                     #**********************************************************                  
    while True:                                                                                       #INFO MODULE THAT ASKS THE USER TO SEELCT THE FERRY IDS                          
        print("\t F-Select Ferry ID")                                                                 #THAT ARE AVAILABLE TO THE USERS.PRINTING THE LISTS OF BOTH  
        print("\t T-Select Trip Time")                                                                #FERRY IDS AND TRIPTIMES.USER SELECTS BY CHOICE AND THE   
        print("\t P-Previous Menu")                                                                   #VALUE IS ASSIGNED TO THE GLOBAL VARIABLE CUSTOMER_FERRY_ID  
        choice3=input("Please Enter Your Selection: ")                                                #AND CUSTOMER TRIP TIME.  
        if(choice3=="F"):                                                                             #**********************************************************  
            print("FERRY ID'S")
            x=1
            while(x<=8):
                print(x,"." ,Ferryid[x-1])
                x=x+1
            choice4=int(input("Please Enter Your Selection: "))
            if(choice4==1):
                Customer_Ferry_Id=Ferryid[0]
            elif(choice4==2):
                Customer_Ferry_Id=Ferryid[1]
            elif(choice4==3):
                Customer_Ferry_Id=Ferryid[2]
            elif(choice4==4):
                Customer_Ferry_Id=Ferryid[3]
            elif(choice4==5):
                Customer_Ferry_Id=Ferryid[4]
            elif(choice4==6):
                Customer_Ferry_Id=Ferryid[5]
            elif(choice4==7):
                Customer_Ferry_Id=Ferryid[6]
            elif(choice4==8):
                Customer_Ferry_Id=Ferryid[7]
            elif(choice4==9):
                Customer_Ferry_Id=Ferryid[8]
            elif(choice4==10):
                Customer_Ferry_Id=Ferryid[9]
            else:
                print("INVALID INPUT")
        elif(choice3=="T"):
            print("TRIP TIMES")
            x=1
            while(x<=8):
                print(x,"." ,Triptime[x-1])
                x=x+1
            choice5=int(input("Please Enter Your Selection: "))
            if(choice5==1):
                Customer_Trip_Time=Triptime[0]
            elif(choice5==2):
                Customer_Trip_Time=Triptime[1]
            elif(choice5==3):
                Customer_Trip_Time=Triptime[2]
            elif(choice5==4):
                Customer_Trip_Time=Triptime[3]
            elif(choice5==5):
                Customer_Trip_Time=Triptime[4]
            elif(choice5==6):
                Customer_Trip_Time=Triptime[5]
            elif(choice5==7):
                Customer_Trip_Time=Triptime[6]
            elif(choice5==8):
                Customer_Trip_Time=Triptime[7]
            elif(choice5==9):
                Customer_Trip_Time=Triptime[8]
            elif(choice5==10):
                Customer_Trip_Time=Triptime[9]
            else:
                print("INVALID INPUT")
            
        elif(choice3=="P"):
            purchasemodule(Customer_Ferry_Id,Customer_Trip_Time)
def mainmodule(Customer_Ferry_Id,Customer_Trip_Time):                                           #**********************************************************
    print("FERRY TICKETING SYSTEM")                                                             # MAIN MENU OF THE PROGRAM
    print("\t P-Purchase Ticket")                                                               #**********************************************************                
    print("\t V-View Seating Arrangement")
    print("\t R-Read Previous Booked Ticket")
    print("\t Q-Quit")
    choice1=input("Please Enter Your Selection: ")
    if(choice1=="P"):
        infomodule()
    elif(choice1=="V"):
        seatingmodule(Customer_Ferry_Id,Customer_Trip_Time)
    elif(choice1=="Q"):
        exit()
    elif(choice1=="R"):                                                                         #**********************************************************
        myfile=open("FERRYTICKETINGDATA.txt","r")                                               #FILE READING.READING AND DISPLAYING LAST BOOKED TICKET.IT
        data=myfile.read()                                                                      #READS THE VALUES WHICH ARE STORED IN THE FILE BY THE 
        print(data)                                                                             #PREVIOUS USER.
    else:                                                                                       #**********************************************************
        ("INVALID INPUT")
            
            
Buisness_Class = [0,0,0,0,0,0,0,0,0,0]
Economy_Class = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Ferryid = ["001-PENANG TO LANGKAWI","002-PENANG TO LANGKAWI","003-PENANG TO LANGKAWI","004-PENANG TO LANGKAWI","005-LANGKAWI TO PENANG","006-LANGKAWI TO PENANG","007-LANGKAWI TO PENANG","008-LANGKAWI TO PENANG"]
Triptime = ["10AM-PENANG TO LANGKAWI","11AM-PENANG TO LANGKAWI","12AM-PENANG TO LANGKAWI","1PM-PENANG TO LANGKAWI","2PM-LANGKAWI TO PENANG","3PM-LANGKAWI TO PENANG","4PM-LANGKAWI TO PENANG","5PM-LANGKAWI TO PENANG"]
Ferry1=[Buisness_Class,Economy_Class]                                                           #**********************************************************
Ferry2=[Buisness_Class,Economy_Class]                                                           #INITIALIZING OF EIGHT FERRIES WHICH HAVE BUSINESS CLASS
Ferry3=[Buisness_Class,Economy_Class]                                                           #AND ECONOMY CLASS AS THEIR ELEMENTS.INITIALIZING ALL
Ferry4=[Buisness_Class,Economy_Class]                                                           #ELEMENTS OF BUISNESS CLASS AND ECONOMY LIST ELEMENTS TO 0.
Ferry5=[Buisness_Class,Economy_Class]                                                           #DEFINING LISTS OF TRIPTIMES AND FERRYIDS AND STORING 
Ferry6=[Buisness_Class,Economy_Class]                                                           #THE AVAILABLE FERRIES AND TRIPTIMES IN THEM.
Ferry7=[Buisness_Class,Economy_Class]                                                           #**********************************************************
Ferry8=[Buisness_Class,Economy_Class]

while True: 
    Customer_Ferry_Id=0                                                                         #**********************************************************
    Customer_Trip_Time=0                                                                        #INITIALIZING FERYID AND TRIPTIME TO 0.MAIN MODULE FUNCTION
    mainmodule(Customer_Ferry_Id,Customer_Trip_Time)                                            #CALLED IN A WHILE TRUE TO REPEAT THE MAIN MENU.
                                                                                                #**********************************************************
    
