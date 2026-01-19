import ast
from bina.core.models import BaseRule, Severity

class NoPrintRule(BaseRule):
    id = "CP01"
    name = "No Print"
    description = "Flags usage of print() calls."
    severity = Severity.MEDIUM

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id == "print":
            self.report("Found print() call. Use logging instead.", node)
        self.generic_visit(node)
