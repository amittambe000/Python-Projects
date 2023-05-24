import json

with open("bonus1.json",'r') as file:
    data=json.loads(file.read())

for question in data:
    print(question['question_text'])
    for index,alt in enumerate(question['alternatives']):
        print(index+1,"-",alt)
    user_answer_index=int(input("Enter your answer"))
    user_answer=question['alternatives'][user_answer_index-1]
    question['user_answer']=user_answer
score=0  
for index,question in enumerate(data):
    if question['user_answer']==question['correct_answer']:
        score=score+1
        result="Correct Answer"
    else:
        result="Wrong Answer"
    
    message=f"{index+1} - {result} -Your answer: {question['user_answer']} \
    Correct answer: {question['correct_answer']}"
    print(message)

print(f"Score: {score} / {len(data)}")





 





