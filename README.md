# aws-lambda-py-pandas-template
How to use pandas or numpy or other python libraries in aws lambda ,
You add your lib into requirements.txt
```js
numpy==1.15.4
pandas==0.23.4
```

# Build 
You need to install sam for build your python library into a docker container 
https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html


```js
sam build --use-container
```

# Test 
```js
sam local invoke --event d.json
```



