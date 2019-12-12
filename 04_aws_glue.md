# Create Glue Connection and Job

1. Click "Add connection"

2. Connection name should be "glue-tutorial-XXX"

3. Select Connection type. Use "JDBC"

4. Click "Next"

5. Enter JDBC URL. This can be found in Redshift as described in Setup

6. Enter Username. Use "master"

7. Enter Password. Use "WelcomIn1"

8. Select vpc

9. Select subnet

10. Select Security group

11. Select "Next"

12. Click "Test connection"

13. Select IAM role

14. Click "Test connection"

15. Verify glue-tutorial-XXX connected successfully to your instance

16. Click "Add job"

17. Enter a name. Use "glue-tutorial-XXX"

18. Select IAM role. Use "AWSGlueServiceRole-glueServiceRole"

19. Select "A new script to be authored by you"

20. Select Python

21. Enter Script file name. Use "glue-tutorial-XXX"

22. Enter S3 path where the script is stored. Use "s3://glue-tutorial-XXX/glue-scripts"

23. Enter Temporary directory: s3://aws-glue-temporary-952552944372/jack.silverman

24. Expand "Script libraries and job parameteres(optional"

25. Change Concurrent DPU's per job run to "2"

26. Enter key and values for Job parameters
```
Parameters:
--REDSHIFT_DB_NAME			sales
--SCHEMA_NAME				sales-XXX
--TABLE_NAME				products-XXX
--CATALOG_CONNECTION			glue-tutorial-XXX
```

27. Click "Next"

28. Select "glue-tutorial-XXX" Redshfit connection

29. Click "Next"

30. Click Save job and edit script

31. Update the script
```
See glue script in repository.
```

32. Click "Save"


[Back](README.md)