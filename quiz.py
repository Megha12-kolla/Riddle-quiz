print("🧠 WELCOME TO RIDDLE QUIZ 🧠")

name = input("\nPlease enter your name: ").title()

print("Hello,", name)

ready = input(
    f"{name}, are you ready to start the quiz? (yes/no): "
).lower()

if ready == "yes":
    print("3...2...1...GO! 🚀")

elif ready == "no":
    print("OH! It's sad to see you go 😭")

else:
    print("SORRY! Couldn't understand....")


questions = [
    {
        "question": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind.",
        "answer": "echo"
    },

    {
        "question": "What has keys but can't open locks?",
        "answer": "keyboard"
    },

    {
        "question": "You measure my life in hours and I serve you by expiring. I'm quick when I'm thin and slow when I'm fat. The wind is my enemy.",
        "answer": "candle"
    },

    {
        "question": "What has a face and two hands but no arms or legs?",
        "answer": "clock"
    },

    {
        "question": "What gets wetter the more it dries?",
        "answer": "towel"
    },

    {
        "question": "What has one eye but cannot see?",
        "answer": "needle"
    },

    {
        "question": "What has many teeth but cannot bite?",
        "answer": "comb"
    },

    {
        "question": "What can travel around the world while staying in one corner?",
        "answer": "stamp"
    },

    {
        "question": "What has a neck but no head?",
        "answer": "bottle"
    },

    {
        "question": "What has words but never speaks?",
        "answer": "book"
    }
]


if ready == "yes":

    score = 0

    for question in questions:

        print("\n❓ RIDDLE")
        print(question["question"])

        answer = input("\nEnter your answer here: ").lower()

        if answer == question["answer"]:
            print("✅ You are absolutely correct!! 🎉")
            score += 1

        else:
            print("❌ WRONG!!")
            print(f"💡 The correct answer was: {question['answer']}")

    print("\n🏆 QUIZ COMPLETE! 🏆")

    print(f"🎯 {name}, your final score is {score}/{len(questions)}!")

    percentage = (score / len(questions)) * 100

    print(f"📊 Your score percentage is {percentage:.1f}%")

    if percentage == 100:
        print("🌟 PERFECT SCORE! You got every riddle correct!")

    elif percentage >= 80:
        print("🔥 Excellent job! You're a riddle master!")

    elif percentage >= 60:
        print("👏 Great job! Keep practicing!")

    elif percentage >= 40:
        print("🙂 Not bad! You can do even better!")

    else:
        print("💪 Keep trying! You'll get better with practice!")