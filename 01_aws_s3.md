# Create S3 bucket and Add Data file

1. Go to AWS S3 service

2. Click "Create bucket"

3. Give your S3 bucket a name. Use "glue-tutorial-`<initials>`"

4. Specify the region as "US-East-1 (N. Virginia)"

5. Click "Create"

6. Add file from repository called "WA_Sales_Products_2012-14.csv"

Or you can do this via the aws console or with in the command line with cli

```
$ aws s3api create-bucket --bucket  glue-tutorial-XXX --region us-east-1
```

7. Click "Upload"


[Back](README.md)