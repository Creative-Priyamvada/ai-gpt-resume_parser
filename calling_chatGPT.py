import openai
import os





openai.api_key = "Enter key here"


def chatGPT_output(resume_text):
    print('--in chatGPT ouput function --')

    completion = openai.ChatCompletion.create(
    model="gpt-4", 
    messages=[{"role": "user", "content": "Please cleanup {resume_text} and output in rchilli format.".format(resume_text = resume_text)}]
    )

    print('--- next will print message ---)')
    message= dict(completion.choices[0].message)
    print('--message-- ',message)
    content=message['content']


