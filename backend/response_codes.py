import typing as t
import pydantic


class Message(pydantic.BaseModel):
    detail: str


RESPONSE_SCHEME: t.Dict[str, t.Any] = {"model": Message}

RESPONSE_304: t.Mapping[t.Union[int, str], t.Dict[str, t.Any]] = {
    304: {
        "description": "not modified",
    }
}

RESPONSE_400: t.Mapping[t.Union[int, str], t.Dict[str, t.Any]] = {
    400: {"description": "error msg", **RESPONSE_SCHEME}
}

RESPONSE_401: t.Mapping[t.Union[int, str], t.Dict[str, t.Any]] = {
    401: {"description": "invalid token", **RESPONSE_SCHEME}
}

RESPONSE_403: t.Mapping[t.Union[int, str], t.Dict[str, t.Any]] = {
    403: {"description": "access denied", **RESPONSE_SCHEME}
}

RESPONSE_404: t.Mapping[t.Union[int, str], t.Dict[str, t.Any]] = {
    404: {"description": "not found", **RESPONSE_SCHEME}
}

RESPONSE_405: t.Mapping[t.Union[int, str], t.Dict[str, t.Any]] = {
    405: {"description": "error msg", **RESPONSE_SCHEME}
}
