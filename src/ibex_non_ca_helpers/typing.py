from numpy.typing import ArrayLike

__all__ = ["PVBaseValue", "PVValue"]

type PVBaseValue = bool | int | float | str | bytes
type PVValue = PVBaseValue | list[PVBaseValue] | ArrayLike | None
