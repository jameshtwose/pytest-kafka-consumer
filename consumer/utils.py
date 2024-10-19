"""This module contains utility functions for the avro schema and jinja template handling.

- deserialize_message: Deserializes a serialized message.
- serialize_message: Serializes a message.
- create_filled_jinja_template: Fills a jinja template with a message.

"""

from typing import Any, Union
import io
from fastavro import parse_schema, schemaless_reader, schemaless_writer
from jinja2 import Environment, FileSystemLoader


def deserialize_message(
    serialized_message: bytes,
    avro_schema: Union[str, list[Any], dict[Any, Any]],
    schema_id: None | bytes = None,
) -> dict:
    """This function deserializes a serialized message. The message should have been serialized with the provided
    avro schema.

    Parameters
    ----------
    serialized_message : bytes
        Message that has been serialized according to the schema that is provided.
    avro_schema : (Union[str, List[Any], Dict[Any, Any]])
        The avro schema used to deserialize the message.

    Returns
    -------
    dict
        The message in dictionary format.

    """
    parsed_schema = parse_schema(avro_schema)
    if schema_id:
        bytes_reader = io.BytesIO(serialized_message[len(schema_id) :])
    else:
        bytes_reader = io.BytesIO(serialized_message)
    message = schemaless_reader(bytes_reader, parsed_schema)
    return message


def serialize_message(
    message: dict[str, Any],
    avro_schema: Union[str, list[Any], dict[Any, Any]],
) -> bytes:
    """This function serializes a message with the provided avro schema. The message should follow the format of
    the provided schema.

    Parameters
    ----------
    message : Dict[str, Any]
        The dictionary to be converted to bytes.
    avro_schema : (Union[str, List[Any], Dict[Any, Any]])
        The avro schema used to serialize the message dict.

    Returns
    -------
    bytes
        The message in bytes.

    """
    parsed_schema = parse_schema(avro_schema)
    bytes_writer = io.BytesIO()
    schemaless_writer(bytes_writer, parsed_schema, message)
    return bytes_writer.getvalue()


def create_filled_jinja_template(
    message: dict[str, Any],
    template_path: str = "./",
    template_file: str = "example_template.yaml",
) -> str:
    """This function fills a jinja template with the provided message.

    Parameters
    ----------
    message : Dict[str, Any]
        The message to fill the template with.
    template_path : str
        The path to the jinja template.
    template_file : str
        The name of the jinja (yaml) template file.

    Returns
    -------
    str
        The filled template as a string.

    """
    env = Environment(
        loader=FileSystemLoader(template_path), trim_blocks=True, lstrip_blocks=True
    )
    return env.get_template(template_file).render(message)
