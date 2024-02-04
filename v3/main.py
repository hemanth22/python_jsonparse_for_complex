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


def print_selected_values(data):
  if isinstance(data, dict):
    id_value = data.get('id', '')
    status_value = data.get('status', '')
    pair_value = data.get('Pair', '')
    print('id', 'status', 'pairs')
    print(f'{id_value},{status_value},{pair_value}')
  elif isinstance(data, list):
    for item in data:
      print_selected_values(item)


# Loop through each item in the 'data' list and print selected values
for item in parsed_data['data']:
  print_selected_values(item)
