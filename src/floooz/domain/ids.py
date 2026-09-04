"""Typed, stable identifiers for Floooz domain entities."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, TypeVar
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class DomainId:
    """Base value object for durable domain identifiers.

    The runtime value is a UUID, while concrete subclasses prevent accidental
    substitution of one domain identifier for another at typed boundaries.
    """

    value: UUID
    kind: ClassVar[str] = "domain"

    def __post_init__(self) -> None:
        if not isinstance(self.value, UUID):
            raise TypeError(f"{type(self).__name__} requires a UUID value")

    @classmethod
    def new(cls) -> Any:
        """Create a new identifier of this concrete type."""
        return cls(uuid4())

    @classmethod
    def from_string(cls, value: str) -> Any:
        """Deserialize the canonical UUID string form."""
        if not isinstance(value, str):
            raise TypeError(f"{cls.__name__}.from_string requires a string")
        try:
            return cls(UUID(value))
        except ValueError as exc:
            raise ValueError(f"invalid {cls.__name__}: {value!r}") from exc

    def to_string(self) -> str:
        """Serialize to the canonical UUID string form."""
        return str(self.value)

    def __str__(self) -> str:
        return self.to_string()


@dataclass(frozen=True, slots=True)
class UserId(DomainId):
    kind: ClassVar[str] = "user"


@dataclass(frozen=True, slots=True)
class AgentId(DomainId):
    kind: ClassVar[str] = "agent"


@dataclass(frozen=True, slots=True)
class DeviceId(DomainId):
    kind: ClassVar[str] = "device"


@dataclass(frozen=True, slots=True)
class SessionId(DomainId):
    kind: ClassVar[str] = "session"


@dataclass(frozen=True, slots=True)
class MemoryId(DomainId):
    kind: ClassVar[str] = "memory"


@dataclass(frozen=True, slots=True)
class CapabilityId(DomainId):
    kind: ClassVar[str] = "capability"


@dataclass(frozen=True, slots=True)
class BindingId(DomainId):
    kind: ClassVar[str] = "binding"


@dataclass(frozen=True, slots=True)
class WorkflowId(DomainId):
    kind: ClassVar[str] = "workflow"


@dataclass(frozen=True, slots=True)
class ExtensionId(DomainId):
    kind: ClassVar[str] = "extension"


@dataclass(frozen=True, slots=True)
class RelationshipId(DomainId):
    kind: ClassVar[str] = "relationship"


TDomainId = TypeVar("TDomainId", bound=DomainId)


def serialize_id(identifier: TDomainId) -> str:
    """Serialize any concrete domain ID without erasing its typed API contract."""
    if not isinstance(identifier, DomainId):
        raise TypeError("serialize_id requires a DomainId")
    return identifier.to_string()
