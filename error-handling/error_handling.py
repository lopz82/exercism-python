from typing import Optional, Union, Tuple


def handle_error_by_throwing_exception() -> None:
    raise Exception("Exception raised")


def handle_error_by_returning_none(input_data: str) -> Optional[int]:
    try:
        n = int(input_data)
    except ValueError:
        return None
    else:
        return n


def handle_error_by_returning_tuple(input_data: str) -> Tuple[bool, Union[int, str]]:
    try:
        n = int(input_data)
    except ValueError:
        return False, input_data
    else:
        return True, n


def filelike_objects_are_closed_on_exception(filelike_object: "FileLike") -> None:
    with filelike_object as fp:
        fp.do_something()
