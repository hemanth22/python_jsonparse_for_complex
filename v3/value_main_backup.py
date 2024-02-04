import json

# Assuming the JSON data is stored in a variable called 'json_data'
json_data = '''
{
  "status": "OK",
  "timestamp": 1342342,
  "data": [
    {
      "id": 1,
      "status": "ACTIVE",
      "Someone": "SOMEDATE",
      "Somehow": 0.128,
      "Pair": "kivy,lemon",
      "nothing": "*",
      "lrsf": "",
      "something": [
        {
          "hey": "hi",
          "hope": "doing",
          "good": "nooo"
        }
      ],
      "do": "done",
      "hey": [
        "nohey",
        "hey",
        "heyheyhye"
      ]
    },
    {
      "id": 2,
      "status": "ACTIVE",
      "Someone": "SOMEDATE",
      "Somehow": 0.128,
      "Pair": "kivy,lemon",
      "nothing": "*",
      "lrsf": "",
      "something": [
        {
          "hey": "hi",
          "hope": "doing",
          "good": "nooo"
        }
      ],
      "do": "done",
      "hey": [
        "nohey",
        "hey",
        "heyheyhye"
      ]
    }
  ]
}
'''

# Parse the JSON data
parsed_data = json.loads(json_data)


def print_values_recursive(data):
  if isinstance(data, dict):
    for value in data.values():
      print_values_recursive(value)
  elif isinstance(data, list):
    for item in data:
      print_values_recursive(item)
  else:
    print(f'{data},', end=' ')


print_values_recursive(parsed_data)
