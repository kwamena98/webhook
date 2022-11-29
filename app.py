from flask import Flask, request, Response
import json

import os
import openai



# openai.api_key =os.environ.get("API_KEY")






app = Flask(__name__)
@app.route('/my_webhook', methods=['GET','POST'])
def return_response():
    res=request.json
    text=res['text']
    # print(text)

    # response = openai.Completion.create(
    # model="text-davinci-003",
    # prompt=request.json,
    # temperature=0.9,
    # max_tokens=150,
    # top_p=1,
    # frequency_penalty=0,
    # presence_penalty=0.6,
    # )

    # data_=response["choices"][0]["text"]
    # print("from:",data_)
    # Do something with the request.json data.
    x={

      "message":text
    }

    x=json.dumps(x)
    return (x)
    
if __name__ == "__main__":
    app.run()
