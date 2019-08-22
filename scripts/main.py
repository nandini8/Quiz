path = 'data/'
import json

event = []
categories = []

answers = {}
total = 0

with open(path + 'quiz.json') as json_file:
    data = json.load(json_file)

    for key, value in data.items():
        event.append(key)
        
        if type(value) == dict:
            print("Select a group: ")

            for k,v in value.items():
                categories.append(k)
                print(str(categories.index(k)) + " " + k)

            category = int(input())
            
            try:
                for qno, questions in value[categories[category]].items():
                    print(questions['question'])

                    for option in questions['options']:
                        print(str(questions['options'].index(option)) + " " + option)

                    ans = int(input("Enter the answer: "))
                    try:
                        answers[qno] = questions['options'][ans]

                        if questions['options'][ans] == questions['answer']:
                            total += 1
                    except IndexError:
                        print("Please enter a valid option number. Skipping this question")

            except IndexError:
                print("Please enter a valid option number. Ending quiz.")

print("Your total score is: {}".format(total) )
                



    