# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.17.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from giteapy.configuration import Configuration


class Reaction(object):
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
        'content': 'str',
        'created_at': 'datetime',
        'user': 'User'
    }

    attribute_map = {
        'content': 'content',
        'created_at': 'created_at',
        'user': 'user'
    }

    def __init__(self, content=None, created_at=None, user=None, _configuration=None):  # noqa: E501
        """Reaction - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._content = None
        self._created_at = None
        self._user = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if created_at is not None:
            self.created_at = created_at
        if user is not None:
            self.user = user

    @property
    def content(self):
        """Gets the content of this Reaction.  # noqa: E501


        :return: The content of this Reaction.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Reaction.


        :param content: The content of this Reaction.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def created_at(self):
        """Gets the created_at of this Reaction.  # noqa: E501


        :return: The created_at of this Reaction.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Reaction.


        :param created_at: The created_at of this Reaction.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def user(self):
        """Gets the user of this Reaction.  # noqa: E501


        :return: The user of this Reaction.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Reaction.


        :param user: The user of this Reaction.  # noqa: E501
        :type: User
        """

        self._user = user

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
        if issubclass(Reaction, dict):
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
        if not isinstance(other, Reaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Reaction):
            return True

        return self.to_dict() != other.to_dict()
