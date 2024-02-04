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
    }
  ]
}
'''

# Parse the JSON data
parsed_data = json.loads(json_data)


def print_dict_and_list_recursive(data, indent=0):
  if isinstance(data, dict):
    for key, value in data.items():
      print('  ' * indent + f'{key}:')
      print_dict_and_list_recursive(value, indent + 2)
  elif isinstance(data, list):
    for index, item in enumerate(data):
      print('  ' * indent + f'[{index}]:')
      print_dict_and_list_recursive(item, indent + 2)
  else:
    print('  ' * indent + f'{data}')


print_dict_and_list_recursive(parsed_data)
