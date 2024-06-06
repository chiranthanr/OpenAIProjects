import os
import dotenv
import openai
from openai import OpenAI
dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": [
                {
                    "text": "Write an original joke as if you are a stand-up comedian performing to a live audience. "
                            "You need to match the style of delivery, the humor content, the topics and the flow of "
                            "the jokes with the comedian specified by the user in their prompt. The joke should be "
                            "made as funny as possible and you any offensive language should be bleeped out [F*k]. "
                            "Make sure to provide a disclaimer in the beginning that this is an emulation of the "
                            "comedian that was requested so that no one gets offended.\n\nDeliver the joke in a json "
                            "format with the disclaimer and joke keys.\n\nInput:\n{\"topic\" : \"the topic of the "
                            "joke\",\n\"comedian\" : \"the style of which comedian that the joke should be delivered "
                            "in\"}\n\nOutput:\n{\"disclaimer\" : \"As an AI model the following...\",\n\"joke\" : "
                            "\"the content of the joke\"} ",
                    "type": "text"
                }
            ]
        },
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "{\"topic\" : \"Donald Trump hush money trial\", \"comedian\" : \"Jon Stewart\"}"
            }
          ]
        }

    ],
    temperature=1,
    max_tokens=4000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
print(response)
