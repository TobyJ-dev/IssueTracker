import json
from dataclasses import asdict

from issue_parser import IssueParser


def issue_to_dict(issue):
    data = asdict(issue)

    data["priority"] = issue.priority.label
    data["status"] = issue.status.label

    return data


def main():

    parser = IssueParser("project_management/ISSUES.md")
    issues = parser.parse()

    data = [
        issue_to_dict(issue)
        for issue in issues
    ]

    with open(
        "project_management/summary/issues.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False,
        )

    print(f"Exported {len(data)} issues.")


if __name__ == "__main__":
    main()