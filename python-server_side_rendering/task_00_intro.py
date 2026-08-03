#!/usr/bin/python3
"""Generates personalized invitation files from a template and a list of
attendee dictionaries."""
import os


def generate_invitations(template, attendees):
    """Create one invitation file per attendee from a template string.

    Placeholders in the template are replaced with each attendee's data.
    Missing values are replaced with "N/A". Output files are named
    output_1.txt, output_2.txt, and so on.

    Args:
        template: the invitation text containing placeholders.
        attendees: a list of dictionaries holding each attendee's data.
    """
    if not isinstance(template, str):
        print("Error: template must be a string, got "
              f"{type(template).__name__}")
        return

    if not isinstance(attendees, list) or \
            not all(isinstance(item, dict) for item in attendees):
        print("Error: attendees must be a list of dictionaries")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    fields = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        content = template
        for field in fields:
            value = attendee.get(field)
            if value is None:
                value = "N/A"
            content = content.replace("{" + field + "}", str(value))

        filename = "output_{}.txt".format(index)
        if os.path.exists(filename):
            print("Warning: {} already exists, skipping.".format(filename))
            continue

        try:
            with open(filename, "w", encoding="utf-8") as output:
                output.write(content)
        except OSError as err:
            print("Error writing {}: {}".format(filename, err))
