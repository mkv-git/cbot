SQL_WORKER_PORT = 7000
WS_PUBLISHER_PORT = 7010
INPROC_BACKEND_ADDR = "inproc://backend"

LOGGING_FILE_ROOT_DIR = "/home/maksim/repos/cbot/cbot/logs"
DEFAULT_LOGGING_FILE_CONFIG = {
    "level": "DEBUG",
    "rotation": "00:00",
    "compression": "tar.gz",
    "retention": 7,
    "diagnose": False,
}
DEFAULT_WS_REQUEST_RETRIES = 5
DEFAULT_WS_REQUEST_TIMEOUT = 3000
