from src.prompts_exercise import main as prompts_exercise
from src.endpoints_openai_exercise import chat_completion
from src.run_ollama_localhost_exercise import run_prompts_on_localhost_ollama

def main():
    print("Which exercise you want to execute: \n1) Execute OpenAI Client.\n2) Execute OpenAI API\n3) Execute OpenAI on the local machine")
    choice = int(input("Choice number: "))
    match choice:
        case 1:
            prompts_exercise()
        case 2:
            chat_completion()
        case 3:
            run_prompts_on_localhost_ollama()
        case _:
            prompts_exercise()

if __name__ == '__main__':
    main()

