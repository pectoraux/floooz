import sys
import unittest
from uuid import UUID
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from floooz.domain.ids import (  # noqa: E402
    AgentId,
    BindingId,
    CapabilityId,
    DeviceId,
    DomainId,
    ExtensionId,
    MemoryId,
    RelationshipId,
    SessionId,
    UserId,
    WorkflowId,
)


ID_TYPES = (
    UserId,
    AgentId,
    DeviceId,
    SessionId,
    MemoryId,
    CapabilityId,
    BindingId,
    WorkflowId,
    ExtensionId,
    RelationshipId,
)


class DomainIdTests(unittest.TestCase):
    def test_all_required_identifier_types_exist(self) -> None:
        self.assertEqual(len(ID_TYPES), 10)
        self.assertTrue(all(issubclass(identifier_type, DomainId) for identifier_type in ID_TYPES))
        self.assertEqual([identifier_type.kind for identifier_type in ID_TYPES], [
            "user", "agent", "device", "session", "memory",
            "capability", "binding", "workflow", "extension", "relationship",
        ])

    def test_round_trip_serialization_preserves_concrete_type(self) -> None:
        for identifier_type in ID_TYPES:
            with self.subTest(identifier_type=identifier_type.__name__):
                identifier = identifier_type.new()
                serialized = identifier.to_string()
                restored = identifier_type.from_string(serialized)

                self.assertIsInstance(identifier.value, UUID)
                self.assertIsInstance(restored, identifier_type)
                self.assertEqual(restored, identifier)
                self.assertEqual(str(restored), serialized)

    def test_identifier_types_are_not_interchangeable(self) -> None:
        value = UUID("12345678-1234-5678-1234-567812345678")
        self.assertNotEqual(UserId(value), AgentId(value))
        self.assertNotIsInstance(UserId(value), AgentId)
        self.assertNotIsInstance(AgentId(value), UserId)

    def test_invalid_values_fail_fast(self) -> None:
        with self.assertRaises(TypeError):
            UserId("not-a-uuid")  # type: ignore[arg-type]
        with self.assertRaises(TypeError):
            UserId.from_string(123)  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            UserId.from_string("not-a-uuid")

    def test_new_ids_are_stable_value_objects(self) -> None:
        first = AgentId.new()
        second = AgentId.from_string(first.to_string())
        self.assertEqual(first, second)
        self.assertIsNot(first, second)


if __name__ == "__main__":
    unittest.main()
