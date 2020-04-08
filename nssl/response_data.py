from typing import Generic, Optional, TypeVar

from dataclasses import dataclass

T = TypeVar('T')


@dataclass(frozen=True)
class ResponseData(Generic[T]):
    success: bool = False
    error: str = 'Unknown Error'

    data: Optional[T] = None