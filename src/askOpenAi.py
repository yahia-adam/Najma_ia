import openai
import dotenv

env_vars = dotenv.dotenv_values()
openai.api_key = env_vars["OPENAI_API_KEY"]

def ask_openai(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = message,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )  
    answer = response.choices[0].text.strip()
    return answer

# def main():

#     while True:
#         message = input("Message: ")
#         answer = ask_openai(message)
#         print(f"Answer: {answer}")

# if __name__ == "__main__":
#     main()