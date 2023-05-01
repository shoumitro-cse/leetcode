from itertools import zip_longest
import pandas as pd

dict_data = [
{'name': 'John0', 'age': 300, 'city': 'New York0'}, 
{'name': 'John1', 'age': 301, 'city': 'New York1'}, 
{'name': 'John2', 'age': 302, 'city': 'New York2'}, 
{'name': 'John3', 'age': 303, 'city': 'New York3'}, 
{'name': 'John4', 'age': 304, 'city': 'New York4'},
{'name': 'John5', 'age': 305, 'city': 'New York5'},
{'name': 'John6', 'age': 306, 'city': 'New York6'},
{'name': 'John7', 'age': 307, 'city': 'New York7'},
{'name': 'John8', 'age': 308, 'city': 'New York8'},
{'name': 'Jack0', 'age': 300, 'city': 'New York0'}, 
{'name': 'Jack1', 'age': 301, 'city': 'New York1'}, 
{'name': 'Jack2', 'age': 302, 'city': 'New York2'}, 
{'name': 'Jack3', 'age': 303, 'city': 'New York3'}, 
{'name': 'Jack4', 'age': 304, 'city': 'New York4'},
{'name': 'Jack5', 'age': 305, 'city': 'New York5'},
{'name': 'Jack6', 'age': 306, 'city': 'New York6'},
{'name': 'Jack7', 'age': 307, 'city': 'New York7'},
{'name': 'Jack8', 'age': 308, 'city': 'New York8'},
]


def iter_to_chunk(iter_data, chunk_size, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # json_to_chunk('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iter_data)] * chunk_size
    return zip_longest(*args, fillvalue=fillvalue)

dfs = []
chunk_size = 3 # size of chunk for each block
for json in iter_to_chunk(dict_data, chunk_size):
    df = pd.json_normalize(json)
    dfs.append(df)
    print(json)
    
df = pd.concat(dfs) 
print(df)



"""
args = [iter(dict_data)] * 3
js = zip_longest(*args, fillvalue=None)
for d in js:
  print(d, '\n')

output:
({'name': 'John0', 'age': 300, 'city': 'New York0'}, {'name': 'John1', 'age': 301, 'city': 'New York1'}, {'name': 'John2', 'age': 302, 'city': 'New York2'}) 

({'name': 'John3', 'age': 303, 'city': 'New York3'}, {'name': 'John4', 'age': 304, 'city': 'New York4'}, {'name': 'John5', 'age': 305, 'city': 'New York5'}) 

({'name': 'John6', 'age': 306, 'city': 'New York6'}, {'name': 'John7', 'age': 307, 'city': 'New York7'}, {'name': 'John8', 'age': 308, 'city': 'New York8'}) 

({'name': 'Jack0', 'age': 300, 'city': 'New York0'}, {'name': 'Jack1', 'age': 301, 'city': 'New York1'}, {'name': 'Jack2', 'age': 302, 'city': 'New York2'}) 

({'name': 'Jack3', 'age': 303, 'city': 'New York3'}, {'name': 'Jack4', 'age': 304, 'city': 'New York4'}, {'name': 'Jack5', 'age': 305, 'city': 'New York5'}) 

({'name': 'Jack6', 'age': 306, 'city': 'New York6'}, {'name': 'Jack7', 'age': 307, 'city': 'New York7'}, {'name': 'Jack8', 'age': 308, 'city': 'New York8'}) 

"""




