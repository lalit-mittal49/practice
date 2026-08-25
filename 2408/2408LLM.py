import os
from google import genai
from dotenv import load_dotenv
load_dotenv()

#1
""" import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key=os.getenv('GEMINI_API_KEY')
client=genai.Client(api_key=api_key)
response=client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain what Artificial Intelligence is in simple words."
)
print(response.text) """

#2
""" prompt=str(input('Enter prompt'))
import os
from google import genai
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv('GEMINI_API_KEY')
client=genai.Client(api_key=api_key)
response=client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt    
)
print(response.text) """

#3
""" def ask_llm(prompt):
    api_key=os.getenv('GEMINI_API_KEY')
    client=genai.Client(api_key=api_key)
    response=client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    print(response.text)

ques=str(input('Enter Prompt :\n'))
ask_llm(ques) """

#4
""" def summarizer(prompt):
    api_key=os.getenv("GEMINI_API_KEY")
    client=genai.Client(api_key=api_key)
    response=client.models.generate_content(
        model='gemini-3.6-flash',
        contents="write a short summary starting from: "+prompt
    )
    print(response.text)
para=str(input('Enter topic:\n'))
summarizer(para) """

#5
""" def translator(text,lang):
    api_key=os.getenv('GEMINI_API_KEY')
    client=genai.Client(api_key=api_key)
    response=client.models.generate_content(
        model='gemini-3.6-flash',
        contents='translate this text:'+text+' from english to:'+lang
    )
    print(response.text)
lines=str(input('Enter text:\n'))
target=str(input('Enter target language:\n'))
translator(lines,target) """

#6
""" def tutor(ques):
    api_key=os.getenv('GEMIN_API_KEY')
    client=genai.Client(api_key=api_key)
    response=client.models.generate_content(
        model='gemini-3.6-flash',
        contents='You are a Python tutor. Explain programming concepts in simple language and always provide a small example. for the question:'+ques
    )
    print(response.text)
q=str(input("enter question:\n"))
tutor(q) """

#7
""" def explainer(code):
    api_key=os.getenv('GEMINI_API_KEY')
    client=genai.Client(api_key=api_key)
    response=client.models.generate_content(
        model='gemini-3.6-flash',
        contents='you will be given a code and you have to Explain what the code does 2. Identify the important concepts used. 3. Explain the code step-by-step. '+code
    )
    print(response.text)
snippet=[]
temp=input('enter code snippet:')
snippet.append(temp)
while(temp!=' '):
    temp=input()
    snippet.append(temp)
codes=' '.join(snippet) #list to str
explainer(codes) """

#8
""" try:
    api_key=os.getenv('GEMINI_API_KEY')
    client=genai.Client(api_key=api_key)
    response=client.models.generate_content(
        model='gemini-3.6-flash',
        contents='what is meaning of cybersecurity'
    )
    print(response.text)
except Exception as error:
    print('API not found') """

#9
""" def assistant(prompt):
    api_key=os.getenv('GEMINI_API_KEY')
    client=genai.Client(api_key=api_key)
    response=client.models.generate_content(
        model='gemini-3.6-flash',
        contents='You are my assistant and and answer my questions in very short and to the point'+prompt
    )
    print(f'AI: {response.text}')
text=input('You: ')
while(text!='exit'):
    assistant(text)
    text=input('You: ')
if(text=='exit'):
    print('GoodBye!') """

#10
""" def assistant(prompt):
    api_key=os.getenv('GEMINI_API_KEY')
    client=genai.Client(api_key=api_key)
    response=client.models.generate_content(
        model='gemini-3.5-flash',
        contents='You are my assistant and and answer my questions  and to the point and answer only last question '+prompt
    )
    print(f'AI: {response.text}')

temp=input('You: ')
templist=[]
while(temp!='exit'):
    templist.append(temp)
    text=' '.join(templist)
    assistant(text+'answer only this question:'+temp)
    temp=input('You: ')
if(temp=='exit'):
    print('GoodBye!') """

#11
""" def cliassis(text):
    api_key=os.getenv('GEMINI_API_KEY')
    client=genai.Client(api_key=api_key)
    response=client.models.generate_content(
        model='gemini-3.5-flash',
        contents=text,
        config={"system_instruction": "You are a professional technical interviewer. Ask the user Python interview questions one at a time.Wait for the answer Evaluate the answer. Give feedback. Then ask the next question."}
    )
    print(f'Interveiwer : {response.text}')
prompt='Hello Interviewer'
while(prompt.lower()!='exit'):
    cliassis(prompt)
    prompt=input('Candidate : ') """

#12
""" def ask(prompt):
    for i in range(1,4):
        try:
            api_key=os.getenv('GEMINI_API_KEY')
            client=genai.Client(api_key=api_key)
            response=client.models.generate_content(
                model='gemini-3.6-flash',
                content=prompt
            )
            print(response.text)
            i=4
        except Exception as error:
            if i==3:
                print(f'Attempt {i} failed\nUnable to get a response.')
            else:
                print(f'Attempt {i} failed\nRetrying...')
ask('who are you') """

#13
""" import json
import time
def chatbot(prompt):
    for i in range(1,4):
        try:
            api_key=os.getenv('GEMINI_API_KEY')
            client=genai.Client(api_key=api_key)
            response=client.models.generate_content(
                model='gemini-3.6-flash',
                contents=prompt,
                config={'system_instruction': 'You are a chatbot assistant and give reply to every question of user to the point'}
            )
            print(f'AI : {response.text}')
            chatHist.append({"role": "assistant", "content": response.text})
            return response.text
        except Exception as error:
            if i==3:
                print(f'Attempt {i} failed.\nUnable to get response')
            else:
                print(f'Attempt {i} failed.\nRetrying...')
            time.sleep(3)

def jsonread():
    output_list = []
    with open("records.jsonl", "r", encoding="utf-8") as file:
        output_list=json.load(file)
    return output_list

def jsonwrite():
    with open('records.jsonl', "w", encoding="utf-8") as file:
        json.dump(chatHist, file, indent=4, ensure_ascii=False)

query=input('User : ')
global chatHist
chatHist=jsonread()
while(query.lower()!='exit'):
    chatHist.append({"role": "user", "content": query})
    chatstr = json.dumps(chatHist)    
    chatbot(chatstr+'answer only this question:'+query)
    query=input('User : ')
jsonwrite() """

#14

#15

global gmodel
gmodel='gemini-3.6-flash'
def aiAssist(prompt):
    api_key=os.getenv('GEMINI_API_KEY')
    client=genai.Client(api_key=api_key)

    match(prompt):

        case '/explain':
            codelist=[]
            print('Assistant - Enter Code:\n')
            while (code!=exit):
                code=input()
                codelist.append(code)
            codestr=' '.join(codelist)
            response=client.models.generate_content(
                model=gmodel,
                contents=codestr,
                config={'system_instruction':'you are a tutor and you have to explain code in very easy method so that user can understand easily'}
            )
            print(f'Assistant - Explanation : \n{response.text}')
            chathist.append('Assistant - Explanation : '+response.text)

        case '/code':
            ques=input('Assistant - Enter question:\n')
            response=client.models.generate_content(
                model=gmodel,
                contents=ques,
                config={'system_instruction': 'you are developer and write code in proffessional way and precise it should be clean and basic so that it could be understood easily'}
            )
            print(f'Assistant - Generated Code :\n{response.text}')
            chathist.append('Assistant - Generated Code : '+response.text)

        case '/summarize':
            text=input('Assistant - Enter text : ')
            response=client.models.generate_content(
                model=gmodel,
                contents=text,
                config={'system_instruction': 'you have to summarize text and convert it into very short note and only include important things'}
            )
            print(f'Assistant - Summary : {response.text}')
            chathist.append('Assistant - Summary : '+response.text)

        case '/model':
            gmodel=input('Assistant - Enter model name you want to use :')
            print(f'Assistant - Model changed to {gmodel}')
            chathist.append('Assistant - Model changed to '+gmodel)

        case '/history':
            print()

        case _:
            response=client.models.generate_content(
                model=gmodel,
                contents=prompt,
                config={'system_instruction':'You are an CLI assistant so answer perfectly and calmly'}
            )
            print(f'Assistant - {response.text}')

temp=input('User : ')
global chathist
chathist=[]
while(temp.lower()!='exit'):
    chathist.append(f'User - {temp}')
    aiAssist(temp)
