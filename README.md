
# ReVanced Builder

A Python script that Builds ReVanced.apk quickly and using latest version tools!

**(Youtube APK NOT included)**

Youtube is the property of Google Inc.

Revanced is the property of [ReVanced](https://revanced.app/).

I am not affliated with any of above.

This project is just automation for an already existing process.

## Requirements

[Python](https://www.python.org/downloads/)

[Zulu JDK](https://www.azul.com/downloads/?package=jdk#download-openjdk) (Tested with Zulu JDK 17)

Latest Youtube APK (You'll have to get it on your own)

If you want to login using Google, you'll need [MicroG](https://github.com/TeamVanced/VancedMicroG/releases/latest)
installed on your device

## Usage

- Download the repo:
```
git clone https://github.com/lorenzo3421/ReVanced-Builder
cd ReVanced-Builder
pip install -r requirements.txt
```
- Run it in a Terminal (Can't be easier than this)
```
builder.py
```
If you'd like to exclude patches from [ReVanced Patches](https://github.com/revanced/revanced-patches/tree/main/src/main/kotlin/app/revanced/patches),
open one of the patch files (.kt) and find the `@Name`,
then add it to a file called `exclude_patches.lorf` and
place the file in the same directory as the script.

#### Example:

`exclude_patches.lorf`
```
hide-shorts-button
hide-cast-button
```

## Contributing

Contributions are always welcome!

Please adhere to this project's
[Code of Conduct](https://github.com/lorenzo3421/revanced-builder/blob/main/.github/CODE_OF_CONDUCT.md).

## License

[MIT](https://choosealicense.com/licenses/mit/)

