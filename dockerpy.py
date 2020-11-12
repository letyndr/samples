import docker

client = docker.APIClient()

# binds = {
#         "/home/letyndr/airflow/dags": {
#             "bind": "/home/letyndr/airflow/dags",
#             "mode": "rw"
#         },
#         "/home/letyndr/airflow-data/ml-intermediate": {
#             "bind": "/home/letyndr/airflow-data/ml-intermediate",
#             "mode": "rw"
#         }
#     }

binds = ["/home/letyndr/airflow/dags:/home/letyndr/airflow/dags:rw",
"/home/letyndr/airflow-data/ml-intermediate:/home/letyndr/airflow-data/ml-intermediate:rw"]

container = client.create_container(
    image="continuumio/miniconda3",
    command="sleep 600",
    volumes=["/home/letyndr/airflow/dags", "/home/letyndr/airflow-data/ml-intermediate"],
    host_config=client.create_host_config(binds=binds),
    working_dir="/home/letyndr/airflow/dags",
    name="simple_example",
)

client.start(container=container.get("Id"))
