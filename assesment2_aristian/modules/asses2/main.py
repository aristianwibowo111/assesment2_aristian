from tools.game_recommendation import game_recommendation_def,game_recommendation
from tools.gamedetail_info import gamedetail_info_def,gamedetail_info
from agents import Agent, Runner

from dotenv import load_dotenv

load_dotenv()

tools = [game_recommendation_def,
         gamedetail_info_def,]

agent = Agent(
    name="Gaming Recommendation Agent",
    instructions="You are a helpful gaming assistant that help people find games based on the topic they provide.",
    model="gpt-4.1",
    tools=[game_recommendation, gamedetail_info]
)

async def main():
    messages = []

    while True:
        user_input = input("User:")
        messages.append({"role": "user", "content": user_input})
        runner = await Runner.run(starting_agent=agent, input=user_input)
        result = runner.final_output
        print(result)
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Exiting the chat. Goodbye!")
            break
        elif "export" in user_input.lower():
            from tools.ocr import exporttomd
            exporttomd()
            print("OCR process completed and saved to ocr_response.md")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
    # topic = "Any Adventure video games and their prices you can recommend me ?"
    # gaming_recommend(topic)