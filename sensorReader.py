from homematicip import home

# TODO: Websocket Connection Reader

# if needed you can close the websocket connection with
home.disable_events()
# add a function to handle new events
home.onEvent += print_events
# enable the event connection -> this will also start the websocket connection to the homeMaticIP Cloud
home.enable_events()


# example function to display incoming events
def print_events(eventList):
    for event in eventList:
        print
        f"EventType: {event['eventType']} Data: {event['data']}"
