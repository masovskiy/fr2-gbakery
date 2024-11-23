import re
import typing


def get_file_id(data: str) -> tuple[typing.Any, bool]:
    match = re.search(r'src="([^"]+)"', data)
    if match:
        return match.group(1), True
    else:
        return data, False
