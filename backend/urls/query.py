import sqlalchemy.orm
import sqlalchemy as sa
from models import urls as urls_models


def get_domain_stats(domain_name: str, db: sa.orm.Session) -> sa.engine.row.Row | None:
    active_page_count_sub_q = db.query(sa.func.count(urls_models.Urls.id)).where(
        sa.and_(
            urls_models.Urls.domain_name == domain_name,
            urls_models.Urls.status_code == 200,
        )
    )

    return (
        db.query(
            sa.func.max(urls_models.Urls.visit_date).label("last_visit_date"),
            sa.func.min(urls_models.Urls.visit_date).label("first_visit_date"),
            sa.func.count(urls_models.Urls.id).label("page_count"),
            active_page_count_sub_q.label("active_page_count"),
        )
        .where(urls_models.Urls.domain_name == domain_name)
        .first()
    )


def get_latest_url(url: str, db: sa.orm.Session) -> sa.engine.row.Row | None:
    return (
        db.query(
            urls_models.Urls.visit_date,
            urls_models.Urls.parse_date,
            urls_models.Urls.final_url,
            urls_models.Urls.status_code,
            urls_models.Urls.page_title,
            urls_models.Urls.domain_name,
        )
        .where(urls_models.Urls.url.like(f"{url}%"))
        .order_by(urls_models.Urls.visit_date.desc())
        .first()
    )
