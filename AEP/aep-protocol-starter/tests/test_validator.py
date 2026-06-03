from pathlib import Path

from aep.validator import validate_aep


def test_example_package_valid():
    root = Path(__file__).resolve().parents[1]
    package = root / "examples" / "MT-001_Runtime_Cloud_System_AEP_v0.1"
    result = validate_aep(package)
    assert result.ok, [issue.message for issue in result.errors]


def test_template_package_valid():
    root = Path(__file__).resolve().parents[1]
    package = root / "templates" / "basic_aep"
    result = validate_aep(package)
    assert result.ok, [issue.message for issue in result.errors]
