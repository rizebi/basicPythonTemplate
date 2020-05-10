import os # for basics
import sys # for basics
import logging # for logging
import datetime # for logging and parsing dates
import traceback # for error handling


##### Functions #####

# Logging function
def getLogger():
  baseDir = os.getcwd()
  # Create logs folder if not exists
  if not os.path.isdir(os.path.join(baseDir, "logs")):
    try:
      os.mkdir(os.path.join(baseDir, "logs"))
    except OSError:
      print("Creation of the logs directory failed")
    else:
      print("Successfully created the logs directory")

  now = datetime.datetime.now()
  log_name = "" + str(now.year) + "." + '{:02d}'.format(now.month) + "." + '{:02d}'.format(now.day) + "-main.log"
  log_name = os.path.join(baseDir, "logs", log_name)
  logging.basicConfig(format='%(asctime)s  %(message)s', level=logging.NOTSET,
                      handlers=[
                      logging.FileHandler(log_name),
                      logging.StreamHandler()
                      ])
  log = logging.getLogger()
  return log

# Main function that does all the flow from 2 input excels, to 4 output excels
def mainFunction(param1):
  # Initialize the logger
  log = getLogger()

  log.info("############################################# New run for param1: " + param1)

  try:
    # Here is the actual logic of the script
	  pass

  ##### END #####
  except KeyboardInterrupt:
    log.info("Quit")
    sys.exit(0)
  except Exception as e:
    log.info("FATAL ERROR: {}".format(e))
    tracebackError = traceback.format_exc()
    log.info(tracebackError)
    sys.exit(99)


##### BODY #####
if __name__ == "__main__":

  if len(sys.argv) != 2:
    log = getLogger()
    log.info("Wrong number of parameters. Use: python pythonTemplate.py <param1>")
    sys.exit(100)
  else:
    param1 = sys.argv[1]
    mainFunction(param1)
