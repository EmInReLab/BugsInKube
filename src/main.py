import tkinter as tk
import time
import os
import tkinter.messagebox
import subprocess
import json


def find_subdirectory_by_number(parent_directory, number):
    for subdir in os.listdir(parent_directory):
        if subdir.startswith("bug-") and subdir.split("-")[1] == str(number):
            return os.path.join(parent_directory, subdir)
    return None

def kubectl_apply(manifest_path: str) -> bool:
    command = ["kubectl", "apply", "-f", manifest_path]
    try:
        result = subprocess.run(command, check=True)
        print("Resource deployed successfully.")
        print("Subprocess output:")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as err:
        print(f"Error deploying resource: {err}")
        return False

def kubectl_delete(patchJson:dict, namespace=None)->bool:
    resource_type = patchJson['kind']
    resource_name = patchJson['metadata']['name']

    command = ["kubectl", "delete", resource_type, resource_name]
    if namespace:
        command.extend(["--namespace", namespace])
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print("Resource deleted successfully.")
        print("Subprocess output:")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as err:
        print(f"Error deleting resource: {err}")
        print("Subprocess error output:")
        print(err.stderr)
        return False

def deploy_kubernetes_resource(manifest: str, text_widget: tk.Text, new_window: tk.Toplevel) -> bool:
    if (kubectl_apply(manifest)):
        text_widget.insert(tk.END, "Resource deployed Successfully\n")
        new_window.update()
        time.sleep(1)
        text_widget.insert(tk.END, "Will patch the resource to reproduce the error in 10 seconds.\n")
        new_window.update()
        time.sleep(10)
        return True
    else:
        text_widget.insert(tk.END, "Resource deployment failed\nPlease Check all the requirements.\n")
        new_window.update()
        time.sleep(1)
        return False
    
def deploy_kubernetes_patch(patch: str, text_widget: tk.Text, new_window: tk.Toplevel) -> bool:
    if (kubectl_apply(patch)):
        text_widget.insert(tk.END, "Buggy Patch Created!\nYou can view you resource via kubectl\n")
        new_window.update()
        time.sleep(3)
        toDelete = tkinter.messagebox.askyesno("Delete Resource", "You want to delete the resource?")
        if (toDelete):
            with open(patch, "r") as file:
                patchJson = json.load(file)
            counter = 20
            while ((not (kubectl_delete(patchJson))) and counter>0):
                counter-=1
            if counter == 0:
                text_widget.insert(tk.END, "Error Deleting the resource\nDelete the resource manually using kubectl\n")
                new_window.update()
                time.sleep(1)
                return False
            return True
        else:
            text_widget.insert(tk.END, "Delete the resource manually when necessary\n")
            new_window.update()
            time.sleep(1)
            return True
    else:
        text_widget.insert(tk.END, "Patch deployment failed\nPlease Check all the requirements.\n")
        new_window.update()
        time.sleep(1)
        return False


def handleSubmit(
    text_widget: tk.Text,
    new_window: tk.Toplevel,
    platform: str,
    bugId: int,
    toReproduce: bool = False,
):
    subdirectory = find_subdirectory_by_number("./bugs", bugId)
    if subdirectory:
        text_widget.insert(
            tk.END, "====================BUG Definition====================\n"
        )
        definition = os.path.join(subdirectory, "definition.json")
        manifest = os.path.join(subdirectory, "manifest.json")
        patch = os.path.join(subdirectory, "patch.json")

        with open(definition, "r") as file:
            definitionData = json.load(file)
        with open(manifest, "r") as file:
            manifestData = json.load(file)
        with open(patch, "r") as file:
            patchData = json.load(file)

        text_widget.insert(tk.END, f'Bug ID\t\t\t\t\t: {definitionData["id"]}\n')
        text_widget.insert(
            tk.END, f'Bug reported Platform\t\t\t\t\t: {definitionData["platform"]}\n'
        )
        text_widget.insert(
            tk.END,
            f'Affected Version\t\t\t\t\t: {definitionData["affected-version"]}\n',
        )
        text_widget.insert(
            tk.END,
            f'Affected Component Categorization\t\t\t\t\t: {definitionData["affected-categorization"]}\n',
        )
        text_widget.insert(
            tk.END, f'Severity\t\t\t\t\t: {definitionData["severity"]}\n'
        )
        text_widget.insert(
            tk.END, "======================================================\n"
        )
        new_window.update()
        time.sleep(1)
        if definitionData["resolved"] == "open":
            text_widget.insert(
                tk.END, "Full patch of the bug has not been produced yet\n"
            )
        else:
            text_widget.insert(tk.END, "Full patch of the bug has been produced\n")
        text_widget.insert(
            tk.END,
            f'Follow the link for more information about the bug status: {definitionData["link"]}\n',
        )
        new_window.update()
        time.sleep(1)
        text_widget.insert(
            tk.END, "======================================================\n"
        )
        text_widget.insert(tk.END, "Detailed Description About the Bug\n")
        text_widget.insert(
            tk.END, "======================================================\n"
        )
        text_widget.insert(tk.END, definitionData["description"])
        text_widget.insert(tk.END, "\n")
        new_window.update()
        time.sleep(1)
        text_widget.insert(
            tk.END, "======================================================\n"
        )
        text_widget.insert(tk.END, "Expected behaviour: ")
        text_widget.insert(tk.END, definitionData["expected-behaviour"])
        text_widget.insert(tk.END, "\n")
        new_window.update()
        time.sleep(1)

        if toReproduce:
            toReproduce = tkinter.messagebox.askyesno("Reproduce Bug", "Do you have the required version installed to reproduce the bug?") and toReproduce

        text_widget.insert(
            tk.END, "======================================================\n"
        )
        text_widget.insert(tk.END, "Manual bug reproduction step\n")
        new_window.update()
        time.sleep(1)
        text_widget.insert(
            tk.END, "======================================================\n"
        )
        if toReproduce:
            text_widget.insert(tk.END, "Using the below manifest to create Kubernetes Resource")
        else:
            text_widget.insert(tk.END, "Use the below manifest to create Kubernetes Resource:\n")
        new_window.update()
        time.sleep(1)
        pretty_json = json.dumps(manifestData, indent=4)
        text_widget.insert(tk.END, pretty_json)
        text_widget.insert(tk.END, "\n")
        new_window.update()
        time.sleep(1)
        text_widget.insert(
            tk.END, "======================================================\n"
        )

        is_deployed = False
        if toReproduce:
            is_deployed = deploy_kubernetes_resource(manifest, text_widget, new_window)
        
        if is_deployed:
            text_widget.insert(tk.END, "Modifying the manifest as below\n")
        else:
            text_widget.insert(tk.END, "Modify the manifest as below\n")
        text_widget.insert(
            tk.END, "======================================================\n"
        )
        new_window.update()
        time.sleep(1)
        pretty_json = json.dumps(patchData, indent=4)
        text_widget.insert(tk.END, pretty_json)
        text_widget.insert(tk.END, "\n")
        new_window.update()
        time.sleep(1)
        
        if is_deployed:
            deploy_kubernetes_patch(patch, text_widget, new_window)

    else:
        text_widget.insert(tk.END, f"No subdirectory found for bug-{bugId}\n")
        new_window.update()
        time.sleep(2)

def printDefinitionK8s(definition: dict, manifest: dict, patch: dict) -> None:
    print("====================BUG Definition====================")
    print(f'Bug ID\t\t\t\t\t: {definition["id"]}')
    print(f'Bug reported Platform\t\t\t: {definition["platform"]}')
    print(f'Affected Version\t\t\t: {definition["affected-version"]}')
    print(
        f'Affected Component Categorization\t: {definition["affected-categorization"]}'
    )
    print(f'Severity\t\t\t\t: {definition["severity"]}')
    print("======================================================")
    if definition["resolved"] == "open":
        print("Full patch of the bug has not been produced yet")
    else:
        print("Full patch of the bug has been produced")
    print(
        f'Follow the link for more information about the bug status: {definition["link"]}'
    )
    print("======================================================")
    print("Detailed Description About the Bug")
    print("======================================================")
    print(definition["description"])
    print("======================================================")
    print("Expected behaviour:", end=" ")
    print(definition["expected-behaviour"])
    print("======================================================")
    print("Manual bug reproduction step")
    print("======================================================")
    print("Use the below manifest to create Kubernetes Resource:")
    pretty_json = json.dumps(manifest, indent=4)
    print(pretty_json)
    print("======================================================")
    print("Modify the manifest as below")
    print("======================================================")
    pretty_json = json.dumps(patch, indent=4)
    print(pretty_json)
