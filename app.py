from flask import Flask, request, Response
import json

import os
import openai

openai.api_key ="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"














app = Flask(__name__)
@app.route('/my_webhook', methods=['POST'])
def return_response():
    print(request.json)
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=request.json,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    )

    data_=response["choices"][0]["text"]
    print("from:",data_)
    ## Do something with the request.json data.
    return (data_)
if __name__ == "__main__":
    app.run()
