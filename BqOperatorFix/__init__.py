
from airflow.plugins_manager import AirflowPlugin
from BqOperatorFix.operators.custom_bq_operator import BigQueryOperator
from BqOperatorFix.operators.custom_bq_to_bq import BigQueryToBigQueryOperator

class BqOperatorFix(AirflowPlugin):
    name = "BqOperatorFix"
    operators = [BigQueryOperator,BigQueryToBigQueryOperator]
    # Leave in for explicitness
    hooks = []
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = []
    menu_links = []
