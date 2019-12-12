# Connect to Redshift with SQL Workbench

1. Start SQL Workbench and open a Connection Profile

2. Select the Driver. Use "Amazon Redshift (com.amazon.redshift.jdbc.Driver)"

3. Set Username. Use "master"

4. Set Password. Use "WelcomeIn1"

5. Select "Autocommit"

6. Click "OK"

7. Copy the SQL script from the repository into SQL Workbench and run 

8. Verify the table was created by running a select
```
SELECT * FROM sales_XXX.products_XXX LIMIT 100;
```

9. Go to Glue Jobs

10. Select the glue job. "glue-tutorial-XXX"

11. Select "Action" and click "Run job"

12. Wait for the job run status to display "Succeeded"

13. Go back to SQL Workbench

14. Re run select statement and verify that data was loaded
```
SELECT * FROM sales_XXX.products_XXX LIMIT 100;
```


[Back](README.md)