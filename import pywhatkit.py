import pywhatkit as kit
import datetime

# Replace these with your group name and the message you want to send
group_name = "9th batch 2023-2024"
message = "hello,this is a test message"
time_hour=20
time_minute=55

# Send the message to the group
kit.sendwhatmsg_to_group(group_name, message, time_hour, time_minute)
                        