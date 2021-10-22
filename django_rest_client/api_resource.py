from abc import ABCMeta, abstractmethod
from typing import Callable, List

from .types import Toid, TExpandableFields


class APIResource(metaclass=ABCMeta):
    #: is injected during ``APIClient`` initialization.
    #: :meta private:
    _request: Callable

    @property
    @abstractmethod
    def OBJECT_NAME(self) -> str:
        """
        Object name that is used to construct URL string.

        :meta private:
        """
        raise NotImplementedError()

    @property
    @abstractmethod
    def EXPANDABLE_FIELDS(self) -> TExpandableFields:
        """
        Expandable fields
        """
        raise NotImplementedError()

    @property
    @abstractmethod
    def ORDERING_FIELDS(self) -> List[str]:
        """
        Ordering fields.
        """
        raise NotImplementedError()

    @classmethod
    def class_url(cls):
        """
        :meta private:
        """
        if cls == APIResource:
            raise NotImplementedError(
                "APIResource is an abstract class."
                " You should perform actions on its subclasses."
            )
        # Namespaces are separated in object names with periods (.) and in URLs
        # with forward slashes (/), so replace the former with the latter.
        base = cls.OBJECT_NAME.replace(".", "/")
        return base

    @classmethod
    def instance_url(cls, object_id: Toid):
        """
        :meta private:
        """
        if not isinstance(object_id, (str, int)):
            raise RuntimeError(
                "Could not determine which URL to request: %s instance "
                "has invalid ID: %r, %s. ID should be of type `int` or `str`"
                % (type(cls).__name__, object_id, type(id)),
                "id",
            )

        base = cls.class_url()
        return f"{base}/{object_id}"
