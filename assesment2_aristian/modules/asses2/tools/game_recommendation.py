from utils import openai_client
from agents import function_tool

@function_tool
def game_recommendation(topic:str):
    SYSTEM_PROMPT = """
    You are a helpful assistant that helps people find games for the given topic.

        GUIDELINES:
        - Provide a list of 7 games related to the topic.
        - For each game, include a short description.
        - Any question that does not relate to game recommendation should be responded with "I can only help with game recommendations."
    """
    
    response = openai_client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Recommend me 7 games about {topic}, with a short description and it's review score for each game."}
        ]
    )
    return response.choices[0].message.content

game_recommendation_def = {
    "type": "function",
    "function" : {
        "name": "game_recommendation",
        "description": "Recommend games based on a topic",
        "parameters": {
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "The topic to recommend games about"
                }
            },
            "required": ["topic"]
        }
    }
}