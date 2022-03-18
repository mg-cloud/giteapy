# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.16.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from giteapy.configuration import Configuration


class NodeInfoUsageUsers(object):
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
        'active_halfyear': 'int',
        'active_month': 'int',
        'total': 'int'
    }

    attribute_map = {
        'active_halfyear': 'activeHalfyear',
        'active_month': 'activeMonth',
        'total': 'total'
    }

    def __init__(self, active_halfyear=None, active_month=None, total=None, _configuration=None):  # noqa: E501
        """NodeInfoUsageUsers - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active_halfyear = None
        self._active_month = None
        self._total = None
        self.discriminator = None

        if active_halfyear is not None:
            self.active_halfyear = active_halfyear
        if active_month is not None:
            self.active_month = active_month
        if total is not None:
            self.total = total

    @property
    def active_halfyear(self):
        """Gets the active_halfyear of this NodeInfoUsageUsers.  # noqa: E501


        :return: The active_halfyear of this NodeInfoUsageUsers.  # noqa: E501
        :rtype: int
        """
        return self._active_halfyear

    @active_halfyear.setter
    def active_halfyear(self, active_halfyear):
        """Sets the active_halfyear of this NodeInfoUsageUsers.


        :param active_halfyear: The active_halfyear of this NodeInfoUsageUsers.  # noqa: E501
        :type: int
        """

        self._active_halfyear = active_halfyear

    @property
    def active_month(self):
        """Gets the active_month of this NodeInfoUsageUsers.  # noqa: E501


        :return: The active_month of this NodeInfoUsageUsers.  # noqa: E501
        :rtype: int
        """
        return self._active_month

    @active_month.setter
    def active_month(self, active_month):
        """Sets the active_month of this NodeInfoUsageUsers.


        :param active_month: The active_month of this NodeInfoUsageUsers.  # noqa: E501
        :type: int
        """

        self._active_month = active_month

    @property
    def total(self):
        """Gets the total of this NodeInfoUsageUsers.  # noqa: E501


        :return: The total of this NodeInfoUsageUsers.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this NodeInfoUsageUsers.


        :param total: The total of this NodeInfoUsageUsers.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(NodeInfoUsageUsers, dict):
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
        if not isinstance(other, NodeInfoUsageUsers):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NodeInfoUsageUsers):
            return True

        return self.to_dict() != other.to_dict()
