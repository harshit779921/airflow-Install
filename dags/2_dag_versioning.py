from airflow.decorators import dag, task

@dag(
        dag_id="versioned_dag",
)
def versioned_dag():

    @task.python
    def first_task():
        print("This is the first task")

    @task.python
    def second_task():
        print("This is the second task")
    
    @task.python
    def third_task():
        print("This is the third task. DAG complete!")
    
    @task.python
    def fourth_task():
        print("This is the fourth task. DAG versioning implemented!")

    @task.python
    def version_task():
        print("This is the version task. DAG versioning implemented!")
    
    # Defining task dependencies
    first = first_task()
    second = second_task()
    third = third_task()
    fourth = fourth_task()
    version = version_task()
    
    first >> second >> third >> fourth >> version

# Instantiating the DAG
versioned_dag()