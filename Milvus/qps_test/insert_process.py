# -*- coding: utf-8 -*-
#Connectings to Milvus and Redis

# import redis
from pymilvus import *

connections.connect(host="127.0.0.1", port=19530)

schema = CollectionSchema([
            FieldSchema("text_id", DataType.INT64, is_primary=True),
            FieldSchema("text_vector", dtype=DataType.FLOAT_VECTOR, dim=400)
    ])
collection = Collection("test_vector_search")
collection.load()
print('nums: ', collection.num_entities)
# collection.drop()
# collection = Collection("test_vector_search", schema, using='default', shards_num=5)
import random
import numpy as np
data_num = 2015 # 10000

while True:
    input("tap any key to insert 10000 vectors")
    data = [
            [i for i in range(0, data_num)],
            np.random.rand(data_num,400).tolist()
            ]
    print("data generated done ! ")
    print(type(data), type(data[0]), type(data[0][0]))
    collection.insert(data)
    index_param = {
                    "metric_type":"L2",
                    "index_type":"IVF_SQ8",
                    "params":{"nlist":1024}
            }
    collection.create_index("text_vector", index_params=index_param)
    print('nums: ', collection.num_entities)
    #     ]

