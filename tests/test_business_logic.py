from consumer.business_logic import (
    add_timezone_info,
    convert_money_int_to_str,
    convert_to_lower_case,
    message_processing_pipeline,
)
import json
import pytest

@pytest.fixture
def example_json():
    with open("example.json", "r") as f:
        return json.loads(f.read())

class TestBusinessLogic:
    """Tests for the business_logic module."""

    def test_add_timezone_info(self):
        """Test that the add_timezone_info function works as expected."""
        assert add_timezone_info("2023-10-01T12:34:56Z") == "2023-10-01T12:34:56+02:00"

    def test_convert_money_int_to_str(self):
        """Test that the convert_money_int_to_str function works as expected."""
        assert convert_money_int_to_str(99999) == "$99999.00"

    def test_convert_to_lower_case(self):
        """Test that the convert_to_lower_case function works as expected."""
        assert convert_to_lower_case("Hello, World!") == "hello, world!"

    def test_add_timezone_info_invalid_datetime(self):
        """Test that the add_timezone_info function raises a
        ValueError for an invalid datetime string."""
        with pytest.raises(ValueError) as e:
            add_timezone_info("10-01-2023 12:34:56")
            # check that the exception message is correct
            assert str(e.value) == "Invalid datetime string: 10-01-2023 12:34:56"
            
    def test_convert_money_int_to_str_invalid_money_int(self):
        """Test that the convert_money_int_to_str function raises a
        ValueError for an invalid money integer."""
        with pytest.raises(ValueError) as e:
            convert_money_int_to_str("sup")
            # check that the exception message is correct
            assert str(e.value) == "Invalid money integer: sup"
            
    def test_convert_to_lower_case_invalid_string(self):
        """Test that the convert_to_lower_case function raises an
        AttributeError for an invalid string."""
        with pytest.raises(AttributeError) as e:
            convert_to_lower_case(123)
            # check that the exception message is correct
            assert str(e.value) == "Invalid string: 123"
            
    def test_message_processing_pipeline(self, example_json):
        """Test that the message_processing_pipeline function works as expected."""
        processed_message = message_processing_pipeline(example_json)
        assert isinstance(processed_message, dict)
        assert len(processed_message) > 0
        assert processed_message.get("name") == "John Doe"
        assert processed_message.get("history").get("last_login") == "2023-10-01T12:34:56+02:00"
        assert processed_message.get("history").get("purchase_history")[0].get("purchase_date") == "2023-09-15T10:00:00+02:00"
        assert processed_message.get("history").get("purchase_history")[0].get("amount") == "$999.99"
        assert processed_message.get("history").get("purchase_history")[0].get("item_name") == "laptop"
        assert processed_message.get("history").get("purchase_history")[1].get("purchase_date") == "2023-09-16T11:30:00+02:00"
        assert processed_message.get("history").get("purchase_history")[1].get("amount") == "$25.50"
        assert processed_message.get("history").get("purchase_history")[1].get("item_name") == "mouse"