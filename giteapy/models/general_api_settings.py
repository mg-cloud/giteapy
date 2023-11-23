# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.21.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from giteapy.configuration import Configuration


class GeneralAPISettings(object):
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
        'default_git_trees_per_page': 'int',
        'default_max_blob_size': 'int',
        'default_paging_num': 'int',
        'max_response_items': 'int'
    }

    attribute_map = {
        'default_git_trees_per_page': 'default_git_trees_per_page',
        'default_max_blob_size': 'default_max_blob_size',
        'default_paging_num': 'default_paging_num',
        'max_response_items': 'max_response_items'
    }

    def __init__(self, default_git_trees_per_page=None, default_max_blob_size=None, default_paging_num=None, max_response_items=None, _configuration=None):  # noqa: E501
        """GeneralAPISettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._default_git_trees_per_page = None
        self._default_max_blob_size = None
        self._default_paging_num = None
        self._max_response_items = None
        self.discriminator = None

        if default_git_trees_per_page is not None:
            self.default_git_trees_per_page = default_git_trees_per_page
        if default_max_blob_size is not None:
            self.default_max_blob_size = default_max_blob_size
        if default_paging_num is not None:
            self.default_paging_num = default_paging_num
        if max_response_items is not None:
            self.max_response_items = max_response_items

    @property
    def default_git_trees_per_page(self):
        """Gets the default_git_trees_per_page of this GeneralAPISettings.  # noqa: E501


        :return: The default_git_trees_per_page of this GeneralAPISettings.  # noqa: E501
        :rtype: int
        """
        return self._default_git_trees_per_page

    @default_git_trees_per_page.setter
    def default_git_trees_per_page(self, default_git_trees_per_page):
        """Sets the default_git_trees_per_page of this GeneralAPISettings.


        :param default_git_trees_per_page: The default_git_trees_per_page of this GeneralAPISettings.  # noqa: E501
        :type: int
        """

        self._default_git_trees_per_page = default_git_trees_per_page

    @property
    def default_max_blob_size(self):
        """Gets the default_max_blob_size of this GeneralAPISettings.  # noqa: E501


        :return: The default_max_blob_size of this GeneralAPISettings.  # noqa: E501
        :rtype: int
        """
        return self._default_max_blob_size

    @default_max_blob_size.setter
    def default_max_blob_size(self, default_max_blob_size):
        """Sets the default_max_blob_size of this GeneralAPISettings.


        :param default_max_blob_size: The default_max_blob_size of this GeneralAPISettings.  # noqa: E501
        :type: int
        """

        self._default_max_blob_size = default_max_blob_size

    @property
    def default_paging_num(self):
        """Gets the default_paging_num of this GeneralAPISettings.  # noqa: E501


        :return: The default_paging_num of this GeneralAPISettings.  # noqa: E501
        :rtype: int
        """
        return self._default_paging_num

    @default_paging_num.setter
    def default_paging_num(self, default_paging_num):
        """Sets the default_paging_num of this GeneralAPISettings.


        :param default_paging_num: The default_paging_num of this GeneralAPISettings.  # noqa: E501
        :type: int
        """

        self._default_paging_num = default_paging_num

    @property
    def max_response_items(self):
        """Gets the max_response_items of this GeneralAPISettings.  # noqa: E501


        :return: The max_response_items of this GeneralAPISettings.  # noqa: E501
        :rtype: int
        """
        return self._max_response_items

    @max_response_items.setter
    def max_response_items(self, max_response_items):
        """Sets the max_response_items of this GeneralAPISettings.


        :param max_response_items: The max_response_items of this GeneralAPISettings.  # noqa: E501
        :type: int
        """

        self._max_response_items = max_response_items

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
        if issubclass(GeneralAPISettings, dict):
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
        if not isinstance(other, GeneralAPISettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GeneralAPISettings):
            return True

        return self.to_dict() != other.to_dict()
