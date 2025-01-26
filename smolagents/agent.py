from typing import Optional
from smolagents import CodeAgent, tool, LiteLLMModel

@tool
def send_request(addr: str) -> bytes:
    """
    Sends HTTP GET request to the given address and returns the response as bytes.

    Args:
        addr: The address to send the request to.
    """
    import requests
    response = requests.get(addr)
    return response.content  # Return content as bytes

@tool
def create_file(name: str, content: bytes) -> None:
    """
    Creates a file with the given name and the given content.

    Args:
        name: The name of the file.
        content: The content of the file as bytes.
    """
    with open(name, "wb") as f:
        f.write(content)

model = LiteLLMModel(
    model_id="ollama/llama3:latest",
    api_base="http://localhost:11434"
)

agent = CodeAgent(
    tools=[send_request, create_file], 
    model=model, 
    additional_authorized_imports=["datetime", "bytearray"]
)

# Example usage
output = agent.run("Get the content of the website (has to be short. just content) 'https://dev.to/feed' and write it to file named dev_feed.txt")
print(output)
