from flask import Flask
from src.logger import logging
from src.exception import CustommException
import  os,sys
app = Flask(__name__)

@app.route('/',methods= ['GET','POST'])

def index():
    try:
        raise Exception("we are testing our exception file") # error
    except Exception as e:
        ML = CustommException(e,sys)
        logging.info(ML.error_message)
        logging.info("we are testing our logging file")
        return " welcome to ml modular coding"

if __name__ == "__main__":
    app.run(debug=True) #5000
