import docker


# client = docker.from_env()
# print("Client created")


# image = "continuumio/miniconda3"
# name = "simple_sample"
# binds = {
#     "/home/letyndr/airflow/dags": {
#         "bind": "/home/letyndr/airflow/dags",
#         "mode": "rw"
#     },
#     "/home/letyndr/airflow-data/ml-intermediate": {
#         "bind": "/home/letyndr/airflow-data/ml-intermediate",
#         "mode": "rw"
#     }
# }

# client.containers.list()

# client.containers.create_container(
#     image,
#     name=name,
#     volumes=[volumes],
#     command="sleep 600",
# )

#######################################################################################

client = docker.APIClient()

container = client.create_container(
    image="continuumio/miniconda3",
    command="sleep 600",
    volumes=["/home/letyndr/airflow/dags", "/home/letyndr/airflow-data/ml-intermediate"],
    host_config=client.create_host_config(binds={
        "/home/letyndr/airflow/dags": {
            "bind": "/home/letyndr/airflow/dags",
            "mode": "rw"
        },
        "/home/letyndr/airflow-data/ml-intermediate": {
            "bind": "/home/letyndr/airflow-data/ml-intermediate",
            "mode": "rw"
        }
    }),
    working_dir="/home/letyndr/airflow/dags",
    name="simple_example",
)

client.start(container=container.get("Id"))


########################################################################################


# import docker

# client = docker.from_env()
# image = "continuumio/miniconda3"
# name = "simple_sample"
# volumes={
#     "/home/letyndr/airflow/dags": {
#         "bind": "/home/letyndr/airflow/dags",
#         "mode": "rw"
#     },
#     "/home/letyndr/airflow-data/ml-intermediate": {
#         "bind": "/home/letyndr/airflow-data/ml-intermediate",
#         "mode": "rw"
#     }
# }

# print("Running container")

# client.containers.run(
#     image,
#     name=name,
#     volumes=volumes,
#     command="sleep 600",
# )

# print("Successfully run!")
