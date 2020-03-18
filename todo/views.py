from modernrpc.auth.basic import http_basic_auth_login_required
from modernrpc.core import rpc_method


@rpc_method
@http_basic_auth_login_required
def add(a: int, b: int) -> int:
    """
    Calculates sum.
    :param a: - First addend
    :param b: - Second addend
    :return: Result
    """
    return a + b
