import os, json
data = os.getenv("multi_lp")
print(json.loads(data)["hello"])
print("hello world")
