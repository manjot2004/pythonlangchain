questions = []
def add_list():
    #  while True:
          print("Enter list")
          num=int(input("enter range: "))
          for i in range(1,num+1):
            ques=input("Add question: ")
            options=input("Enter options: ").split(",")
            ans=input("Enter answer: ")
            list_1 = {"question":ques ,"options": options,"answer": ans}
            questions.append(list_1)
            print(questions)

def print_list():
    # while True:
        for index,list_1 in enumerate(questions,start=1):
             print(f"{index}) {list_1['question']}, {list_1['options']},{list_1['answer']}")

def update_list():
    # while True:
        # for i, q in enumerate(questions, start=1):
        #     print(f"{i}. {q['question']}")

        index = int(input("Enter question number to update: "))
        if 1 <= index <= len(questions):
            q=input("enter new question")
            opt=input("enter options").split(",")
            ans=input("enter new answer")
            new={'question':q,'options':opt,'answer':ans}
            questions[index]=new
            # questions[index-1]["question"] = input("New question: ")
            # questions[index-1]["options"] = input("New option: ").split(",")
            # questions[index-1]["answer"] = input("New answer: ")
            print("Updated successfully!")
        else:
            print("Invalid index.")
            

def play_quiz():
    
    if len(questions)==0:
        print("no questions added")
    
    score=0
    for q in questions:
        print("\n"+q['question'])
        
        for i,options in enumerate(q,start=1):
            print(f"{i}) {q['options']}")
        
        user_ans=input("enter your answer")
        if user_ans==q['answer']:
            print("correct")
            score +=1
        else:
            score=0
            print("correct answer",q['answer'])
        
        print(f"your score: {score}/{len(questions)}")
        
        
def delete():
    if len(questions)==0:
        print("no questions found")
        
    index=int(input("enter question number to delete"))
    if 1<= index <=len(questions):
        questions.pop(index-1)
    print(f"question deleted succesfully")
    
        
        
        

def exit():
    print("exit from the quiz")      
            
            









            
            
            
def main():
    while True:
        print("\n" + "="*20 + " " + "start the quiz:" + " " + "="*20) 
        print("1. add quiz")
        print("2. list quiz")
        print("3. update quiz")
        print("4.play quiz")
        print("5.delete question")
        print("6.exit")
        
        choice=input("enter your choice: ")
        
        if choice=="1":
            add_list()
            print(questions)
            print("added successfully")
        
        if choice=="2":
            print("list of questions")
            print_list()
        
        if choice=="3":
            update_list()
            print("update succesfully")
        
        if choice=="4":
            play_quiz()
            
        if choice=="5":
            delete()
            print("deleted succesfully")            
            
        if choice=="6":
            exit()
            
            

               
main()       

