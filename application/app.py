"""
Module define flask server configuration
"""

from flask import Flask
from flask_restful import Api, Resource
from hypercorn.asyncio import serve
from hypercorn.config import Config as HyperCornConfig
from prometheus_client import Counter

app = Flask(__name__)
api = Api(app)

REQUESTS = Counter('server_requests_total', 'Total number of requests to this webserver')
HEALTHCHECK_REQUESTS = Counter('healthcheck_requests_total', 'Total number of requests to healthcheck')
MAIN_ENDPOINT_REQUESTS = Counter('main_requests_total', 'Total number of requests to main endpoint')
REGISTER_ENDPOINT_REQUESTS = Counter('register_requests_total', 'Total number of requests to register endpoint')
LOGIN_ENDPOINT_REQUESTS = Counter('login_requests_total', 'Total number of requests to login endpoint')
LOGOUT_ENDPOINT_REQUESTS = Counter('logout_requests_total', 'Total number of requests to logout endpoint')
BUY_ENDPOINT_REQUESTS = Counter('buy_requests_total', 'Total number of requests to buy endpoint')
SELL_ENDPOINT_REQUESTS = Counter('sell_requests_total', 'Total number of requests to sell endpoint')


class App:
    """
    App class define flask configuration and implemented endpoints
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
        # Increment counter used for register the total number of calls in the webserver
        REQUESTS.inc()
        # Increment counter used for register the total number of calls in the main endpoint
        MAIN_ENDPOINT_REQUESTS.inc()
        
    
    @app.get("/register")
    async def read_register():
        """Implement register endpoint"""
        # Increment counter used for register the total number of calls in the webserver
        REQUESTS.inc()
        # Increment counter used for register the total number of calls in the registration endpoint
        REGISTER_ENDPOINT_REQUESTS.inc()
    
    @app.get("/login")
    async def read_login():
        """Implement login endpoint"""
        # Increment counter used for register the total number of calls in the webserver
        REQUESTS.inc()
        # Increment counter used for register the total number of calls in the login endpoint
        LOGIN_ENDPOINT_REQUESTS.inc()
        
    @app.get("/logout")
    async def read_logout():
        """Implement logout endpoint"""
        # Increment counter used for register the total number of calls in the webserver
        REQUESTS.inc()
        # Increment counter used for register the total number of calls in the login endpoint
        LOGOUT_ENDPOINT_REQUESTS.inc()
    
@app.get("/buy")
    async def read_buy():
        """Implement buy endpoint"""
        # Increment counter used for register the total number of calls in the webserver
        REQUESTS.inc()
        # Increment counter used for register the total number of calls in the buy endpoint
        BUY_ENDPOINT_REQUESTS.inc()    
    
@app.get("/sell")
    async def read_sell():
        """Implement sell endpoint"""
        # Increment counter used for register the total number of calls in the webserver
        REQUESTS.inc()
        # Increment counter used for register the total number of calls in the sell endpoint
        SELL_ENDPOINT_REQUESTS.inc()    
