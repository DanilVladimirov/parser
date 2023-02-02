import sqlalchemy.orm
import sqlalchemy as sa
import fastapi as fa
import response_codes
from core import database
from urls.schemas import urls_schemas
from urls import query
from models import urls as urls_models


router = fa.APIRouter()


@router.post(
    "/get-urls-by-domain",
    response_model=urls_schemas.ResponseUrlsByDomain,
    responses={
        **response_codes.RESPONSE_404,
    },
)
async def get_urls_by_domain(
    request: urls_schemas.RequestUrlsByDomain,
    db: sa.orm.Session = fa.Depends(database.get_db),
):
    urls_list = db.scalars(
        db.query(urls_models.Urls.url).where(
            urls_models.Urls.domain_name == request.domain_name
        )
    ).all()

    if not urls_list:
        raise fa.HTTPException(
            status_code=404, detail="Записів з таким доменом не знайшлося"
        )

    domain_stats = query.get_domain_stats(request.domain_name, db)

    return {**domain_stats._asdict(), "urls_list": urls_list}


@router.post(
    "/latest-url-info",
    response_model=urls_schemas.ResponseLastUrlInfoByUrl,
    responses={
        **response_codes.RESPONSE_404,
    },
)
async def get_latest_url_info(
    request: urls_schemas.RequestLastUrlInfoByUrl,
    db: sa.orm.Session = fa.Depends(database.get_db),
):
    latest_url_info = query.get_latest_url(request.url, db)

    if not latest_url_info:
        raise fa.HTTPException(
            status_code=404, detail="Статистики за цим посиланням не знайшлося"
        )

    return latest_url_info
