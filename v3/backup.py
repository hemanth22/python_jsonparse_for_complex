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

# Access specific values
status = parsed_data["status"]
timestamp = parsed_data["timestamp"]
data = parsed_data["data"][0]
id_value = data["id"]
status_value = data["status"]
someone = data["Someone"]
somehow = data["Somehow"]
pair = data["Pair"]
nothing = data["nothing"]
lrsf = data["lrsf"]
something = data["something"][0]
hey_value = something["hey"]
hope_value = something["hope"]
good_value = something["good"]
do_value = data["do"]
hey_list = data["hey"]

# Print the values
print("Status:", status)
print("Timestamp:", timestamp)
print("ID:", id_value)
print("Status:", status_value)
print("Someone:", someone)
print("Somehow:", somehow)
print("Pair:", pair)
print("Nothing:", nothing)
print("Lrsf:", lrsf)
print("Hey:", hey_value)
print("Hope:", hope_value)
print("Good:", good_value)
print("Do:", do_value)
print("Hey List:", hey_list)
