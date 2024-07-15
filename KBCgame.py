# This is the game like KBC where we aks question about our nation to user and user have to answer that and then he got reward 
import random 
# The list of the all questions :
quiz = [
    ["Which is the national animal of India?", "Tiger", "Lion", "Elephant", "Leopard", 1],
    ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["Who wrote 'Hamlet'?", "Charles Dickens", "J.K. Rowling", "Mark Twain", "William Shakespeare", 4],
    ["Which element has the chemical symbol 'O'?", "Oxygen", "Gold", "Silver", "Iron", 1],
    ["What is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 4],
    ["Which country is known as the Land of the Rising Sun?", "China", "South Korea", "Japan", "Thailand", 3],
    ["What is the smallest primea number?", "1", "2", "3", "5", 2],
    ["Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", 3],
    ["Which language is primarily spoken in Brazil?", "Spanish", "Portuguese", "French", "Italian", 2],
    ["What is the boiling point of water?", "50°C", "75°C", "100°C", "125°C", 3],
    ["Which is the longest river in the world?", "Nile", "Amazon", "Yangtze", "Mississippi", 2],
    ["Who is the founder of Microsoft?", "Steve Jobs", "Bill Gates", "Elon Musk", "Mark Zuckerberg", 2],
    ["What is the currency of Japan?", "Dollar", "Yen", "Euro", "Won", 2],
    ["Which organ is primarily responsible for pumping blood?", "Lungs", "Brain", "Liver", "Heart", 4]
]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money = 0
lifeline_50_50 = 1
lifeline_expert = 1

# Run loop to aks a question
for i in range(0,len(quiz)):
    question = quiz[i]
    print(f"\nQue. for {levels[i]} is :{question[0]}")
    print(f"A.{question[1]}")
    print(f"B.{question[2]}")
    print(f"C.{question[3]}")
    print(f"D.{question[4]}")

    print(f"\nAvailable lifeline : 50-50 -> {lifeline_50_50}, Ask an expert -> {lifeline_expert}")
    reply = input("\nEnter your answer OR you can use lifeline (L) OR you can Quit(Q) :")

    
    if (reply.upper() == "Q"):
        if(i >= 1):
            print("You Quit")
            money = levels[i-1]
            break
        else:
            print("You Quit")
            money = 0
            break
        
    if (reply.upper() == "A"):
        reply = 1 
    elif (reply.upper() == "B"):
        reply = 2 
    elif (reply.upper() == "C"):
        reply = 3 
    elif (reply.upper() == "D"):
        reply = 4
    
    elif (reply.upper() == "L"):
        print(f"\nAvailable lifeline : 50-50 -> {lifeline_50_50}, Ask an expert -> {lifeline_expert}")
        
        #Check if any lifeline is available or not 
        if (lifeline_50_50 == 1 or lifeline_expert == 1):
            user_lifeline = int(input("Enter 1 for 50-50 OR Enter 2 for Aks an expert :"))
        else:
            print("\nYou don't have any life line !!")
            break

        if (user_lifeline == 1):

            # Check if 50-50 lifeline is available or not 
            if (lifeline_50_50 == 1):
            
                # Logic for 50-50 lifeline
                lifeline_50_50 = 0
                correct_ans = question[-1]
                random_option = random.randint(1,4) # for 50-50 we'll pick any random option except answer
                while True:
                    if (random_option != correct_ans):
                        break
                    else:
                        random_option = random.randint(1,4)

                random_int_for_option_pattern = random.randint(1,3)

                if (random_int_for_option_pattern == 1):
                    print("\nChoose your answer from these 2 option!!")
                    print(f"1. {question[correct_ans]}          2. {question[random_option]} ")
                    reply_lifeline = int(input("Pick your ans :"))
                    if (reply_lifeline == 1):
                        reply = question[-1]
                        
                else:
                    print("\nChoose your answer from these 2 option!!")
                    print(f"1. {question[random_option]}          2. {question[correct_ans]} ")
                    reply_lifeline = int(input("Pick your ans :"))
                    if (reply_lifeline == 2):
                        reply = question[-1]
                       
            else:
                print("\nSorry you don't have this lifeline !!")
                break
        
        elif (user_lifeline == 2):

            # Check if Ask an expert lifeline is available or not
            if(lifeline_expert == 1):

                # Logic for Ask an expert lifeline 
                lifeline_expert = 0
                suggest_ans = question[-1]
                print(f"\nAs an expert, I think the ({question[suggest_ans]}) option should be the correct answer")    
                print(f"A.{question[1]}")
                print(f"B.{question[2]}")
                print(f"C.{question[3]}")
                print(f"D.{question[4]}")

                reply = input("You can choose your answer :")
                if (reply.upper() == "A"):
                    reply = 1 
                elif (reply.upper() == "B"):
                    reply = 2 
                elif (reply.upper() == "C"):
                    reply = 3 
                elif (reply.upper() == "D"):
                    reply = 4            
                else:
                    print("Invalid answer!!")
            
            else:
                print("\nSorry you don't have this lifeline !!")
                break
        else : 
            print("Invalid Choice for lifeline!!")       
    else : 
        print("This is Invalid answer!!")
        break
        
    if (reply == question[-1]):
        print("\n-----------------------------------------")
        print(f"    Correct answer you won {levels[i]} Rs.") 
        print("-----------------------------------------")
        if (i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000
        
    else: 
        print("Wrong answer!!")
        break
print(f"Your take home money is :{money}")



