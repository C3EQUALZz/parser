from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import status
from starlette.responses import RedirectResponse

from app.application.api.product_marketplace.wildberries.handlers import router as wildberries_router

app = FastAPI(
    title='Complex Parser',
    version='1.0.0',
    root_path="/api",
    debug=True,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin",
                   "Authorization"]
)

app.include_router(wildberries_router)

@app.get(
    path="/",
    response_class=RedirectResponse,
    status_code=status.HTTP_303_SEE_OTHER
)
async def homepage():
    return RedirectResponse(
        status_code=status.HTTP_303_SEE_OTHER,
        url="/docs"
    )