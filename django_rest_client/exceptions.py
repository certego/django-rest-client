import json
from typing import Optional, Union, Dict, Any
from requests.exceptions import RequestException


class APIClientException(RequestException):
    @property
    def error_detail(self) -> Optional[Union[Dict, Any]]:
        content = None
        try:
            content = self.response.json()
            detail = content.get("detail", None)
            if detail:
                content = detail
        except json.JSONDecodeError:
            content = self.response.content
        except Exception:
            pass

        return content

    def __str__(self):
        err_msg = super().__str__()
        detail = self.error_detail
        return err_msg + f"\n[Details: {detail}]"
