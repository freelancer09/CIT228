# import message_activity
from message_activity import *
# from message_activity import send_messages
# import message_activity as ma
# from message_activity import send_messages as sendM

messages = ["Be mine","Thinking of you","Sweetheart","You rock","Love me"]
messagesCopy = []
for message in messages:
    messagesCopy.append(message)
send_messages(messages[:])
print("Original list: ",messages)
print("Copied List: ",messagesCopy)
