from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_gpt():

    file = "conversation.txt"


    messages = []
    
    prompt = "You are a very lovely computer teacher."


    messages = [{"role": "system", "content": prompt}]


    while True:
        user_input = input("User: ")
        
        if user_input.lower() == "exit":
            print("대화 종료")
            break
        

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7,
            )
            assistant_response = response.choices[0].message.content
            print(f"GPT: {assistant_response}")

            messages.append({"role": "assistant", "content": assistant_response})

            with open(file, "a", encoding="utf-8") as file:
                file.write(f"You: {user_input}\n")
                file.write(f"GPT: {assistant_response}\n\n")
        except Exception as e:
            print(f"오류: {e}")

if __name__ == "__main__":
    chat_with_gpt()