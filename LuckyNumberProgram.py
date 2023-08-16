
##################################
#         Rute Pardal            #
#       New Lucky Number         #
##################################

#Program

import LuckyNumberFunctions as funcs

username = input("Insert your name: ")
oldNrUser = input("Insert your actual Lucky Number: ")
oldNr = funcs.check_oldNr(oldNrUser)

print(funcs.buildMessage(funcs.create_newNr(oldNr), username))


