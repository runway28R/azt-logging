import importlib

from azt_logging import create_logger


def test_create_logger_is_publicly_available():
    create_logger_module = importlib.import_module("azt_logging.create_logger")

    assert create_logger is create_logger_module.create_logger


def test_create_logger_returns_configured_logger(monkeypatch):
    create_logger_module = importlib.import_module("azt_logging.create_logger")

    fake_logger = object()

    class FakeAzureLogger:
        def get_logger(self):
            return fake_logger

    def fake_table_logger_factory(
        st_account_name, account_key, table_name, log_level
    ):
        assert st_account_name == "account"
        assert account_key == "key"
        assert table_name == "logs"
        assert log_level == 10
        return FakeAzureLogger()

    monkeypatch.setattr(
        create_logger_module,
        "table_logger",
        fake_table_logger_factory,
    )

    result = create_logger(
        st_account_name="account",
        account_key="key",
        table_name="logs",
        log_level=10,
    )

    assert result is fake_logger
