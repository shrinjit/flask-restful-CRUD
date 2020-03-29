from flask_restful import Api

from app import flaskAppInstance

from .task import Task
from .taskById import TaskById
restServer=Api(flaskAppInstance)


##there are body pararmeters , resource parameters etc
## simple CRUD application say task 
## we have to create a simple task .py file 
  ## attach the resource 
restServer.add_resource(Task,"/api/v1.0/task")
## for accepting the parameters 

restServer.add_resource(TaskById,"/api/v1.0/task/id/<string:taskbyId>")