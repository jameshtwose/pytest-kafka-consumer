"""This module contains the Kafka consumer function that consumes messages

- kafka_consumer: Consumes messages from a Kafka topic, processes them, and logs the results.

"""

import logging
from confluent_kafka import Consumer
from consumer.utils import deserialize_message
from consumer.business_logic import message_processing_pipeline

logger = logging.getLogger(__name__)

def kafka_consumer(
    kafka_topic: str = "test",
    kafka_group_id: str = "test_group",
    kafka_brokers: str = "localhost:9092",
):
    """This function consumes messages from a Kafka topic, does some
    processing on the messages, and logs the results.
    
    Parameters
    ----------
    kafka_topic : str
        The Kafka topic to consume messages from.
    kafka_group_id : str
        The Kafka consumer group id.
    kafka_brokers : str
        The Kafka brokers to connect to.
    
    Returns
    -------
    None
    
    """
    consumer = Consumer(
        {
            # For more info on these settings, see:
            # https://kafka.apache.org/documentation/#consumerconfigs
            # use a comma seperated str to add multiple brokers
            "bootstrap.servers": kafka_brokers,
            "group.id": kafka_group_id,
            "auto.offset.reset": "latest",
            "socket.keepalive.enable": True,
        }
    )

    consumer.subscribe([kafka_topic])
    logger.info(f"Consumer is subscribed op topic {kafka_topic}")
    while True:
        msgs = consumer.consume(num_messages=300, timeout=5)
        if msgs is None:
            continue
        logger.info(f"Received {len(msgs)} messages")

        msgs_list = [msg.value() for msg in msgs]
        if len(msgs_list) == 0:
            continue
        else:
            try:
                converted_messages = [
                    deserialize_message(raw_message) for raw_message in msgs_list
                ]
            except Exception as e:
                logger.error(f"Error deserializing message: {e}")
                continue

            for message in converted_messages:
                new_yaml = message_processing_pipeline(message=message)