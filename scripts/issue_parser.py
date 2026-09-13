import re
from pathlib import Path

from models import Issue, Priority, Status


class IssueParser:
    """
    Parses DiscounTJer ISSUES.md and returns Issue objects.
    """

    def __init__(self, issue_file: str | Path):
        self.issue_file = Path(issue_file)

    def parse(self) -> list[Issue]:
        """
        Parse all issues contained in the markdown file.

        Returns
        -------
        list[Issue]
        """

        with self.issue_file.open(
            mode="r",
            encoding="utf-8"
        ) as f:
            content = f.read()

        issue_blocks = re.split(
            r"(?=^## DTJ-\d+)",
            content,
            flags=re.MULTILINE
        )

        issues: list[Issue] = []

        for block in issue_blocks:

            block = block.strip()

            if not block:
                continue
            
            if "DTJ-XXX" in block:
                continue

            if not re.match(r"##\s+(TGIS-\d+)\s+—\s+", block):
                continue

            issues.append(self._parse_issue(block))

        return issues

    @staticmethod
    def _extract(pattern: str, text: str) -> str:
        """
        Extract the first regex group.

        Raises
        ------
        ValueError
            If the pattern could not be found.
        """

        match = re.search(pattern, text, re.MULTILINE)

        if match is None:
            raise ValueError(
                f"Could not parse pattern:\n{pattern}"
            )

        return match.group(1).strip()

    def _parse_issue(self, block: str) -> Issue:
        """
        Parse a single markdown issue.
        """

        # title = self._extract(
        #     r"^##\s+(DTJ-\d+)\s+—\s+(.+)$",
        #     block
        # )

        issue_id, title = re.search(
            r"^##\s+(DTJ-\d+)\s+—\s+(.+)$",
            block,
            re.MULTILINE
        ).groups()

        issue_type = self._extract(
            r"\*\*Type:\*\*\s*(.+)",
            block
        )

        priority = self._parse_priority(
            self._extract(
                r"\*\*Priority:\*\*\s*(.+)",
                block
            )
        )

        status = self._parse_status(
            self._extract(
                r"\*\*Status:\*\*\s*(.+)",
                block
            )
        )

        reporter = self._extract(
            r"\*\*Reporter:\*\*\s*(.+)",
            block
        )
        
        aiu = self._extract(
            r"\*\*AIU:\*\*\s*(.+)",
            block,
        )

        request_date = self._extract(
            r"\*\*Request Date:\*\*\s*(.+)",
            block
        )

        resolved_date = self._extract(
            r"\*\*Resolved Date:\*\*\s*(.+)",
            block
        )

        return Issue(
            issue_id=issue_id,
            title=title,
            issue_type=issue_type,
            priority=priority,
            status=status,
            reporter=reporter,
            aiu=aiu.lower() == "yes",
            request_date=request_date,
            resolved_date=resolved_date,
        )


    @staticmethod
    def _parse_priority(text: str) -> Priority:
        text = text.replace("🔺", "").replace("🔸", "").replace("🔹", "").strip()

        mapping = {
            "High": Priority.HIGH,
            "Medium": Priority.MEDIUM,
            "Low": Priority.LOW,
        }

        return mapping[text]


    @staticmethod
    def _parse_status(text: str) -> Status:
        text = (
            text.replace("🔴", "")
                .replace("🟠", "")
                .replace("🟢", "")
                .replace("⚫", "")
                .strip()
        )

        mapping = {
            "Pending": Status.PENDING,
            "In Progress": Status.IN_PROGRESS,
            "Done": Status.DONE,
            "Won't Fix": Status.WONT_FIX,
        }

        return mapping[text]


if __name__ == "__main__":

    parser = IssueParser("project_management/ISSUES.md")

    issues = parser.parse()

    print(f"Parsed {len(issues)} issues.\n")

    for issue in issues:
        print(issue)