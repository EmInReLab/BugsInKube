import json
import os

if __name__ == "__main__":
    patch = os.path.join(".", "bugs", "bug-1", "patch.json")
    # kubectl_delete(patch)
    with open(patch, "r") as file:
        patchData = json.load(file)
    print(patchData["metadata"]["name"])
