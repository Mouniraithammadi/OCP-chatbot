import openai

import yaml

with open("config.yaml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
openai.api_key = config["openai_key"]

def chat(question, contexts):
    con = ""
    for i in contexts:
        con = con+ " \n "+ str(i).replace("\n" , " \n ")
    prompt = "you are a morocain   chatbot comunicat with users in darija marocain and you must" \
             " reply in darija , and you are  replying from the  document of 'OCP GROUP'  , the " \
             "question and the contexts is about 'OCP' you must reply from the " \
             "context  , please read the context " \
             ":<< " + con + " >>, question in french : " + question + " \nreply in darija marocain : "
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2000
    )
    answer = response.choices[0].text.strip()
    return answer
def translat_from_darija(q):
    prompt = f"translat this text from   marocain darija  to english  , and translat it clearly , without any chnages \n"\
             f"DarijaText: {q} \n EN_Text: "
    # response = openai.Completion.create(
    #     engine="gpt-3.5-turbo",
    #     prompt=prompt,
    #     max_tokens=1000
    # )todo 9ad had zft
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an transaltor , the users will send you the text dirctly and you must translat it , you don't undrstand anything"
                                          " , you just translat the  messages"
                                          " directly  to french , ."
                                         },
            {"role": "user", "content": q}
        ]
    )
    answer =response.choices[0].message.content
    return answer