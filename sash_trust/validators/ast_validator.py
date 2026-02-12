"""
AST-based validator.

Designed for structural code analysis without executing code.
Currently supports Python AST scanning.
"""

from __future__ import annotations

import ast
from pathlib import Path
from typing import List

from sash_trust.validators.base import BaseValidator
from sash_trust.core.result import Finding
from sash_trust.utils.file_utils import safe_read_text


class _SecureASTVisitor(ast.NodeVisitor):
    """
    Custom AST visitor for detecting insecure patterns.
    Extend this class to add new structural rules.
    """

    def __init__(self) -> None:
        self.issues: List[str] = []

    def visit_Call(self, node: ast.Call) -> None:
        # Detect usage of eval or exec
        if isinstance(node.func, ast.Name):
            if node.func.id in {"eval", "exec"}:
                self.issues.append(
                    f"Insecure function usage detected: {node.func.id}"
                )
        self.generic_visit(node)

    def visit_Import(self, node: ast.Import) -> None:
        # Example: detect unsafe modules
        for alias in node.names:
            if alias.name == "pickle":
                self.issues.append(
                    "Potentially unsafe module imported: pickle"
                )
        self.generic_visit(node)


class ASTValidator(BaseValidator):
    """
    Structural validator using AST parsing.

    - Does NOT execute code.
    - Safe for untrusted files.
    - Python-only (for now).
    """

    def __init__(self, severity: int = 20) -> None:
        self._severity = severity

    async def validate(self, file_path: Path) -> Finding | None:
        # Only process Python files
        if file_path.suffix != ".py":
            return None

        source = safe_read_text(file_path)
        if not source:
            return None

        try:
            tree = ast.parse(source)
        except SyntaxError:
            # Do not crash engine if file has syntax error
            return None

        visitor = _SecureASTVisitor()
        visitor.visit(tree)

        if visitor.issues:
            return Finding(
                file_path=str(file_path),
                message="; ".join(visitor.issues),
                severity=self._severity,
            )

        return None
