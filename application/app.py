"""
Module define fastapi server configuration
"""

from fastapi import FastAPI
from hypercorn.asyncio import serve
from hypercorn.config import Config as HyperCornConfig
from prometheus_client import Counter

app = FastAPI()

REQUESTS = Counter('server_requests_total', 'Total number of requests to this webserver')
HEALTHCHECK_REQUESTS = Counter('healthcheck_requests_total', 'Total number of requests to healthcheck')
MAIN_ENDPOINT_REQUESTS = Counter('main_requests_total', 'Total number of requests to main endpoint')

class TestApp:
    """
    TestApp class define FastAPI configuration and implemented endpoints
    """

    _hypercorn_config = None

    def __init__(self):
        self._hypercorn_config = HyperCornConfig()

    async def run_server(self):
        """Starts the server with the config parameters"""
        self._hypercorn_config.bind = ['0.0.0.0:8081']
        self._hypercorn_config.keep_alive_timeout = 90
        await serve(app, self._hypercorn_config)

    @app.get("/health")
    async def health_check():
        """Implement health check endpoint"""
        # Increment counter used for register the total number of calls in the webserver
        REQUESTS.inc()
        # Increment counter used for register the requests to healtcheck endpoint
        HEALTHCHECK_REQUESTS.inc()
        return {"health": "ok"}

    @app.get("/")
    async def read_main():
        """Implement main endpoint"""
        # Increment counter used to register the total number of calls in the webserver
        REQUESTS.inc()
        # Increment counter used tor register the total number of calls in the main endpoint
        MAIN_ENDPOINT_REQUESTS.inc()
        return {"msg": "App ok"}
    
    @app.get("/buy")
    async def read_main():
        """Implement practise endpoint"""
        # Increment counter used to register the total number of calls in the webserver
        REQUESTS.inc()
        # Increment counter used to register the total number of calls in the buy endpoint
        BUY_ENDPOINT_REQUESTS.inc()
        return {"msg": "buy endpoint"}

    @app.get("/history")
    async def read_main():
        """Implement history endpoint"""
        # Increment counter used to register the total number of calls in the webserver
        REQUESTS.inc()
        # Increment counter used to register the total number of calls in the history endpoint
        HISTORY_ENDPOINT_REQUESTS.inc()
        return {"msg": "history endpoint"}
		
	@app.get("/quote")
    async def read_main():
        """Implement quote endpoint"""
        # Increment counter used to register the total number of calls in the webserver
        REQUESTS.inc()
        # Increment counter used to register the total number of calls in the quote endpoint
        QUOTE_ENDPOINT_REQUESTS.inc()
        return {"msg": "quote endpoint OK"}
		
	@app.get("/register")
    async def read_main():
        """Implement register endpoint"""
        # Increment counter used to register the total number of calls in the webserver
        REQUESTS.inc()
        # Increment counter used to register the total number of calls in the register endpoint
        REGISTER_ENDPOINT_REQUESTS.inc()
        return {"msg": "register endpoint OK"}
		
	@app.get("/sell")
    async def read_main():
        """Implement sell endpoint"""
        # Increment counter used to register the total number of calls in the webserver
        REQUESTS.inc()
        # Increment counter used to register the total number of calls in the sell endpoint
        SELL_ENDPOINT_REQUESTS.inc()
        return {"msg": "sell endpoint OK"}
		
	@app.get("/login")
    async def read_main():
        """Implement login endpoint"""
        # Increment counter used to register the total number of calls in the webserver
        REQUESTS.inc()
        # Increment counter used to register the total number of calls in the login endpoint
        LOGIN_ENDPOINT_REQUESTS.inc()
        return {"msg": "login endpoint OK"}
		
	@app.get("/logout")
    async def read_main():
        """Implement logout endpoint"""
        # Increment counter used to register the total number of calls in the webserver
        REQUESTS.inc()
        # Increment counter used to register the total number of calls in the logout endpoint
        LOGOUT_ENDPOINT_REQUESTS.inc()
        return {"msg": "logout endpoint OK"}
