from threading import Thread
import pytest
from app import create_app


@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.config["TESTING"] = True
    yield app


@pytest.fixture(scope="session")
def server(app):
    def start_flask_server():
        app.run()

    # Start the Flask server in a separate thread
    thread = Thread(target=start_flask_server)
    thread.daemon = True
    thread.start()

    # Wait for the server to start
    # Add any necessary additional wait time or checks here
    # For simplicity, we'll use a static wait time in this example
    import time
    time.sleep(2)
