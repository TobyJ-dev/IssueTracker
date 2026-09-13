from collections import Counter

from models import Issue, Priority, Status


class IssueStatistics:

    def __init__(self, issues: list[Issue]):
        self.issues = issues

    def total_issues(self) -> int:
        return len(self.issues)

    def status_counts(self) -> Counter:
        return Counter(issue.status for issue in self.issues)

    def type_counts(self) -> Counter:
        return Counter(issue.issue_type for issue in self.issues)

    def progress(self) -> float:
        if not self.issues:
            return 0.0

        done = sum(
            issue.status == Status.DONE
            for issue in self.issues
        )

        return done / len(self.issues) * 100

    def high_priority(self) -> list[Issue]:
        return sorted(
            (
                issue
                for issue in self.issues
                if issue.priority == Priority.HIGH
            ),
            key=lambda issue: issue.issue_id,
            reverse=True,
        )

    def oldest_pending(self) -> list[Issue]:
        return sorted(
            (
                issue
                for issue in self.issues
                if issue.status == Status.PENDING
            ),
            key=lambda issue: issue.issue_id,
        )

    def newest(self) -> list[Issue]:
        return sorted(
            self.issues,
            key=lambda issue: issue.issue_id,
            reverse=True,
        )

    def overview(self) -> list[Issue]:
        return sorted(
            self.issues,
            key=lambda issue: issue.issue_id,
            reverse=True,
        )