if CC.error:
    return "You got an error: " + str(CC.error)

if CC.printed("Can you expand on that answer?"):
    return True
else:
    return "I didn't see the new response to the patient's 'no' answer"
