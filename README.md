# BqOperatorFix
custom BQ operator with bug fix
https://stackoverflow.com/questions/55300785/google-cloud-composer-bigquery-operator-get-jobs-api-httperror-404

* Copy BqOperatorFix folder as it is in your plugins folder.
* Change import statement in your dag to this

 ```from BqOperatorFix.operators.custom_bq_operator import BigQueryOperator```
 
 
