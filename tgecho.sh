#!/bin/sh

message='Message goes here'
apiToken=TokenGoesHere #i.e. 123456789:ABCDEFGLKJASHDFLKJSDHF
userChatId=ChatIDGoesHere #i.e. -123456789

sendTelegram() {
        curl -s \
        -X POST \
        https://api.telegram.org/bot$apiToken/sendMessage \
        -d text="$message" \
        -d chat_id=$userChatId
}

if  [[ -z "$message" ]]; then
        echo "Please pipe a message to me!"
else
        sendTelegram
	clear
fi
