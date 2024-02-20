# Using AWS CodeCommit + AWS Pipeline to update the Lambda Function

## Steps 

- Create a Repository using AWS CLI
        
        aws codecommit create-repository --repository-name lambda_repo

- Clone the Repo to your local (⚠️ configure aws user and git credentials )
  
        git clone https://git-codecommit.<region>.amazonaws.com/v1/repos/lambda_repo

- Setup the Repo Structure and code
  
    refer : [./lambda_repo](./lambda_repo/).

        cd lambda_repo

        mkdir lambda_one_codes lambda_two_codes

        # Add your Lambda code files in respective folders (e.g., lambda_function.py)

        
- Create a ```buildspec.yml``` file to mention the build steps 

    refer : [./lambda_repo/buildspec.yml](./lambda_repo/buildspec.yml)

-  This will update the code to the Lambda Function / Create a NEw one if one is not already present


- Create a CodeBuild and use the CodeCommit repo as the Source. Use the Default role and attach the Necessary Policy . I have attached AWS Lambda Full access (I have to create a function if needed)

- Create a CodePiepline to use CodeCommit repo as source and CodeBuild to build. Use cloudwatch logs to Trigger Builds on changes. Use the default role and attach the nessary policies to it.

- Now Push the codes to the repository

        git add .
        git commit -m "Initial commit"
        git push origin master


- This will trigger the pipeline to codebuild and the Updated code will be pushed to the respective lambda




