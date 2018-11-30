# aws-lambda-py-pandas-template
how to use pandas in aws lambda 

You need to install sam for build your python library into a docker container 
https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html


# Build 

```js
sam build --use-container
```

# Test 
```js
sam local invoke --event d.json
```



