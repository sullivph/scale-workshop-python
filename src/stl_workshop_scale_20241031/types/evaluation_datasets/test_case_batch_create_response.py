# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .test_case_version import TestCaseVersion

__all__ = ["TestCaseBatchCreateResponse"]

TestCaseBatchCreateResponse: TypeAlias = List[TestCaseVersion]
