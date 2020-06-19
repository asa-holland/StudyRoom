from urllib import request, parse
import json


# Code taken from https://www.accadius.com/send-message-slack-python-program/
# Comments added for clarity

# Posting to a Slack channel
def send_message_to_slack(text, channel_to_message):
    """
    Takes a string of text and an HTTP address of a Slack channel, and sends the message to that channel as the Slack App
    :param text: String of text wanted to send
    :param channel_to_message: HTTP address of the slack channel you want to message
    :return: returns True if the message was sent appropriately, or False if not.
    """

    # Creates a key value pair the key "text" and the provided text
    post = {"text": "{0}".format(text)}

    # Encode the provided text from ascii (default string) into JSON format, which is how the HTTP post is processed
    # Then make a HTTP request using the slack channel provided, sending the text.
    # If this is successful, return True.
    try:
        json_data = json.dumps(post)
        req = request.Request(channel_to_message,
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'})
        resp = request.urlopen(req)
        return True

    # If the HTTP request is not successful, print out the error code and return False.
    except Exception as em:
        print("EXCEPTION: " + str(em))
        return False

send_message_to_slack('Hello GAPP', "https://hooks.slack.com/services/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")
