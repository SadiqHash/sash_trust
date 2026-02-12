from pydantic import BaseModel
from typing import List


class Rule(BaseModel):
    name: str
    type: str
    severity: int
    pattern: str | None = None


class PolicySchema(BaseModel):
    rules: List[Rule]

    def build_validators(self):
        from sash_trust.validators.regex_validator import RegexValidator

        validators = []

        for rule in self.rules:
            if rule.type == "regex":
                validators.append(
                    RegexValidator(rule.pattern, rule.severity)
                )

        return validators
