import uuid
import sqlalchemy as sa
import datetime as dt
from sqlalchemy.dialects import postgresql
from core import database


class Urls(database.Base):
    __tablename__ = "urls"

    id: uuid.UUID = sa.Column(
        postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    url: str = sa.Column(postgresql.TEXT, nullable=False, index=True)
    final_url: str = sa.Column(postgresql.TEXT, nullable=True)
    status_code: int = sa.Column(postgresql.INTEGER(), nullable=True)
    page_title: str = sa.Column(postgresql.VARCHAR(), nullable=True)
    domain_name: str = sa.Column(postgresql.VARCHAR(), nullable=False, index=True)
    parse_date: dt.datetime = sa.Column(postgresql.TIMESTAMP, nullable=False)
    visit_date: dt.datetime = sa.Column(postgresql.TIMESTAMP, nullable=False)
