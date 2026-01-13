from src.main import main


def test_main_good():
    assert main() == "Hello from py-nanny!"