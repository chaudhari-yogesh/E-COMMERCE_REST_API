from rest_framework.response import Response
from datetime import datetime, timedelta


def http_response(
        response_serializer_class=None,
        details: object = {},
        errors: list = [],
        ex_errors=None,
        **kwargs,
):
    if len(errors) <= 0:
        return Response(
            data=response_serializer_class(
                {
                    "details": details,
                    "errors": errors,
                    "status": kwargs.get("status", 200),
                    "timestamp": datetime.utcnow().isoformat() + "Z",
                }
            ).data,
            **kwargs
        )

    return Response(
        data=response_serializer_class(
            {
                "details": {},
                "errors": errors,
                "error_stack_trace": str(ex_errors) if ex_errors else None,
                "status": kwargs.get("status", 400),
                "timestamp": datetime.utcnow().isoformat() + "Z",
            }
        )
    )
