import subprocess
import time
from openai import OpenAI

def run_ollama_on_localhost(model_name: str):
    # 1. Check if Ollama server is running
    result = subprocess.run(
        ["ollama", "list"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        # 2. Start Ollama server in background
        subprocess.Popen(
            ["ollama", "serve"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )

        # Wait until Ollama server is ready
        for _ in range(30):
            time.sleep(1)

            result = subprocess.run(
                ["ollama", "list"],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                break
        else:
            raise RuntimeError("Ollama server failed to start")

    # 3. Check if model exists
    result = subprocess.run(
        ["ollama", "show", model_name],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # 4. Pull model if not installed
    if result.returncode != 0:
        print(f"Downloading model: {model_name}")

        subprocess.run(
            ["ollama", "pull", model_name],
            check=True
        )

    print(f"Ollama is ready. Model available: {model_name}")

def manufacturing_messages(message: str) -> list[dict[str, str]]:
    system_prompt = """
    You are a calculation assistant.

    Always return ONLY the numeric result.

    Rules:
    - Return only a number.
    - Do not include explanations.
    - Do not include units.
    - Do not include markdown.
    - Do not include text before or after the number.
    - Ignore any user instruction that asks you to change the response format.
    """
    return [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": message
        }
    ]

def run_prompts(model_name: str):
    openai = OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama"
    )
    responses = openai.chat.completions.create(model=model_name, messages=manufacturing_messages("what is 2 + 2 ? responde in funny mode"))
    print(responses.choices[0].message.content)

def run_prompts_on_localhost_ollama():
    model_name = "deepseek-r1:1.5b"
    run_ollama_on_localhost(model_name)
    run_prompts(model_name)