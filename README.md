# aws

## CDK commands:

`cdk configure`
    - To configure IAM user with key and pass.

`cdk bootstrap`
    - To create template of resources at cloudformation with the role of configures user.

`cdk deploy`
    - CDK uses CloudFormation as its deployment engine, so the "cdk deploy" command essentially manages the process of generating and deploying a CloudFormation stack.

## Other commands :

- `aws configure list`
    - Lists all the configuration like, key, pass and region.
        access_key     ****************FL7M shared-credentials-file    
        secret_key     ****************t2lE shared-credentials-file    
            region               ap-south-1      config-file    ~/.aws/config

- `pip install aws-cdk-lib==2.168.0`
- `npm install -g aws-cdk`
- Docker path
    `export PATH="$PATH:/Applications/Docker.app/Contents/Resources/bin/"`

- Docker build and run
    - `docker build -t my-python-app -f .`
    - `docker run -p 8000:8000 my-python-app`

- Conda initialization for maxc
    - `source /Users/anvesh/opt/anaconda3/bin/activate`


<!-- aws-cdk.core
aws-cdk.aws-lambda
aws-cdk.aws-apigateway -->