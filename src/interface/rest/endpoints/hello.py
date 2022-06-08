from fastapi import APIRouter

hello_router = APIRouter(
    responses={
        400: {'description': 'Something went wrong'},
        401: {'description': 'Need authentication'},
        403: {'description': 'Not enough privileges'},
        500: {'description': 'Something went wrong'},
        502: {'description': 'Technical work in progress'},
    },
)


@hello_router.get(
    '/hello',
)
def hello_view():
    """Greeting view, for test.

    Returns:
        Hello string
    """
    return 'Hello4'
