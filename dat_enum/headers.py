from enum import Enum

class Headers(Enum):
    HEADERS_AUTH = {
            'Content-Type': 'application/json',
            'Cookie': 'S-Refresh-Token=eyJhbGciOiJIUzUxMiJ9.eyJmaW5nZXJwcmludCI6IiQyYSQxMCQ2eVhBNnRoSDN5d01LNGc4QThGVHIuWFpLZ0syMU1tT3RjS3BYbGNLVXZ6YkkxMHhncGExVyIsInN1YiI6IkRFTU9XRUIiLCJqdGkiOiIwMmU5ZWNjNy0xNjE4LTRjZGMtYWViMC0yYTJlZjcwZDNmNjUiLCJleHAiOjE3NDYwNTgzODAsImlhdCI6MTc0NjA0Mzk4MH0.7tTZnaPTKggCCWTYWBXHPLnJWqopb7AQpl0FAd6ckopW_Iiv7vitq9ws6I7o_UQSTUnxUJoL7a1PVO4SFrldXQ'
        }


def method_headers(assess_token):
    headers = {
            'Content-Type': 'application/json',
            'Authorization': assess_token
            }
    return headers
