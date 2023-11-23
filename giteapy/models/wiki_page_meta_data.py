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


class WikiPageMetaData(object):
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
        'html_url': 'str',
        'last_commit': 'WikiCommit',
        'sub_url': 'str',
        'title': 'str'
    }

    attribute_map = {
        'html_url': 'html_url',
        'last_commit': 'last_commit',
        'sub_url': 'sub_url',
        'title': 'title'
    }

    def __init__(self, html_url=None, last_commit=None, sub_url=None, title=None, _configuration=None):  # noqa: E501
        """WikiPageMetaData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._html_url = None
        self._last_commit = None
        self._sub_url = None
        self._title = None
        self.discriminator = None

        if html_url is not None:
            self.html_url = html_url
        if last_commit is not None:
            self.last_commit = last_commit
        if sub_url is not None:
            self.sub_url = sub_url
        if title is not None:
            self.title = title

    @property
    def html_url(self):
        """Gets the html_url of this WikiPageMetaData.  # noqa: E501


        :return: The html_url of this WikiPageMetaData.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this WikiPageMetaData.


        :param html_url: The html_url of this WikiPageMetaData.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def last_commit(self):
        """Gets the last_commit of this WikiPageMetaData.  # noqa: E501


        :return: The last_commit of this WikiPageMetaData.  # noqa: E501
        :rtype: WikiCommit
        """
        return self._last_commit

    @last_commit.setter
    def last_commit(self, last_commit):
        """Sets the last_commit of this WikiPageMetaData.


        :param last_commit: The last_commit of this WikiPageMetaData.  # noqa: E501
        :type: WikiCommit
        """

        self._last_commit = last_commit

    @property
    def sub_url(self):
        """Gets the sub_url of this WikiPageMetaData.  # noqa: E501


        :return: The sub_url of this WikiPageMetaData.  # noqa: E501
        :rtype: str
        """
        return self._sub_url

    @sub_url.setter
    def sub_url(self, sub_url):
        """Sets the sub_url of this WikiPageMetaData.


        :param sub_url: The sub_url of this WikiPageMetaData.  # noqa: E501
        :type: str
        """

        self._sub_url = sub_url

    @property
    def title(self):
        """Gets the title of this WikiPageMetaData.  # noqa: E501


        :return: The title of this WikiPageMetaData.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this WikiPageMetaData.


        :param title: The title of this WikiPageMetaData.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(WikiPageMetaData, dict):
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
        if not isinstance(other, WikiPageMetaData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WikiPageMetaData):
            return True

        return self.to_dict() != other.to_dict()
