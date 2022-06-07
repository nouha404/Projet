import json
from textwrap import indent

with open('data.json', 'r') as file:
    contenue = json.load(file)
contenue.append("Test")

with open('data.json', 'w') as file:
    json.dump(contenue, file, indent=4)
    
contenue.append("Atal weed")

with open('data.json', 'w') as file:
    json.dump(contenue, file, indent=4)
    
contenue.append(list(range(6)))

with open('data.json', 'w') as file:
    json.dump(contenue, file , indent=4)

    

    
    
  
    
