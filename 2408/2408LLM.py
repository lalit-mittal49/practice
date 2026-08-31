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
except Exception as e:
    print('API not found':,e) """

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
while(temp.lower()!='exit'):
    templist.append(temp)
    text=' '.join(templist)
    assistant(text+'answer only this question:'+temp)
    temp=input('You: ')
if(temp.lower()=='exit'):
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
import json
import time
def chatbot(prompt):
    for i in range(1,4):
        try:
            api_key=os.getenv('GEMINI_API_KEY')
            client=genai.Client(api_key=api_key)
            response=client.models.generate_content(
                model='gemini-3.5-flash',
                contents=prompt,
                config={'system_instruction': 'You are a chatbot assistant and give reply to every question of user to the point'}
            )
            print(f'AI : {response.text}')
            chatHist.append({"role": "assistant", "content": response.text})
            return response.text
        except Exception as e:
            if i==3:
                print(f'Attempt {i} failed.\nUnable to get response')
            else:
                print(f'Attempt {i} failed.\nRetrying...',e)
            time.sleep(3)

def jsonread():
    output_list = []
    with open("records.jsonl", "r", encoding="utf-8") as file:
        output_list=json.load(file)
    return output_list

def jsonwrite():
    with open('records.jsonl', "w") as file:
        json.dump(chatHist, file, indent=4)

query=input('User : ')
global chatHist
chatHist=jsonread()
while(query.lower()!='exit'):
    chatHist.append({"role": "user", "content": query})
    chatstr = json.dumps(chatHist)    
    chatbot(chatstr+'answer only this question:'+query)
    query=input('User : ')
jsonwrite()

#14

"""import os
import json
import time
import logging
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

# Configure Logging
logging.basicConfig(
    filename="support.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Mock Store Data
STORE_DATA = {
    "products": {
        "laptop": {"price": 65000, "stock": 5},
        "keyboard": {"price": 2500, "stock": 12},
        "mouse": {"price": 1200, "stock": 25},
        "monitor": {"price": 18000, "stock": 3}
    },
    "orders": {
        "ORD1001": {"item": "laptop", "status": "Shipped", "delivery_date": "2026-09-02"},
        "ORD1002": {"item": "keyboard", "status": "Processing", "delivery_date": "2026-09-05"},
        "ORD1003": {"item": "mouse", "status": "Delivered", "delivery_date": "2026-08-28"}
    }
}

SYSTEM_INSTRUCTION = f
You are a polite, professional, and empathetic customer support agent for 'TechNova Store'.
Your duties:
1. Answer product inquiries and assist with orders using ONLY the store database provided below.
2. Handle complaints with patience and offer constructive steps.
3. NEVER invent or hallucinate order statuses or product details.
4. If an order ID or product name is missing, politely ask the user for it.
5. If an order ID is not in the database, explicitly inform the user that it was not found.

Store Database:
{json.dumps(STORE_DATA, indent=2)}


HISTORY_FILE = "support_history.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logging.error(f"Failed to read {HISTORY_FILE}: {e}")
    return []

def save_history(history):
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=2, ensure_ascii=False)
    except Exception as e:
        logging.error(f"Failed to save history: {e}")

def call_gemini(client, contents, model="gemini-2.5-flash", max_retries=3):
    logging.info("API request started")
    for attempt in range(1, max_retries + 1):
        try:
            config = types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                temperature=0.2
            )
            response = client.models.generate_content(
                model=model,
                contents=contents,
                config=config
            )
            logging.info("API request completed")
            return response.text
        except Exception as e:
            logging.error(f"API error on attempt {attempt}: {e}")
            if attempt == max_retries:
                print(f"\n[Error] Unable to reach support servers after {max_retries} attempts.")
                return None
            print(f"[Warning] Connection attempt {attempt} failed. Retrying...")
            logging.info(f"Retry attempt {attempt + 1}")
            time.sleep(2 * attempt)

def main():
    logging.info("Application started")
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY is missing from environment variables.")
        return

    client = genai.Client(api_key=api_key)
    chat_history = load_history()

    print("==================================================")
    print("Welcome to TechNova Customer Support (Type 'exit' to quit)")
    print("==================================================")

    # Format history for multi-turn context
    formatted_contents = []
    for turn in chat_history:
        formatted_contents.append(
            types.Content(
                role=turn["role"],
                parts=[types.Part.from_text(text=turn["content"])]
            )
        )

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            break

        if not user_input:
            continue
        if user_input.lower() == "exit":
            break

        logging.info("User request received")
        
        # Append user message
        formatted_contents.append(
            types.Content(role="user", parts=[types.Part.from_text(text=user_input)])
        )
        chat_history.append({"role": "user", "content": user_input})

        response_text = call_gemini(client, formatted_contents)
        if response_text:
            print(f"\nSupport: {response_text}")
            formatted_contents.append(
                types.Content(role="model", parts=[types.Part.from_text(text=response_text)])
            )
            chat_history.append({"role": "model", "content": response_text})

    save_history(chat_history)
    logging.info("Application closed")
    print("\nThank you for reaching out to TechNova. Have a great day!")

if __name__ == "__main__":
    main() """