from sqlalchemy import types

from src.common.location import Location


class SerializableLocation(types.TypeDecorator):
    impl = types.Unicode

    @property
    def python_type(self):
        return Location

    def process_literal_param(self, value, dialect):
        return value.serialize()

    def process_bind_param(self, value, dialect):
        return value.serialize()

    def process_result_value(self, value, dialect):
        return Location.deserialize(value)
