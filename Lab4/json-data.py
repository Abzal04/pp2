import json
file=open('sample-data.json','r')
json_data=json.loads(file.read())
print(json_data["imdata"][0]["l1PhysIf"]["attributes"]["mtu"])

print("Interface Status")
print("=" * 80)
print("{:<50}{:<20}{:<8}{:<8}".format("DN","Description","Speed","MTU"))
print("-" * 80)

for item in json_data:
    dn = item.get('DN', '')
    description = item.get('Description', '')
    speed = item.get('Speed', 'inherit')
    mtu = item.get('MTU', '')

    print("{:<50}{:<20}{:<8}{:<8}".format(dn, description, speed, mtu))

