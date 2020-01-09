import os.path
name = "Jtonna"
currentRoom= "\"glossary\": {\"title\": \"example glossary\", \"ergergf\": {\"wefwef\":\"efwef\"}},"

# f = open(f"{name}s_room_map.json", "a+")
# f.write("What do i write here")
# f.close()

# If the file does not exist
    # Create the file
    # write { some json inside brackets }


if os.path.isfile(f"{name}s_room_log.json"):
        print(f"file exists")
else:
  # Create the file and add JSON brackets
  f = open(f"{name}s_room_log.json", "w+")
  f.write("{")
  f.write(f"\n{currentRoom}\n")  
  f.write("}")
  f.close()