import pytest
import json
from consumer.utils import serialize_message, deserialize_message

@pytest.fixture
def example_json():
    with open("example.json", "r") as f:
        return json.loads(f.read())
    
@pytest.fixture
def example_avsc():
    with open("example.avsc", "r") as f:
        return json.loads(f.read())

@pytest.fixture
def example_template():
    with open("example_template.yaml", "r") as f:
        return f.read()
    
class TestUtils:
    """Tests for the utils module."""
    def test_serialize_message(self, example_json, example_avsc):
        """Test that the serialize_message function works as expected."""
        serialized_message = serialize_message(example_json, example_avsc)
        assert isinstance(serialized_message, bytes)
        assert len(serialized_message) > 0
        assert serialized_message == b'\x02\x10John Doe(john.doe@example.com<\x08male\x01\x01\x00\x01\x16123 Main St\x0eAnytown\x04CA\n12345\x06USA(2023-10-01T12:34:56Z\x04\xca\x01\x0cLaptop(2023-09-15T10:00:00ZR\xb8\x1e\x85\xeb?\x8f@\xcc\x01\nMouse(2023-09-16T11:30:00Z\x00\x00\x00\x00\x00\x809@\x00'
        
    def test_deserialize_message(self, example_json, example_avsc):
        """Test that the deserialize_message function works as expected."""
        serialized_message = serialize_message(example_json, example_avsc)
        deserialized_message = deserialize_message(serialized_message, example_avsc) 
        assert isinstance(deserialized_message, dict)
        assert len(deserialized_message) > 0
        assert deserialized_message == example_json
        assert deserialized_message.get("name") == "John Doe"
        