

##################################
#         Rute Pardal            #
#   New Lucky Number Exercise    #
##################################

#Functions


from math import sqrt


def create_newNr (oldNr):
    """
    oldNr: Old Lucky Number
    makes math calculation to create new lucky Number
    --------
    Returns: the new Lucky Number
    """
    newNr = int(oldNr-sqrt(oldNr)+oldNr/2)
    return (newNr)

def buildMessage (newNr, username):
    """   
    newNr : new lucky number.
    username : name given by user
    ----------
    Returns
    message : message to inform the user of the new lucky number

    """
    message = f"{username}, your new Lucky Number is {newNr}!"
    return (message)


def check_oldNr (oldNrUser):
    """
    oldNrUser : old Lucky Number given by user
    ---------
    Returns
    oldNr : corrected Lucky Number
    """
    try:
        oldNr = int(oldNrUser)
        return oldNr
    except ValueError:
        oldNrattempt = input("Not a number! Type your current Lucky Number please: ")
        return check_oldNr(oldNrattempt)
        
