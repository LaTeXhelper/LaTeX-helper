import json

json_data =r'''
{
    "Print to console": {
        "prefix": "log",
        "body": [
            "console.log('$1');",
            "$2"
        ],
        "description": "Log output to console"
    },
    "hello": {
        "prefix": "hello",
        "body": [
            "hello world"
        ],
        "description": "description of hello world."
    },
    "Basic Blocks": {
        "prefix": "bb",
        "body": [
            "\\b"
        ],
        "description": "null"
    }
}
'''

json_dict = json.loads(json_data)
print(json_dict)