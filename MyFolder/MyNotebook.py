# Databricks notebook source
print("hello world")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "SQL hello world"

# COMMAND ----------

# MAGIC %md
# MAGIC # Title1
# MAGIC ## Title2
# MAGIC ### Title3
# MAGIC
# MAGIC text with a **bold** and *italicized* in it.
# MAGIC
# MAGIC Ordered list
# MAGIC 1. onec
# MAGIC 1. onec
# MAGIC 1. onec
# MAGIC
# MAGIC Unordered list
# MAGIC * apple
# MAGIC * peaches
# MAGIC * bananas
# MAGIC
# MAGIC Images:
# MAGIC ![](https://www.databricks.com/en-website-assets/static/45a46db7611db9405e5a94f1b16475f1/13806.png)
# MAGIC
# MAGIC And of course, tables:
# MAGIC | user_id | user_name |
# MAGIC |---------|-----------|
# MAGIC | 1 | adam |
# MAGIC | 2 | sarah |
# MAGIC | 3 | John |
# MAGIC
# MAGIC Links(or Embedded HTML): <a href="https://www.webassessor.com/" target="_blank">Manage exam</a> 

# COMMAND ----------

# MAGIC %run ./includes/setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')
print(files)

# COMMAND ----------

display(files)

# COMMAND ----------

# MAGIC %md
# MAGIC
