# =-----------------------------= #
# ReVanced Builder by Lorenzo3421 #
# =-----------------------------= #

# Youtube is the property of Google Inc.
# Revanced is the property of ReVanced (https://revanced.app/).
# I am not affliated with any of above.
# This project is just automation for an already existing process.

import os
import requests
from clint.textui import progress


# Get all tools needed from ReVanced's github repos
def get_revanced_tools(tool_name, repo_filename, output=None):
    # Get HTML from latest version of tool
    r = requests.get(f"https://github.com/revanced/{tool_name}/releases/latest")

    # Get Version from HTML
    version = r.text.split(f"/revanced/{tool_name}/releases/download/")[1].split("/")[0]
    # Remove the "v" from the version
    version = version[1:]

    # Download the tool
    if output is None:
        output = tool_name + ".jar"
    output = output.replace("{repo_filename}", repo_filename)
    print(f"{output}:")

    # Code from https://stackoverflow.com/a/20943461/10117351 #
    r = requests.get(
        f"https://github.com/revanced/{tool_name}/releases/download/v{version}/{repo_filename}".replace(
            "{version}", version
        ),
        stream=True,
    )
    with open(output, "wb") as f:
        total_length = int(r.headers.get("content-length"))
        for chunk in progress.bar(
            r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1
        ):
            if chunk:
                f.write(chunk)
                f.flush()
    # ------------------------------------------------------- #


# Get the Zulu JDK 17 path
def get_jdk():
    if os.path.isfile("java_path.lorf"):
        with open("java_path.lorf", "r") as f:
            return f.read()
    else:
        print("Please drag in this terminal the Zulu JDK 17 java.exe file")
        print("(java.exe can be found in the bin folder)")
        print("After dragging in the file, press enter.")
        path = input("JDK Path: ")
        with open("java_path.lorf", "w") as f:
            f.write(path)
        return path


# Prepare to build
def prepare_build():
    # JDK
    global java_path
    java_path = get_jdk()

    # ReVanced Tools
    get_revanced_tools("revanced-patches", "revanced-patches-{version}.jar")
    get_revanced_tools(
        "revanced-cli", "revanced-cli-{version}-all.jar", "revanced-cli-all.jar"
    )
    get_revanced_tools(
        "revanced-integrations", "app-release-unsigned.apk", "{repo_filename}"
    )

    # Youtube APK
    print(
        "\nEnsure you have the latest version of Youtube APK "
        + "(or Youtube Music APK) exactly at this path:"
    )
    print(os.getcwd() + "\\youtube.apk")

    input("Press enter to build ReVanced.")
    build_revanced()


# Build ReVanced.apk
def build_revanced():
    print("Building ReVanced.apk...")

    if os.path.isfile("exclude_patches.lorf"):
        with open("exclude_patches.lorf", "r") as f:
            lines = f.read().splitlines()
            exclude_patches = " ".join(["-e " + line for line in lines])

    os.system(
        f"{java_path} -jar revanced-cli-all.jar -a youtube.apk -c -o ReVanced.apk -b revanced-patches.jar"
        + "-m app-release-unsigned.apk {exclude_patches}"
    )

    print("Done.")


if __name__ == "__main__":
    prepare_build()