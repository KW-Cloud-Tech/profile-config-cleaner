#! /usr/bin/env python

import argparse
import json
import sys
from os import path


def parse_args():
    parser = argparse.ArgumentParser(
        description="""Creates a new Conformity profile file from an 
						existing profile, and removes unconfigured rules.""",
    )
    parser.add_argument(
        "user_profile",
        help="path to the user profile json file",
    )
    parser.add_argument(
        "-d",
        "--default_profile",
        default=path.join(
            path.dirname(sys.argv[0]),
            "conformity_default_profile.json",
        ),
        required=False,
        help="path to the default profile json file",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="new_conformity_profile.json",
        required=False,
        help="path to new profile json file",
    )

    return parser.parse_args()


def main():  # sourcery skip: list-comprehension

    args = parse_args()

    with open(args.default_profile) as default_fileobject:
        default_profile = json.load(default_fileobject)

    with open(args.user_profile) as user_fileobject:
        user_profile = json.load(user_fileobject)

    new_rule_settings = []
    for rule in user_profile["ruleSettings"]:
        if rule not in default_profile["ruleSettings"]:
            new_rule_settings.append(rule)

    user_profile["ruleSettings"] = new_rule_settings

    with open(args.output, "w+") as output_fileobject:
        output_fileobject.write(json.dumps(user_profile, indent=2))

    # print(json.dumps(new_rule_settings, sort_keys=True, indent=4))


if __name__ == "__main__":
    main()
