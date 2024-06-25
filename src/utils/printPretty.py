import json


def printDefinitionK8s(definition: dict, manifest: dict, patch: dict) -> None:
    print("====================BUG Definition====================")
    print(f'Bug ID\t\t\t\t\t: {definition["id"]}')
    print(f'Bug reported Platform\t\t\t: {definition["platform"]}')
    print(f'Affected Version\t\t\t: {definition["affected-version"]}')
    print(
        f'Affected Component Categorization\t: {definition["affected-categorization"]}'  # noqa E501
    )
    print(f'Severity\t\t\t\t: {definition["severity"]}')
    print("======================================================")
    if definition["resolved"] == "open":
        print("Full patch of the bug has not been produced yet")
    else:
        print("Full patch of the bug has been produced")
    print(
        f'Follow the link for more information about the bug status: {definition["link"]}'  # noqa E501
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
