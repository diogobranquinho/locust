from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):  
    @task
    def index(self):
        self.client.get("/")
        
class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = "http://fatecsjc-prd.azurewebsites.net/"
    min_wait = 5000
    max_wait = 15000