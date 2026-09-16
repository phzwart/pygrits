"""Bundle checks. The agent can omit these; this function must not."""

from __future__ import annotations

from collections.abc import Iterable

from pygrits.models import Activity, Bundle, Entity, Node, Plan


class BundleValidationError(ValueError):
    pass


def _as_graph(src: Bundle | Iterable[Node]) -> tuple[list[Node], Bundle | None]:
    if isinstance(src, Bundle):
        return list(src.graph), src
    return list(src), None


def validate(src: Bundle | Iterable[Node]) -> None:
    nodes, _ = _as_graph(src)
    by_id = {node.id: node for node in nodes}
    if len(by_id) != len(nodes):
        raise BundleValidationError("duplicate @id in graph")
    plans = {node.id for node in nodes if isinstance(node, Plan)}

    for node in nodes:
        if isinstance(node, (Entity, Activity)):
            if node.plan not in by_id:
                raise BundleValidationError(f"{node.id}: missing id {node.plan!r} in bundle")
            if node.plan not in plans:
                raise BundleValidationError(f"{node.id}: plan {node.plan!r} is not a prov:Plan")
        if isinstance(node, Entity):
            if node.how in ("derived", "inferred") and not (node.rationale and node.rationale.strip()):
                raise BundleValidationError(f"{node.id}: {node.how} requires rationale")
            if node.how == "quote" and (node.source is None or node.target is None):
                raise BundleValidationError(f"{node.id}: quote requires source and target")
            if node.how == "quote" and node.result is not None:
                raise BundleValidationError(f"{node.id}: quote cannot also have result")
            if node.result is not None and not (node.summary and node.summary.strip()):
                raise BundleValidationError(f"{node.id}: result requires summary")
        if isinstance(node, Activity):
            for ref in node.used + node.generated:
                if ref not in by_id:
                    raise BundleValidationError(f"{node.id}: missing id {ref!r} in bundle")
            if node.kind in ("support", "contradiction") and node.generated:
                raise BundleValidationError(f"{node.id}: {node.kind} must not have generated")
            if node.kind == "adjudication" and not (node.rationale and node.rationale.strip()):
                raise BundleValidationError(f"{node.id}: adjudication requires rationale")


validate_bundle = validate
