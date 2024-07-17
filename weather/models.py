from pydantic import BaseModel


class Location(BaseModel):
    long: str | None = None
    lat: str | None = None