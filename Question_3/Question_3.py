import pickle
while True :
    operation = input("enter tu for translator user or enter td for translator deveolper or enter exit ")
    if operation == 'exit' :
        print("you have enterd exit")
        break
    elif operation =='tu':
        eng_word = input("enter English word for translation")
        file_name=r"C:\Users\Basel.ICT\Desktop\Assignment1\translation.pkl"
        in_file=open(file_name,'rb')
        dictonary_content=pickle.load(in_file)
        print('the translation for :',eng_word,'is :',dictonary_content[eng_word])
        in_file.close()
    elif operation == 'td':
        file_name = r"C:\Users\Basel.ICT\Desktop\Assignment1\translation.pkl"
        in_file = open(file_name, 'rb')
        dictonary_content = pickle.load(in_file)
        in_file.close()
        eng_word  = input("enter english word")
        arab_word = input("enter arabic word")
        dictonary_content[eng_word] = arab_word
        in_file=open(file_name,'wb')
        pickle.dump(dictonary_content,in_file)
        in_file.close()
    else :
        print ("you have entered wrong text ")


