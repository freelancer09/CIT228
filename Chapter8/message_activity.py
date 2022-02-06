def show_messages(messageList):
    for message in messageList:
        print(message)

def send_messages(messageList):
    sent_messages = []
    while messageList:
        message = messageList.pop()
        print(message)
        sent_messages.append(message)
    print("Sent list: ",messageList)
    print("New List: ",sent_messages)