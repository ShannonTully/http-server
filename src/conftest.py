from . import server
import pytest
# from multiprocessing import Process
from threading import Thread


@pytest.fixture(scope='module', autouse=True)
def server_setup():
    instance = server.create_server()
    # process = Process(target=instance.serve_forever)

    process = Thread(target=instance.serve_forever)
    process.setDaemon(True)

    process.start()
