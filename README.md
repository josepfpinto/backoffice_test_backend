# Flask REST API 

This is a basic REST API on Python/Flask, with a Serverless Framework setup to launch the REST API Gateway and Flask Lambda in AWS.

## Steps
1. Clone this repo
2. Add your aws profile to serverless.yml and adjust aws region here (if necessary)
3. Make sure you add your user pool arn from cognito in a json file `config.dev.json`:
    - like so: { "USER_POOL_ARN": "arn:aws:cognito-idp:eu-west-1:xxx:userpool/eu-west-1_xxx" }
4. npx sls deploy