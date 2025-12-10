# Convert dictionary to JSON string.
import json

# Example dictionary
data = {
    "name": "Hiral",
    "rno": 1,
    "city": "jnd"
}

# Convert dictionary to JSON string
json_str = json.dumps(data)
print(json_str)


