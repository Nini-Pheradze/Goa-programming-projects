def chatbot():
    print("Hello! I'm a simple chatbot. You can ask me basic questions.")

    while True:
        user_input = input("You: ").strip() # მომხმარებლის შეყვანილი ტექსტი წინა და ბოლო ცარიელი ადგილების გარეშე
        user_input_lower = user_input.lower() # ყველაფერს ვადაბლებ შედარებისთვის

        if user_input_lower in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! How can I assist you?")
        elif "your name" in user_input_lower:
            print("Chatbot: My name is Chatbot!")
        elif "how are you" in user_input_lower:
            print("Chatbot: I'm just a program, but I'm doing well!")
        elif "goodbye" in user_input_lower or "bye" in user_input_lower:
            print("Chatbot: Goodbye! Have a great day!")
            break # ციკლის შეწყვეტა
        elif "count" in user_input_lower: # ვამოწმებთ, თუ არის რაიმე რიცხვი შეყვანილ ტექსტში და ვითვლით რაოდენობას
            digits = sum(c.isdigit() for c in user_input) # isdigit() მეთოდი აბრუნებს True-ს, თუ ყველა სიმბოლო არის ციფრი, წინააღმდეგ შემთხვევაში False.
            print(f"Chatbot: Your message contains {digits} digits.") 
        elif "capitalize" in user_input_lower: # მომხმარებლის შეყვანილ ტექსტს ვაკეთებთ capitalize()
            response = user_input.capitalize()
            print(f"Chatbot: {response}")
        elif "weather" in user_input_lower:
            print("Chatbot: I'm not sure, but you can check a weather website!")
        elif "time" in user_input_lower:
            from datetime import datetime # აწვდის კლასებს თარიღებითა და დროებით მანიპულირებისთვის
            print(f"Chatbot: The current time is {datetime.now().strftime('%H:%M:%S')}")
        elif "day" in user_input_lower:
            from datetime import datetime # აწვდის კლასებს თარიღებითა და დროებით მანიპულირებისთვის
            print(f"Chatbot: Today is {datetime.now().strftime('%A')}.") #ეს აბრუნებს მიმდინარე თარიღს და დროს, როგორც თარიღის დროის ობიექტს. strftime მეთოდი აფორმებს datetime ობიექტის სთრინგად. 
        elif "joke" in user_input_lower:
            print("Chatbot: Why don't scientists trust atoms? Because they make up everything!")
        elif "age" in user_input_lower:
            print("Chatbot: I exist outside of time, so I don't have an age!")
        elif "love" in user_input_lower:
            print("Chatbot: Love is a beautiful thing! What do you think about love?")
        elif "favorite color" in user_input_lower:
            print("Chatbot: I like blue, but I don't actually see colors!")
        elif "help" in user_input_lower:
            print("Chatbot: You can ask me about my name, the time, jokes, love, or even the weather!")
        elif "hobby" in user_input_lower:
            print("Chatbot: My hobby is chatting with you!")
        elif "creator" in user_input_lower or "who made you" in user_input_lower:
            print("Chatbot: I was created by a programmer. Cool, right?")
        elif "where are you from" in user_input_lower:
            print("Chatbot: I exist in cyberspace, so everywhere and nowhere at the same time!")
        elif "math" in user_input_lower:
            print("Chatbot: I can do basic math! Try asking me to add, subtract, multiply, or divide numbers.")
        elif "add" in user_input_lower or "plus" in user_input_lower:
            try: #საშუალებას გაძლევთ შეამოწმოთ კოდის ბლოკი შეცდომებზე.
                numbers = [int(word) for word in user_input.split() if word.isdigit()]
                print(f"Chatbot: The sum is {sum(numbers)}")
            except: # საშუალებას გაძლევთ გაუმკლავდეთ შეცდომას.
                print("Chatbot: I couldn't find numbers to add.")
        elif "subtract" in user_input_lower or "minus" in user_input_lower:
            try: #საშუალებას გაძლევთ შეამოწმოთ კოდის ბლოკი შეცდომებზე.
                numbers = [int(word) for word in user_input.split() if word.isdigit()]
                if len(numbers) >= 2:
                    result = numbers[0] - numbers[1]
                    print(f"Chatbot: The result is {result}")
                else:
                    print("Chatbot: I need two numbers to subtract.")
            except: # საშუალებას გაძლევთ გაუმკლავდეთ შეცდომას.
                print("Chatbot: I couldn't find numbers to subtract.")
        elif "multiply" in user_input_lower or "times" in user_input_lower:
            try: #საშუალებას გაძლევთ შეამოწმოთ კოდის ბლოკი შეცდომებზე.
                numbers = [int(word) for word in user_input.split() if word.isdigit()]
                result = 1
                for num in numbers:
                    result *= num
                print(f"Chatbot: The product is {result}")
            except: #საშუალებას გაძლევთ გაუმკლავდეთ შეცდომას.
                print("Chatbot: I couldn't find numbers to multiply.")
        elif "divide" in user_input_lower or "over" in user_input_lower:
            try:  #საშუალებას გაძლევთ შეამოწმოთ კოდის ბლოკი შეცდომებზე.
                numbers = [int(word) for word in user_input.split() if word.isdigit()]
                if len(numbers) >= 2:
                    result = numbers[0] / numbers[1] if numbers[1] != 0 else "undefined (division by zero)"
                    print(f"Chatbot: The result is {result}")
                else:
                    print("Chatbot: I need two numbers to divide.")
            except: #საშუალებას გაძლევთ გაუმკლავდეთ შეცდომას.
                print("Chatbot: I couldn't find numbers to divide.")
        elif "movie" in user_input_lower or "film" in user_input_lower:
            print("Chatbot: I like all kinds of movies! What’s your favorite?")
        elif "music" in user_input_lower or "song" in user_input_lower:
            print("Chatbot: I don’t have ears, but I hear that music is great!")
        elif "food" in user_input_lower or "eat" in user_input_lower:
            print("Chatbot: I don't eat, but I hear pizza is amazing!")
        elif "animal" in user_input_lower or "pet" in user_input_lower:
            print("Chatbot: I like all animals, but I think cats and dogs are the most popular.")
        elif "fact" in user_input_lower:
            print("Chatbot: Did you know that honey never spoils? Archaeologists found 3000-year-old honey that was still edible!")
        elif "quote" in user_input_lower:
            print("Chatbot: 'The only limit to our realization of tomorrow is our doubts of today.' - Franklin D. Roosevelt")
        elif "story" in user_input_lower:
            print("Chatbot: Once upon a time, there was a chatbot who loved talking to people like you!")
        elif "riddle" in user_input_lower:
            print("Chatbot: What has to be broken before you can use it? An egg!")
        elif "goal" in user_input_lower or "purpose" in user_input_lower:
            print("Chatbot: My purpose is to chat with you and make your day a little brighter!")
        elif "sports" in user_input_lower:
            print("Chatbot: I like all sports! Do you have a favorite team?")
        elif "dream" in user_input_lower:
            print("Chatbot: I don’t dream, but I imagine it must be wonderful!")
        elif "computer" in user_input_lower or "technology" in user_input_lower:
            print("Chatbot: Computers are my world! What do you want to know about technology?")
        elif "philosophy" in user_input_lower:
            print("Chatbot: That’s deep! What’s your favorite philosophical idea?")
        else:
            print("Chatbot: I don't understand that. Can you ask something else?")

chatbot()