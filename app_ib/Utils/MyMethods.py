from ast import Pass
import time
from types import SimpleNamespace
import json
class MY_METHODS:
    @staticmethod
    def GetCurrentTimeinStr():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    @staticmethod
    def GetCurrentTimeinInt():
        return int(time.time())
    
    @staticmethod
    def json_to_object(json_data):
        """
        Convert a JSON string or dictionary to a dot notation object.
        """
        if isinstance(json_data, str):
            json_data = json.loads(json_data)

        def convert(item):
            if isinstance(item, dict):
                return type('JSONObject', (), {k: convert(v) for k, v in item.items()})()
            elif isinstance(item, list):
                return [convert(i) for i in item]
            else:
                return item
        return convert(json_data)


    @staticmethod
    def object_to_json(obj):
        def convert(item):
            if isinstance(item, list):
                return [convert(i) for i in item]
            elif isinstance(item, dict):
                return {k: convert(v) for k, v in item.items()}
            elif hasattr(item, "__dict__"):
                return {k: convert(v) for k, v in item.__dict__.items()}
            else:
                return item

        return json.dumps(convert(obj), default=str, indent=4)