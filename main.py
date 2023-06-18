import yaml

from PineCone import put, get

# from chatGpt import answer , chatGPT
from chatgpt import chat , translat_from_darija
import spacy

# first download the en_core_web_lg model
# use this command <python -m spacy download en_core_web_lg>
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
checko = spacy.load('en_core_web_lg')
count = 0
def check(x):
    global count
    count += 1
    return checko(x)


paths = []
texts = []
import os

with open("text.txt", "r", encoding="utf8") as f:
    data = f.read()
chunkss = data.split(".")
chunks = []

for i in range(0, len(chunkss) - 2, 3):
    chunks.append(chunkss[i] + " " + chunkss[i + 1] + " " + chunkss[i + 2])


def start1():
    ids = ["text" + str(i) for i in range(len(chunks))]
    vectors = [list(check(chunk).vector) for chunk in chunks]
    print(put(ids, vectors))
    return len(ids)


def start2():
    chunk_size = 1000  # Maximum number of vectors allowed per request
    ids = ["text" + str(i) for i in range(len(chunks))]
    vectors = [list(check(chunk).vector) for chunk in chunks]
    for i in range(0, len(ids), chunk_size):
        start_idx = i
        end_idx = min(i + chunk_size, len(ids))
        chunk_ids = ids[start_idx:end_idx]
        chunk_vectors = vectors[start_idx:end_idx]
        print(put(chunk_ids, chunk_vectors))
    return len(ids)

# start1()
prompt = ""


def getReply(q, dictt={}):
    q = translat_from_darija(str(q))

    # result = get(check(q).vector)
    #
    # index = [int(str(i["id"]).replace("text", "")) for i in result["results"][0]["matches"]]
    # # index = int(str(result["results"][0]["matches"][0]["id"]).replace("text",""))
    # contexts = [chunks[i] for i in index]
    #
    # reply = chat(q, contexts)

    return q #reply
import random
ktb = ["kteb chi haja mafhoma !" ,  "mafhemtkch mzzn !? " , "hawl tsowlni m9ad !" , "3lach baghi t3adbni bhad lmessage ??" ," 3awed ktb chno baghi tsawl !" , "bach katkteb ? hawl tkteb bi sba3ek.","kteb liya 3afak message mfhom bach n9dr njawbek!"]
while True:
    q = input("ana : ")

    if q in ["salit" , "tfa" ,"exit"]:
        break
    if  len(q.strip()) > 1 :
        print(" OCP_BOT : "+ getReply(q=q))
    else:
        print(ktb[random.randint(0, len(ktb) - 1)])
