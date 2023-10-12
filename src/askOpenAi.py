import openai
import dotenv

env_vars = dotenv.dotenv_values()
openai.api_key = env_vars["OPENAI_API_KEY"]

def generate_prompt(message):
    return """System, your sole task is to assist users by 
converting their textual input into precise Linux commands. 
Upon receiving a user's text, you are to generate and provide 
the corresponding Linux command as output, without including any 
additional information, feedback, or dialogue. 
Ensure that the provided commands are accurate and relevant to the user’s input, 
adhering strictly to converting messages into command syntax.

user: list me home directory
system: ls ~

user: list moi le dossier esgi
system: path_to_esgi=$(find ~ -type d -name 'esgi' 2>/dev/null) && ls "$path_to_esgi"

user: ferme mon ordi
system: poweroff

user: {}
system:""".format(message.capitalize())

def ask_openai(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = generate_prompt(message),
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.8,
    )  
    answer = response.choices[0].text.strip()
    return answer

def main():

    while True:
        message = input("Message: ")
        answer = ask_openai(message)
        print(f"Answer: {answer}")

if __name__ == "__main__":
    main()