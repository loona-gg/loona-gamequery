import base64
from io import BytesIO
from typing import Dict, Any, Optional, Union, List

from pydantic import BaseModel, Field, root_validator, model_validator, ConfigDict, computed_field, field_validator, \
    HttpUrl


class ServerPlayer(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None

    class Config:
        extra = "allow"


class PlayersList(BaseModel):
    online: Optional[int] = 0
    max: Optional[int] = 0
    list: Optional[List[ServerPlayer]] = []


class ServerStatus(BaseModel):
    # TODO: Implement this model as a replacement for the current server status models
    name: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[bytes] = Field(None, alias='favicon', repr=False)
    version: Optional[str] = None

    players_list: Optional[PlayersList] = None

    class Config:
        extra = "allow"

    @field_validator('icon', mode='before')
    @classmethod
    def validate_icon(cls, v: Union[str, bytes]):
        if isinstance(v, str):
            if 'base64' in v:  # Check if the icon is a base64 string
                return base64.b64decode(v.split(",")[1])
        return v

    @field_validator('version', mode='before')
    @classmethod
    def validate_version(cls, v: Union[str, Dict]):
        if isinstance(v, str):
            return v
        elif isinstance(v, dict):
            return v.get("name", "Unknown")
        return v
