# Create and run glue crawler

1. Click "Add database"

2. Give your database a name. Use “sales_XXX”

3. Click "Apply"

4. Click "Add tables"

5. Click "Add tables using a crawler"

6. Give your crawler a name. Use "glue-tutorial-XXX"

7. Click "Next"

8. Choose a data store. Use "S3"

9. Include path. Use "s3://glue-tutorial-XXX/products_XXX"

10. Click "Next"

11. Add another data store. Select "No"

12. Click "Next"

13. Select "Choose an existing IAM role"

14. Select "AWSGlueServiceRole-glueServiceRole"

15. Click "Next"

16. Select "Run on Demand"

17. Click "Next"

18. Select the database. Use “glue-tutorial-XXX”

19. Under Configuration options, select "Update the table definition in the data catalog"the data and in the redshift table

20. Select "Mark the table as deprecated in the data catalog"

21. Click "Next"

22. Click "Finish"

23. Click the checkbox to select your crawler and click "Run crawler"


[Back](README.md)