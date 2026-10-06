## DataBricks
Data Bricks is a multicloud lakehouse plateform based on **Apach Spark**.

### Data Lakehouse
A Data lakehouse is a unified analytics plateform that combine the best elements of Data lakes and Data Warehouse. It unified all of your data engineering analytics and ai workloads.
- Data Lake : 
    - open
    - flexible
    - ml support
- Data Warehouse :
    - Reliable
    - Strong gouvernance
    - Performance

### Databricks Architecture Lakehouse 
![](/Data%20Engineering/DataBricks/Assets/Databricks%20Lakehouse%20Architecture.png)

- The architecture is compose of three important layer :
    - the Cloud services : Aws, Azure , Gcp
    - the runtime :  Spark, Delta Lake
    - the workspace : Data Engineering, Data warehousing, Machine learning
- DataBricks use infrastructure of cloud provider to provision virtual machine, or a cluster, and this cluster come with databricks runtime pre-install.

![](/Data%20Engineering/DataBricks/Assets/Databricks%20Ressources%20Deployment%20in%20Cloud.png)
- There are two high level component :
    - Control plan : Databricks Account( Web UI, Cluster Management, Workflow, Notebooks)
    - Data Plan : Customer cloud account( Cluster Vms, Stockage DBFS(DataBrics File System))
- When you create a databricks workspace , it is deploy in the control plan along with databricks services
- On the other hand a third accound is deploy in the data plan in your own cloud subscription
- it is use to store the data into dbfs
- in addition when ou create a cluster , the cluster of virtual machine will be deploy in data plan 
- compute and storage are always in your own cloud account
- databricks provide tools to control infrastructure

### Apache spark
- Databricks have the same founder than Apache spark
- Because of spark, data is distributed an processed in memory of multiple nodes
- Databricks support python, scala, R, sql, Java
- It support Batch processing and stream processing
- It can processed structured semi-structured or unstructured data

### DBFS( DataFrics File System)
![](/Data%20Engineering/DataBricks/Assets/DBFS%20Functioning.png)

- DBFS is a distributed storage solution
- Databricks offer the native support for it
- It come preinstallon databrics cluster
- We usually use it to persist data and file but DBFS is just an abstraction layer
- It use the underlying cloud storage to persist

### Working space
- The inteface frquently change
- New button :  quicly create notebooks, clusters, jobs
- workspace : organise resources
- Catalog : Manage data 
- Workflow : create data pipelines
- Compute : Create and manage cluster
- Marketplace : exchange data products
- Sql :  Databricks Sql services, manage data wharehouse and BI solutions
- Data engineering : monitor jobs executions, ingest data from externals sources, build data pipelines
- Machine learning :  Manage AI and datascience products


### Cluster Creation 
- a cluster is a sets of nodes workings together like one entity
- it have a master node and workers nodes
- master(driver) coordinates workers and parallees executions of tasks
- For create the cluster :
    - create compute
    - policy (configurable or not)
    - multinode or not
    - photon or not
    - can be shared but limited( python, sql)
    - configure driver runtimes
    - configure workers runtimes
    - autoscaling or not( nodes scales automaticly)
    - time of terimination of a cluster after inactivity

- We can see the DBU (DataBricks Units)
- Represent Unit of processing capaility per hours
- Each configuration tells you  how much DBU would be consume a virtual machine per hour
- less number of worker reduce DBU
- to access cluster got to compute
- you can start, terminate or edits
- changing configuration require restart
- you can visualise events logs


### Notebooks Fundamentals 
- To create notebook, we simply click on create  and select notebooks
- Change the notebook name
- we connect the notebook to the cluster
- By default notebook language is python
- we can change the language of the notebook
- we can change the language of a specific cell
- notebook provide cell by cell execution of commands
- magic command are identify by **%** at the start of a cell
- ex : 
```SQL
    %sql
    Select("Hello !")
```
- magic command are built in command that provide the same output as the language in the cell , regadless of the cell language
- it start with a % ex: %sql
- it is called language magic command
- %md execute markdown in the cell
- %run run a cell, it also alwo to run another notebook in a cell ex: %run .path/notebook_names
- all variable will be available in current notebook
- it help build notebook in modular approach
- %fs command deal with files systems operation
- ex : %fs ls '/path-datasets'
- another way to deals with file system is to use dbutils
- dbutils provide a number of utility commands for configuring and interactings with the environnement
- ex : dbutils.fs.helps()
- ex : dbutils.helps()
- with dbutils you can interact with differents services and tools like : credentials, fs(file system),secrets, widgets, 
- dbutils.fs.ls('paths')
- dbutils is more useful than %fs because it can be use in python code
- display inprove dbutils function outputs
- with display you can be download data as csv
- we can export our notebooks
- we can export folders of notebooks
- Variable Explorer: you can view all the variables defined in a notebook session, including their names, data types, and current values.
- The Variable Explorer also presents additional information for Spark and Pandas DataFrames. The shape and column names are available at-a-glance, and full view of the schema is available on hover.
- Python  Interactive debugger: Databricks Notebooks now support interactive debugging for real-time inspection of Python code execution. By setting breakpoints directly in your notebook, you can pause execution and inspect variable values at runtime, which is ideal for identifying logic errors.
    - Add one or more breakpoints by clicking in the margin of a cell.
    - Start the debugging session by clicking "Debug cell"
    - A debug session starts automatically, where you can use the debug toolbar to go through your code step by step.


### Git Folders
- Notebook have some basic version control built in but it is better to use Github
- GitFolders(databricks repo) provide source control for your data projects by integrating with github providers
- you must connect your workspace to your github account to do advance modifications
- then create a git project in github
- you create a git folder in the workspace that you link with it
- you can create a new branch, do some modification, commit and push , merge and then pull and see the result in the main





### Delta Lake
![Delta Lake Architecture](/Data%20Engineering/DataBricks/Assets/Delta%20Lake%20Architecture.png)
- Delta lake is an opensource storage framework that bring reliablity to data lakes
- data lakes haves many limitations suchs as data inconsistency and performance issues
- Delta lake is :
    - opensource
    - storage framework/layer not a format/medium
    - enable building lakehouse not datawarehouse /database
- lakehouse is the plateform that unified both datawarehouse and advance analytics
- delta lake is deployed on the cluster as part of the databricks runtime 
- if you create delta lake table, it get stored on the storage on one or more datafile in parquet format.
- with this file are store **transaction log**
- transaction log ( delta log) : ordered record of every transaction performed on the table
- it serve as single source of truth
- evry time you query the table, spark check this transactions log to retrieve the most recent version
- each commited transaction is recorded in the JSON file (transaction log)
- it contain operation that have been performed (insert update)
- predicate (conditions and filters )
- files affected by the operations

#### First Scenario : Write and Reads
![Scénario 1](/Data%20Engineering/DataBricks/Assets/Delta%20Lake%20Scenario%201.png)
- when the write process start it store two file in parquet format
- when the write operation finish it add the transaction log into the delta.log directory
- the reader process always start by reading transaction log that contain information about file 1 and 2
- in this case it start reading them

#### Second Scenario : Update
![Scenario 2](/Data%20Engineering/DataBricks/Assets/Delta%20Lake%20Scénario%202.png)
- the writer process uptade a record in file 1
- instead of updating the record in the file itself, it will make a copy of it and make change
- it then update the transaction.log
- the log then know that file 1 is no longer need
- now when reader process start only file two and three are part of current table version
- so it can read them

#### Third Scenario : Simultanous Write and Read
![Scenario 3](/Data%20Engineering/DataBricks/Assets/Delta%20Lake%20Scenario%203.png)
- the writer process start writing the file 4
- at the same time the reader start reading transaction log who only have information about 2 and 3
- and not 4 which is not  fully written
- so it start read the file who represent the most recent data at the moment
- you will always have the most recent data
- your read operation will never have a deadlock or conflick with any ongoing operation



#### Fourth Scenario : Failed Writes
![Scenario 4](/Data%20Engineering/DataBricks/Assets/Delta%20Lake%20Scenario%204.png)
- the writer process start writng file 5 to the lake
- but this time there is an error in the jobs
- it add an incomplete file
- but because of this failure delta lake doesnot write any information in the log
- reader will only read 2, 3 and 4
- delta lake garanteed you will never read dirties data


#### Delta Lake advantages :
- Bring acid transacions to object storage
- handle scalable metadata
- full audit trail of all changes
- build upon standard data format = parquet + json


### Advance Feature of Delta Lake 
- Time Travel
- Compacting Small Files and Indexing
- Vacuum

#### Time travel
- Each operations is automaticly versionned
- audit data changes
- We can **provide full history of modification** on the table
- Command : **DESCRIBE HISTORY** TABLE
- We can query older version of the table
- We use TIMESTAMP
- SELECT * FROM table TIMESTAMP AS OF "2019-01-01"
- We can also use a version number
- SELECT * FROM table VERSION AS OF 36
- SELECT * FROM table@v36
- 
- We can Rollback Version
- Command : **RESTORE TABLE**
- Roll back to a date : RESTORE TABLE table_name TO TIMESTAMP AS OF "2019-01-01"
- Roll back to a version : RESTORE TABLE table_name TO VERSION AS OF 36

#### Compaction
- delta lake can improve the query of reading the table that is compose of many small file
- compacting small file
- Command : **OPTIMISE**
- OPTIMISE table_name
- we compact many small file into lower number file
- We can Compact by indexing
- indeed we can apply **ZORDER BY** column_name
- It will reaoganize the file around indexing table
- OPTIMISE my_table ZORDER BY column_name
- it co-locate column information

#### VACUUM 
- clean up unsused file
- file that are uncommited 
- file that are not in the latest table state
- VACUUM table_name [retention period(7 days by default)]
- vacuum implie no longer time travel because file are no longer exist



### DATA FILE LAYOUT OPTIMISATION
- Concept of Datafile Layout 
    -   Data File layout refers to the organisation and storage of the underlying data files that make up the delta tables
    - Optimizing layout help leveraging data skipping algorithms
    - it ensure that only relevent data are read when executing a query
- Exploring optimisation technique
    - Partitionning ( Hive Style Partitionning) : method of organizing a table by grouping rows that share same values for predefined partitioning columns
        - To enable partitionning we simply use : PARTITIONED BY column_name during table creation
        - Create Table ma_table(id INT, name STRING, year INT) PARTITIONED BY year
        - To apply Partition **Skipping** we apply filtering
        - ex : Select * from ma_table where year = 2023
        - partitionning improve the performance but only for huge delta tables
        - Small to medium size does not benefit from partition
        - Partition physically separate data into subfolders
        - OPTIMIZE commands will only be applied at the partition level to compact data files, which leave us with a small file problem in the table.
        - Then it prevent file compaction across boundaries
        - Partitionning is inneficient for high cardinality columns
        - create a lots of partition
        - if business requirement evolve, you may have to rewrite all table
        - As a best practice, you should default to non partition tables for most use cases when working with
        - instead we can use Zorder indexing

    - Z-Order indexing
        - column need to be specified at each run of th optimised command
        - Z-order indexing group your data into optimised file without creating subfolders
        - leverage data skipping algorithms
        - effective for high cardinality columns
        - the main issue with Z-ORDER indexing is that it is not incremental operation
        - when new data is ingested , you must rerun the optimise command to reorganise the data
        - rerunning the command result in recreation of all files in the entire table
        - instead we can use liquid clustering

    
    - liquid clustering
        - Improved version of Z-order indexing
        - like partitionning , liquid clustering is defined at the defined at the table level by specifying your clutering keys, no need to call it like we call column at each optimized
        - Create table1 (col1 INT, col2 STRING, col3 Date) CLUSTER BY (col1,col3)
        - Alter Table table2 CLUSTER BY (clustering columns)
        - clustering is not compatible with partitionnig or zordering
        - You can create a new table by projecting the existing table and using the previous partition columns and Z-order columns as clustering keys.
        - To trigger clustering, simply use the **OPTIMIZE** command on your table.
        - This is an incremental operation on a new data ingestion.
        - It is smart enough to know that old data is already well clustered.
        - So on the next run of the optimize command, only unoptimized files are affected
        - while files already optimized are simply ignored.
        - As a result, optimize operation for clustered tables run quickly and efficiently.
        - Moreover, liquid clustering provides the flexibility to redefine clustering keys without rewriting existing data.
        - So you can evolve your data layout alongside your business needs over time.
        - **Choosing clustering Keys**
        - The optimal way is to choose them based on your query pattern
        - specifically those that are frequently used in query filters.
        - However, such an insight may not be available during the creation of new tables.
        - To address this challenge, you can use Automatic Liquid Clustering. 
        - with Automatic Liquid Clustering,
        - Databricks automatically chooses clustering keys by analyzing 
        - the table historical query workloads.
        - This requires activating a feature called Predictive Optimization on Unity Catalog managed tables.
        - To enable Automatic Liquid Clustering on such tables, simply use the clause: CLUSTER BY AUTO.


### DATA BASES AND TABLES ON DATA BRICKS 
- Manage table are define without specifying location table
- to create an external table you need to specify location table
- we can easily drop managed table
- if delete external table , underlying files are still there


### SETTING UP DELTA LAKES TABLES
- CTAS STATEMENTS 
    - In addition to regular CREATE TABLE statements, we can use CTAS statements to create Delta tables.
    - CTAS statements or Create Table As Select statements create and populate data tables using the output of a SELECT statement.
    - exemple : CREATE TABLE_1 AS SELECT * FROM TABLE_2
    - CTAS statements automatically infer schema information from query results
    - and do not support manual schema declaration.
    - With CTAS statements, we can do simple transformations like changing column names or omitting columns from target tables during table creation.
    - ex : CREATE TABLE_1 AS SELECT col_1, new_col_3 FROM TABLE_2
    -  the Create Table clause contains several options.
    - You can provide a descriptive comment for the table.
    - The underlying data of a data table can be partitioned in subfolders by the value of one or more columns.
    - the created table with CTAS statements can be an external table, so the data will be stored
    in an external location specified by the LOCATION keyword.
    - Regular CREATE TABLE statements need manual schema declaration.
    - While CTAS statements do not support manual schema declaration.
    - They automatically infer schema information from query results.
    - Regular CREATE TABLE statements create an empty table.
    - you need an INSERT INTO statement to load data into the table.
    - On the other hand, with CTAS statements, data will be inserted during table creation from the output of the SELECT statement.

- TABLE CONSTRAINTS
    - once you create your Delta table, either with a regular create table or CTAS statements
    - you can add constraints to your table.
    - Databricks currently supports two types of table constraints, NOT NULL constraints and CHECK constraints.
    - In both cases, you must ensure that there is no data violating the constraint is already in the table prior to defining the constraint.
    - Once a constraint has been added to a table, new data violating the constraint would result in write failure.
    - ALTER TABLE table_name ADD CONSTRAINT contrain_name constraint_details
    - ex: ALTER TABLE orders ADD CONSTRAINT valid_date CHECK(date>'2020-01-01')
    - Note that Check constraints look like standard WHERE clauses you might use to filter a dataset.

- CLONING DELTA LAKE TABLES
    - delta Lake has two options for efficiently copying Delta Lake tables.
    - Either deep clone or shallow clone.
    - Deep clone fully copies both data and metadata from a source table to a target.
    - CREATE TABLE table_clone DEEP CLONE source_table
    - This copy can occur incrementally.
    - executing this command again can synchronize changes from the source to the target location
    -  because all the data must be copied over, this can take a while for large data sets.
    - With shallow Clone, you can quickly create a copy of a table. Since it just copies the Delta transaction logs.
    - a good option, for example, to test out applying changes on a table without the risk of modifying the current table.


### VIEWS
- A view in Databricks is a virtual table that has no physical data. In fact, it is just a saved SQL query against actual tables.
- this query is executed each time a view is queried.
- You can create them with select statement

- Classic VIEWS(stored views)
    - They are persisted in databases
    - drop only by drop view
    - CREATE VIEW AS QUERY
- TEMP VIEWS
    - Session scoped
        - Spark session is created.
        - when opening a new notebook, a new session is created.
        - when detaching and reattaching a notebook to a cluster.
        - after installing a Python package, which leads to restarting the python interpreter.
        - simply after restarting the cluster.
    - dropped when session end
    - CREATE TEMP VIEW
- GLOBAL TEMP VIEWS
    - cluster scoped
    - dropped when cluster restarted
    - create global temp view




