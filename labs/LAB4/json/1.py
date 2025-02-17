import json
with open("/Users/serik-dias/Downloads/KBTU/PP2/PYTHON/4 lab/json/sample-data.json", "r") as f:
    data = json.load(f)
print("Inherit status")
print("="*84)
DN="DN"
Description="Description"
Speed="Speed"
MTU="MTU"
print(f"{DN:50} {Description:20} {Speed:7} {MTU:10}") 
print("-"*84)
for item in data["imdata"]:  #imdata is key which contain list of elements
    attr = item["l1PhysIf"]["attributes"]  #attr == attributes     attributes is dictionary
    dn = attr.get("dn")
    
    descr = attr.get("descr")
    speed = attr.get("speed")
    mtu = attr.get("mtu")
    print(f"{dn:50} {descr:20} {speed:7} {mtu:10}")  