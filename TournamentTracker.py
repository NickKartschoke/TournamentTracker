#Prints main menu and returns selection
from json.tool import main
import csv


def mainMenu():
    print("\nParticipant Menu")
    print("================")
    selection = input("1. Sign Up\n2. Cancel Sign Up\n3. View Participants\n4. Save Changes\n5. Exit\n")
    return selection

#Prints welcome statement
def welcome():
    print("Welcome to Tournaments R Us")
    print("============================")
    participants = input("Enter the number of participants: ")

    print(f'There are {participants} participant slots ready for sign-ups.')
    return participants

def createDict(p):
    dict = {}
    for i in range(int(p)):
        dict[str(i+1)] = None
    return dict

participants = welcome()
slots = createDict(participants)

#Participant signup
def signUp(p):
    print("\nParticipant Sign Up\n====================")
    participantName = input("Participant Name: ")
    slotNum = input(f"Desired Starting Slot #[1-{p}]: ")
    while(slotNum not in slots.keys() or slots[slotNum] != None):
        print(f"Error:\nSlot #{slotNum} is filled. Please try again.\n")
        slotNum = input(f"Desired Starting Slot #[1-{p}]: ")
    slots.update({slotNum:participantName})
    print(f"Success:\n{participantName} is signed up in starting slot #{slotNum}.")

def cancel(p):
    print("\nParticipant Cancellation\n========================")
    slotNum = input(f"Starting Slot #[1-{p}]: ")
    participantName = input("Participant Name: ")
    while(slots[slotNum] != participantName):
        print(f"Error:\n{participantName} is not in that stating slot.")
        slotNum = input(f"Starting Slot #[1-{p}]: ")
        participantName = input("Participant Name: ")
    slots.update({slotNum:None})
    print(f"Success:\n{participantName} has been cancelled from starting slot #{slotNum}.")  

def viewParticipants(p):
    print("\nView Participants\n=================")
    slotNum = input(f"Starting slot #[1-{p}]: ")
    print("\nStarting Slot: Participant")
    start = int(slotNum) - 5
    end = int(slotNum) + 5
    if start <= 0:
        start = 1
    if end > int(p):
        end = int(p)
    for i in range(start, end+1):
        if slots[str(i)] != None:
            print(i, ": ", slots[str(i)])
        else: print(f"{i}: [empty]")

def saveChanges(p):
    print("\nSave Changes\n============")
    saveQuestion = input("Save your changes to a txt file? [y/n]: ")
    if saveQuestion == 'y':
        filename = "TournamentSelectionSheet.txt"
        f = open(filename,'w')
        for i in range(1,int(p)+1):
            if slots[str(i)] != None:
                f.write(f"{i}: {slots[str(i)]}\n")
            else: f.write(f"{i}: [empty]\n")
        f.close()

def quitFunction():
    print("\nExit\n=====\nAny unsaved changes will be lost.")
    confirmation = input("Are you sure you want to exit? [y/n]: ")
    if confirmation == 'y':
        return False
    else: return True

continueLoop = True
while continueLoop:
    mainSelection = mainMenu()
    if mainSelection == '1':
        signUp(participants)
    elif mainSelection == '2':
        cancel(participants)
    elif mainSelection == '3':
        viewParticipants(participants)
    elif mainSelection == '4':
        saveChanges(participants)
    elif mainSelection == '5':
        continueLoop = quitFunction()
print ("\nGoodbye!")