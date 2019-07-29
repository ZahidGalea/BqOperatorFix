
from airflow.plugins_manager import AirflowPlugin
from BqOperatorFix.operators.custom_bq_operator import BigQueryOperator

class BQCustomPlugin(AirflowPlugin):
    name = "BQCustomPlugin"
    operators = [BigQueryOperator]
    # Leave in for explicitness
    hooks = []
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = []
    menu_links = []
