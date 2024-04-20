from src.Bugs import Bug
from src.KubernetesBugs import KubernetesBug
from src.main import kubectl_delete
import os, json

if __name__ == "__main__":
    patch = os.path.join(".", "bugs", "bug-1", "patch.json")
    # kubectl_delete(patch)
    with open(patch, "r") as file:
        patchData = json.load(file)
    print(patchData['metadata']['name'])