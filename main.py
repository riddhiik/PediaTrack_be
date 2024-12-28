from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
import apis as router
# Configure allowed origins
origins = ["http://localhost", "http://localhost:3000"]

description = """
Test Project
"""

# Initialize FastAPI app
app = FastAPI(
    title="My Project",
    docs_url="/",  # Set Swagger UI docs endpoint
    redoc_url=None,
    description=description,
    version="0.0.1",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom OpenAPI schema
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Project APIs",
        version="0.1.0",
        description="Riddhi's API",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

app.include_router(router.route)