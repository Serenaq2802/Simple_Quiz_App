print("\n" + "="*60)
print("         🎯   WELCOME TO THE SIMPLE QUIZ APP   🎯")
print("="*60)

#Instructions before the quiz
print("\n                  📌  HOW TO PLAY  📌\n")
print("\n✅️   Answer each question by typing A, B, C, or D.")
print("✅️   Try to get as many correct as you can!")
print("✅️   Best of luck, and have fun!\n")
print("="*60)

#Function that runs the quiz
def run_quiz(questions):
    score = 0              #Starts the user's score at 0 

    #Loop thorugh each question in the list
    for q in questions:
        print("\n" + q["question"])     #Show the question text
        print("-"*60)                   #Dividers to make it look cute!
        #Show all answer choices
        letters = ["A","B","C","D"]
        for i, option in enumerate(q["options"]):
            print(f"        {letters[i]}) {option}")

        #Get the user's answer and make it uppercase for consistency
        print("\n" + "-"*60)
        answer = input("Please choose an option: [A] [B] [C] [D]: ").strip().upper()
        print("-"*60)

        #Check if the answer is correct
        if answer == q["answer"]:
            print("✅ Correct! Well Done!\n")        #Positive Feedback
            score += 1                 # Add 1 to the score

        else:
            print(f"❌ Incorrect. The Correct Answer was {q['answer']}.\n")

    #Show final score after all questions have been answered
    percent = (score / len(questions)) *100
    print("\n" + "="*60)
    print(f" ✨  Your Final Score is: {score}/{len(questions)} ({percent:.1f}%) ✨")
    print("="*60)

    print("\n" + "="*60)
    print("Thanks for playing! Goodbye! 👋")
    print("="*60 + "\n")

#List of questions with options and correct answers
questions = [
    {
        "question": "\n1️⃣    What does RAM stand for?",
        "options":[
            "Random Access Memory",
            "Random Assessory Momentum",
            "Random Act Memory",
            "None of the above"
        ],
        "answer":"A"
    },
    {
        "question": "2️⃣   Which language is this quiz written in?",
        "options": [
            "HTML",
            "Java",
            "Python",
            "C#"
        ],
        "answer":"C"
    },
    {
        "question": "3️⃣  Is Python a compiled language or an interpreted language?",
        "options": [
            "Compiled Language",
            "Interpreted Language",
            "None of the Above",
            "Software Language"
        ],
        "answer": "B"
    }

]

# Start the quiz by calling the run_quiz function'
run_quiz(questions)