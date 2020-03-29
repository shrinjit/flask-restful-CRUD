from flask_restful import Resource   ## converting the class task into a resource 
import logging as logger 



class Task(Resource):
    def get(self):
        logger.debug("inside the get method")
        return {"message": " Inside the Get method"} ,200

    def post(self):
        logger.debug("inside the post method")
        return {"message":"Inside the post"} ,200

    def put(self):
        logger.debug("inside the put  method")
        return  {"message":"Inside the put"} ,200

    def delete(self):
        logger.debug("inside the delete method")
        return {'message':"inside the delte"},200