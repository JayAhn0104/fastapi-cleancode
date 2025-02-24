from typing import Annotated
from dependency_injector.wiring import inject, Provide
from containers import Container
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from user.application.user_service import UserService

router = APIRouter(prefix="/users")


class CreateUserBody(BaseModel):
    name: str
    email: str
    password: str


@router.post("", status_code=201)
@inject
def create_user(
    user: CreateUserBody,
    # user_service: Annotated[UserService, Depends(UserService)]
    # user_service: UserService = Depends(Provide[Container.user_service])
    user_service: Annotated[UserService, Depends(lambda: Container().user_service())]
    ):
    # user_service = UserService()
    created_user = user_service.create_user(
        name=user.name,
        email=user.email,
        password=user.password
    )
    return created_user