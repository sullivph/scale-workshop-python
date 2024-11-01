# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SystemMessage"]


class SystemMessage(BaseModel):
    content: List[str]

    role: Literal["system"]
