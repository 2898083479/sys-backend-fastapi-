from fastapi import APIRouter

from app.forms.account.common import *
from app.response import ResponseModel
from app.response.common import LoginSuccessResponse
from app.view_models.account.common import *

router = APIRouter(
    prefix='/common', tags=['Account common API'], dependencies=[]
)


@router.get(
    '/login',
    response_model=ResponseModel[LoginSuccessResponse | str],
    description='User login'
)
async def login(
        form_data: LoginForm
):
    async with AdminLoginViewModel(form_data) as response:
        return response


@router.post(
    '/register',
    response_model=ResponseModel[str],
    description='User register'
)
async def register(
    form_data: RegisterForm
):
    async with AdminRegisterViewModel(form_data) as response:
        return response
