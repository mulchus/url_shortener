
from pydantic import BaseModel


class URLBase(BaseModel):
    target_url: str
    custom_key: str = None


class URL(URLBase):
    is_active: bool
    clicks: int

    class Config:
        orm_mode = True


class URLInfo(URL):
    url: str
    admin_url: str
