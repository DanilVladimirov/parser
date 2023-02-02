import pydantic
import datetime as dt


class RequestUrlsByDomain(pydantic.BaseModel):
    domain_name: str


class ResponseUrlsByDomain(pydantic.BaseModel):
    last_visit_date: dt.datetime
    first_visit_date: dt.datetime
    page_count: int
    active_page_count: int
    urls_list: list[pydantic.AnyHttpUrl]


class RequestLastUrlInfoByUrl(pydantic.BaseModel):
    url: pydantic.AnyHttpUrl


class ResponseLastUrlInfoByUrl(pydantic.BaseModel):
    visit_date: dt.datetime
    parse_date: dt.datetime
    final_url: pydantic.AnyHttpUrl | None = None
    status_code: int
    page_title: str | None = None
    domain_name: str

    class Config:
        orm_mode = True
