from .tag import Tag
from .loraName import LoraName

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "tag": Tag,
    "loraName": LoraName
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "tag": "Extract Tag from list",
    "loraName": "Extract Lora Name"
}