#####################################################
#### Written By: SATYAKI DE                      ####
#### Written On: 22-Jul-2022                     ####
#### Modified On 30-Aug-2022                     ####
####                                             ####
#### Objective: This is the main calling         ####
#### python script that will invoke the          ####
#### clsReadForm class to initiate               ####
#### the reading capability in real-time         ####
#### & display text from a formatted forms.      ####
#####################################################

# We keep the setup code in a different class as shown below.
from ReadingFilledForm import clsReadForm as rf

from clsConfigClient import clsConfigClient as cf

import datetime
import logging

###############################################
###           Global Section                ###
###############################################
# Instantiating all the main class
scannedImagePath = str(cf.conf['IMAGE_PATH']) + str(cf.conf['FILE_NAME'])
templatePath = str(cf.conf['TEMPLATE_PATH']) + str(cf.conf['TEMPLATE_FILE_NAME'])

x1 = rf.clsReadForm(scannedImagePath, templatePath)

###############################################
###    End of Global Section                ###
###############################################

def main():
    try:
        # Other useful variables
        debugInd = 'Y'
        var = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        var1 = datetime.datetime.now()

        print('Start Time: ', str(var))
        # End of useful variables

        # Initiating Log Class
        general_log_path = str(cf.conf['LOG_PATH'])

        # Enabling Logging Info
        logging.basicConfig(filename=general_log_path + 'readingForm.log', level=logging.INFO)

        print('Started extracting text from formatted forms!')

        # Getting the dictionary
        my_dict = cf.conf['MY_DICT']

        # Execute all the pass
        r1 = x1.startProcess(debugInd, var, my_dict)

        if (r1 == 0):
            print('Successfully extracted text from the formatted forms!')
        else:
            print('Failed to extract the text from the formatted forms!')

        var2 = datetime.datetime.now()

        c = var2 - var1
        minutes = c.total_seconds() / 60
        print('Total difference in minutes: ', str(minutes))

        print('End Time: ', str(var1))

    except Exception as e:
        x = str(e)
        print('Error: ', x)

if __name__ == "__main__":
    main()
