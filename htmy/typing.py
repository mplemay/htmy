from collections.abc import Callable, Coroutine, Mapping
from typing import Any, Protocol, TypeAlias, TypeGuard, TypeVar, runtime_checkable

T = TypeVar("T")
U = TypeVar("U")

# -- Properties

PropertyValue: TypeAlias = Any | None
"""Component/XML tag property value."""

Properties: TypeAlias = Mapping[str, PropertyValue]
"""Component/XML tag property mapping."""

# -- Context

ContextKey: TypeAlias = Any
"""Context key."""

ContextValue: TypeAlias = Any
"""Context value."""

Context: TypeAlias = Mapping[ContextKey, ContextValue]
"""Context mapping."""

# -- Components


@runtime_checkable
class SyncComponent(Protocol):
    """Protocol definition for sync `htmy` components."""

    def htmy(self, context: Context, /) -> "Component": ...


@runtime_checkable
class AsyncComponent(Protocol):
    """Protocol definition for async `htmy` components."""

    async def htmy(self, context: Context, /) -> "Component": ...


HTMYComponentType: TypeAlias = SyncComponent | AsyncComponent
"""Sync or async `htmy` component type."""

ComponentType: TypeAlias = HTMYComponentType | str
"""Type definition for a single component."""

# Omit strings from this type to simplify checks.
ComponentSequence: TypeAlias = list[ComponentType] | tuple[ComponentType, ...]
"""Component sequence type."""

Component: TypeAlias = ComponentType | ComponentSequence
"""Component type: a single component or a sequence of components."""


def is_component_sequence(obj: Any) -> TypeGuard[ComponentSequence]:
    """Returns whether the given object is a component sequence."""
    return isinstance(obj, (list, tuple))


SyncFunctionComponent: TypeAlias = Callable[[T, Context], Component]
"""Protocol definition for sync function components."""

AsyncFunctionComponent: TypeAlias = Callable[[T, Context], Coroutine[Any, Any, Component]]
"""Protocol definition for async function components."""

FunctionComponent: TypeAlias = SyncFunctionComponent[T] | AsyncFunctionComponent[T]
"""Function component type."""

# -- Context providers


@runtime_checkable
class SyncContextProvider(Protocol):
    """Protocol definition for sync context providers."""

    def htmy_context(self) -> Context: ...


@runtime_checkable
class AsyncContextProvider(Protocol):
    """Protocol definition for async context providers."""

    async def htmy_context(self) -> Context: ...


ContextProvider: TypeAlias = SyncContextProvider | AsyncContextProvider
"""Context provider type."""