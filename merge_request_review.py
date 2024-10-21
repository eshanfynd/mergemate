import sys
import os
import json
import requests

project_id = sys.argv[1]
merge_request_id = sys.argv[2]
print(f"Generating reviews for merge request id : {merge_request_id}")


def http_post_request():
    url = 'https://dbe7-122-171-17-199.ngrok-free.app/v1.0/execute'
    {
    "data":  {"messages": [{"role": "user", "content": f"Who is the current president of India?-{str(sys.argv)}"}]},
    "agent": {
        "slug": "ConversationalFexAgent"
    },

}
    response = requests.post(url, data=json.dumps(data))

    if response.status_code == 200:
        print('POST request was successful!')
        print('Response content:')
        print(response.json())
        return True
    else:
        print(f'POST request failed with status code {response.status_code}')
        print(response.text)
        return False


http_post_request()
