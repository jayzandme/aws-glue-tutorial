# Run SQL queries in Athena to verify data has been populated

1. Enter any queries in the Query Editor and click "Run query"

```
# Verify all columns are populated
select * from glue_tutorial_XXX limit 100
```

```
# Verify the total row count is: 888475
select count(*) from glue_tutorial_sales
```

2. Click "Run query"

3. Verify output is as expected. 


[Back](README.md)