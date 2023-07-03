# Databricks notebook source
print('hello word')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 'Test'

# COMMAND ----------

# MAGIC %md
# MAGIC # *Jora* er **best**

# COMMAND ----------

# MAGIC %run ./includes/Setup

# COMMAND ----------

full_name

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')
files

# COMMAND ----------

display(files)
