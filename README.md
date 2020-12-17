# profile-config-cleaner
Parses a Conformity profile JSON file and removes any redundant configurations (e.g. default settings). This works by comparing two existing profile files and creating a third file in the same directory that contains only the rule configurations which differ from the default.

## Problem this solves
Conformity marks all the profile-defined rules as 'manually configured' in the profiles UI. By removing the default rules from the file before upload, users hosting the complete Conformity default profile as a kind of rubrick in version control can improve the UX of managing configured profiles.

## Usage via GitHub actions
The workflows yaml file automatically creates a container and initiates github actions. <br />
All that is reqired is a merge commit to the user profile file path in the github repository (edit this file path name in the yaml file as desired). This will initiate an action which will run the script and produce the file, which can then be uploaded via the Conformity UI.

## Usage
Uses Python 3.8: https://www.python.org/downloads/release/python-380/

Run from the command line in linux/mac or windows. Must contain the default file and the user's comparison file in the same directory. <br />

First argument (required): <br />
`<path-to-user-profile>`<br />

Optional arguments:<br />
`-d <path-to-default-profile>` or `--default-profile <path-to-default-profile>` (if not defined, uses the existing 'conformity-default-profile.json') <br />
`-o <path-to-output>` or `--output <path-to-output>` (if not defined, creates 'new-conformity-profile.json' in the same directory)  <br />

### Examples:

Using the standard values and outputs file to local directory: <br />
`$ ./profile-config-cleaner.py input-profile.json` 

Passing in custom files and names: <br />
`$ ./profile-config-cleaner.py input-profile.json -d default-profile.json -o new-clean-profile.json` or <br /> 
`$ ./profile-config-cleaner.py input-profile.json -default-profile default-profile.json`
