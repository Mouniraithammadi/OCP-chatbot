
import pinecone
import pandas as pd
import numpy as np
import yaml
# use python 311
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
pinecone.init(api_key=config["Pinecone_api_key"],environment=config["environment"])
index = pinecone.Index(index_name=config["index_name"])

# def put(ids ,vectors):
#     df = pd.DataFrame(data={"id":ids ,"vector":vectors})
#     return index.upsert(vectors=zip(df.id,df.vector))
def put(ids, vectors):
    ids_arr = np.array(ids)
    arr = np.concatenate([ids_arr[:, np.newaxis], vectors], axis=1)
    vectors_list = [(str(id_), tuple(values)) for id_, *values in arr]
    return index.upsert(vectors=vectors_list)

def get(Vector):
    ndarray = np.array(Vector)
    # Convert to list
    vector = ndarray.tolist()
    res = index.query(queries=[vector],top_k=3)
    return res


