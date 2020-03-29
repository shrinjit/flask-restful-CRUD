from flask_restful import Resource   ## converting the class task into a resource 
import logging as logger 



class TaskById(Resource):
    def get(self,taskbyId):
        logger.debug("inside the get method")
        return {"message": " Inside the Get method taskid={}".format(taskbyId)} ,200

    def post(self,taskbyId):
        logger.debug("inside the post method")
        return {"message":"Inside the post taskid={}".format(taskbyId)} ,200

    def put(self,taskbyId):
        logger.debug("inside the put  method")
        return  {"message":"Inside the puttaskid={}".format(taskbyId)} ,200

    def delete(self,taskbyId):
        logger.debug("inside the delete method")
        return {'message':"inside the delte taskid={}".format(taskbyId)},200