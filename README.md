## lambda_notifications

Sending notifications about S3 object changes through AWS Lambda.

### Functions
The repository structure allows holding multiple functions related to the topic of 'S3 - Lambda notifications'. Each function can be considered as an isolated logical unit.  
  
All Lambda functions in this repository use modules included in **Python 3.6** standard library and the libraries specified 
in **requirements.txt** files of each function.  
  
In order to create an archive for AWS Lambda function follow the instructions in _'Building an archive'_ section

#### basic
This function represents a basic logic of notifying a single recepient about the changes in an S3 bucket.


### Building an archive

To build an archive of your lambda function simply execute *build.sh* from the root directory with the path to the function.
For example:
```
sh build.sh functions/basic
```

### Testing
To run the tests execute the following command from the project root folder
```
python -m pytest tests
```


### Uploading a function

You can read more about AWS Lambda in the [oficial guide](http://docs.aws.amazon.com/lambda/latest/dg/welcome.html).  
In short, you can follow these steps to have the code runngin:
1. Login to the [Lambda console](https://eu-central-1.console.aws.amazon.com/lambda/home?region=eu-central-1) and select your region
1. Create a function based on _hello-world-python3_ template
1. Clone the repository and build the function archive as described above
1. Upload the archive to your newly created function
1. Test the function and setup S3 triggers
