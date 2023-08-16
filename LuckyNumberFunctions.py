

##################################
#         Rute Pardal            #
#   New Lucky Number Exercise    #
##################################

#Functions


from math import sqrt


def create_newNr (oldNr):
    """oldNr: Old Lucky Number
    makes math calculation to create new lucky number
    returns the new number
    """
    newNr = int(oldNr-sqrt(oldNr)+oldNr/2)
    return (newNr)

def buildMessage (newNr, username):
    """   
    Parameters
    ----------
    newNr : new lucky number.
    username : name given by user

    Returns
    -------
    message : message to politely inform the user of the new lucky number

    """
    message = f"{username}, your new Lucky Number is {newNr}!"
    return (message)


def check_oldNr (oldNrUser):
    """
    Parameters
    ----------
    oldNr : old Lucky Number given by user
    Returns
    -------
    oldNr : corrected Lucky Number

    """
    try:
       oldNr = int(oldNrUser) 
    except ValueError:
        oldNr = int(input("Not a number! Type your actual Lucky Number please: "))
    return oldNr