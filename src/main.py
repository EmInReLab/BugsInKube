import tkinter as tk
import time
import os

def find_subdirectory_by_number(parent_directory, number):
    for subdir in os.listdir(parent_directory):
        if subdir.startswith("bug-") and subdir.split("-")[1] == str(number):
            return os.path.join(parent_directory, subdir)
    return None

def handleSubmit(text_widget:tk.Text, new_window:tk.Toplevel, platform:str, bugId:int, toReproduce:bool=False):
    subdirectory = find_subdirectory_by_number("./bugs", bugId)
    if subdirectory:
        text_widget.insert(tk.END, "====================BUG Definition====================\n")
        definition = os.path.join(subdirectory, "definition.json")
        manifest = os.path.join(subdirectory, "manifest.json")
        patch = os.path.join(subdirectory, "patch.json")

        with open(definition, 'r') as file:
            definitionData = json.load(file)
        with open(manifest, 'r') as file:
            manifestData = json.load(file)
        with open(patch, 'r') as file:
            patchData = json.load(file)
        
        text_widget.insert(tk.END, f'Bug ID\t\t\t\t\t: {definitionData["id"]}\n')
        text_widget.insert(tk.END, f'Bug reported Platform\t\t\t\t\t: {definitionData["platform"]}\n')
        text_widget.insert(tk.END, f'Affected Version\t\t\t\t\t: {definitionData["affected-version"]}\n')
        text_widget.insert(tk.END, f'Affected Component Categorization\t\t\t\t\t: {definitionData["affected-categorization"]}\n')
        text_widget.insert(tk.END, f'Severity\t\t\t\t\t: {definitionData["severity"]}\n')
        text_widget.insert(tk.END, "======================================================\n")
        new_window.update()
        new_window.update()
        time.sleep(1)
        if (definitionData["resolved"] == "open"):
            text_widget.insert(tk.END, "Full patch of the bug has not been produced yet\n")
        else:
            text_widget.insert(tk.END, "Full patch of the bug has been produced\n")
        text_widget.insert(tk.END, f'Follow the link for more information about the bug status: {definitionData["link"]}\n')
        new_window.update()
        time.sleep(1)
        text_widget.insert(tk.END, "======================================================\n")
        text_widget.insert(tk.END, "Detailed Description About the Bug\n")
        text_widget.insert(tk.END, "======================================================\n")
        text_widget.insert(tk.END, definitionData["description"])
        text_widget.insert(tk.END, "\n")
        new_window.update()
        time.sleep(1)
        text_widget.insert(tk.END, "======================================================\n")
        text_widget.insert(tk.END, "Expected behaviour: ")
        text_widget.insert(tk.END, definitionData["expected-behaviour"])
        text_widget.insert(tk.END, "\n")
        new_window.update()
        time.sleep(1)
        text_widget.insert(tk.END, "======================================================\n")
        text_widget.insert(tk.END, "Manual bug reproduction step\n")
        new_window.update()
        time.sleep(1)
        text_widget.insert(tk.END, "======================================================\n")
        text_widget.insert(tk.END, "Use the below manifest to create Kubernetes Resource:\n")
        new_window.update()
        time.sleep(1)
        pretty_json = json.dumps(manifestData, indent=4)
        text_widget.insert(tk.END, pretty_json)
        text_widget.insert(tk.END, "\n")
        new_window.update()
        time.sleep(1)
        text_widget.insert(tk.END, "======================================================\n")
        text_widget.insert(tk.END, "Modify the manifest as below\n")
        text_widget.insert(tk.END, "======================================================\n")
        new_window.update()
        time.sleep(1)
        pretty_json = json.dumps(patchData, indent=4)
        text_widget.insert(tk.END, pretty_json)
        text_widget.insert(tk.END, "\n")
    else:
        print(f"No subdirectory found for bug-{bugId}")
    # for i in range(10):
    #     text_widget.insert(tk.END, f"Statement {i}\n")
    #     new_window.update()  # Update the window to show the new text
    #     time.sleep(1)  # Sleep for 1 second between adding each line

import json

def printDefinitionK8s(definition:dict, manifest:dict, patch:dict)->None:
    print("====================BUG Definition====================")
    print(f'Bug ID\t\t\t\t\t: {definition["id"]}')
    print(f'Bug reported Platform\t\t\t: {definition["platform"]}')
    print(f'Affected Version\t\t\t: {definition["affected-version"]}')
    print(f'Affected Component Categorization\t: {definition["affected-categorization"]}')
    print(f'Severity\t\t\t\t: {definition["severity"]}')
    print("======================================================")
    if (definition["resolved"] == "open"):
        print("Full patch of the bug has not been produced yet")
    else:
        print("Full patch of the bug has been produced")
    print(f'Follow the link for more information about the bug status: {definition["link"]}')
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