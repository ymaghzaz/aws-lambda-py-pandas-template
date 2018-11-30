import json
import sys
import pandas as pd
import numpy as np 
print("hello"  , pd.__version__)
l=[]
l2=[1,2,3,4,5]
l=np.append(l,l2)
d = pd.DataFrame()
print("hell" + str(l))
def hello(event, context):
   
    body = {
        "message": "caffe Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
