# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.20.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from giteapy.configuration import Configuration


class Hook(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'active': 'bool',
        'authorization_header': 'str',
        'config': 'dict(str, str)',
        'created_at': 'datetime',
        'events': 'list[str]',
        'id': 'int',
        'type': 'str',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'active': 'active',
        'authorization_header': 'authorization_header',
        'config': 'config',
        'created_at': 'created_at',
        'events': 'events',
        'id': 'id',
        'type': 'type',
        'updated_at': 'updated_at'
    }

    def __init__(self, active=None, authorization_header=None, config=None, created_at=None, events=None, id=None, type=None, updated_at=None, _configuration=None):  # noqa: E501
        """Hook - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active = None
        self._authorization_header = None
        self._config = None
        self._created_at = None
        self._events = None
        self._id = None
        self._type = None
        self._updated_at = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if authorization_header is not None:
            self.authorization_header = authorization_header
        if config is not None:
            self.config = config
        if created_at is not None:
            self.created_at = created_at
        if events is not None:
            self.events = events
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def active(self):
        """Gets the active of this Hook.  # noqa: E501


        :return: The active of this Hook.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Hook.


        :param active: The active of this Hook.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def authorization_header(self):
        """Gets the authorization_header of this Hook.  # noqa: E501


        :return: The authorization_header of this Hook.  # noqa: E501
        :rtype: str
        """
        return self._authorization_header

    @authorization_header.setter
    def authorization_header(self, authorization_header):
        """Sets the authorization_header of this Hook.


        :param authorization_header: The authorization_header of this Hook.  # noqa: E501
        :type: str
        """

        self._authorization_header = authorization_header

    @property
    def config(self):
        """Gets the config of this Hook.  # noqa: E501


        :return: The config of this Hook.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this Hook.


        :param config: The config of this Hook.  # noqa: E501
        :type: dict(str, str)
        """

        self._config = config

    @property
    def created_at(self):
        """Gets the created_at of this Hook.  # noqa: E501


        :return: The created_at of this Hook.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Hook.


        :param created_at: The created_at of this Hook.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def events(self):
        """Gets the events of this Hook.  # noqa: E501


        :return: The events of this Hook.  # noqa: E501
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this Hook.


        :param events: The events of this Hook.  # noqa: E501
        :type: list[str]
        """

        self._events = events

    @property
    def id(self):
        """Gets the id of this Hook.  # noqa: E501


        :return: The id of this Hook.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Hook.


        :param id: The id of this Hook.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Hook.  # noqa: E501


        :return: The type of this Hook.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Hook.


        :param type: The type of this Hook.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this Hook.  # noqa: E501


        :return: The updated_at of this Hook.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Hook.


        :param updated_at: The updated_at of this Hook.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Hook, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Hook):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Hook):
            return True

        return self.to_dict() != other.to_dict()
