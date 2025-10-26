#Case 1
# import logging
# logging.warning("This is a warning message")
# logging.error("This is a error message")
# logging.critical("This is a critical message")
# logging.debug("This is a debug message")
# logging.info("This is a info message")

#Case 2
# import logging
# logging.basicConfig(filename='example.log',level=logging.INFO)
# logging.warning("This is a warning message")
# logging.error("This is a error message")
# logging.critical("This is a critical message")
# logging.debug("This is a debug message")
# logging.info("This is a info message")

# #Case 4
# import logging
# import datetime
# logging.basicConfig(filename='example.log',level=logging.DEBUG,filemode='w')
#
# logging.debug(datetime.datetime.now())
# logging.info("This is a info message")
# logging.warning("This is a warning message")
# logging.error("This is a error message")
# logging.critical("This is a critical message")

# #case 4
# import logging
# import datetime
# logging.basicConfig(filename='basic.log',filemode='w',level=logging.DEBUG,
#         encoding='UTF-8',format='%(process)d-%(levelname)s-%(message)s')
# logging.debug(datetime.datetime.now())
# logging.info("This is a info message")
# logging.warning("This is a warning message")
# logging.error("This is a error message")
# logging.critical("This is a critical message")

#case 4
import logging
logging.basicConfig(filename='xyz.log',filemode='w',
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.CRITICAL,
                    datefmt='%d/%m/%Y - %I:%M:%S')
logging.critical("This is a critical")