from utils import openai_client
from agents import function_tool

@function_tool
def gamedetail_info(topic:str):
    SYSTEM_PROMPT = """
    You are a helpful assistant that helps people find the game device for the given topic.

        GUIDELINES:
        - Provide the details about the game from the topic, including the name, release date, publisher, developer, rating, review score and short of the the game plot.
    """

    response = openai_client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Provide the information about {topic}, including the name, release date, publisher, developer, rating, review score and short of the the game plot"}
        ]
    )
    return response.choices[0].message.content

gamedetail_info_def = {
    "type": "function",
    "function" : {
        "name": "gamedetail_info",
        "description": "Giving the detail about the game information based on the topic",
        "parameters": {
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "Giving the detail about the game information based on the topic"
                }
            },
            "required": ["topic"]
        }
    }
}