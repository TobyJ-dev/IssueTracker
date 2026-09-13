from dataclasses import dataclass
from enum import Enum


class Priority(Enum):
    HIGH = ("High", "🔺")
    MEDIUM = ("Medium", "🔸")
    LOW = ("Low", "🔹")

    @property
    def label(self) -> str:
        return self.value[0]

    @property
    def icon(self) -> str:
        return self.value[1]


class Status(Enum):
    PENDING = ("Pending", "🔴")
    IN_PROGRESS = ("In Progress", "🟠")
    DONE = ("Done", "🟢")
    WONT_FIX = ("Won't Fix", "⚫")

    @property
    def label(self) -> str:
        return self.value[0]

    @property
    def icon(self) -> str:
        return self.value[1]


@dataclass
class Issue:
    issue_id: str
    title: str
    issue_type: str
    priority: Priority
    status: Status
    reporter: str
    aiu: bool
    request_date: str
    resolved_date: str

    def __str__(self) -> str:
        return (
            f"{self.issue_id} | "
            f"{self.title} | "
            f"{self.status.icon} {self.status.label}"
        )