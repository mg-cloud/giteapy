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


class CreatePullReviewOptions(object):
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
        'body': 'str',
        'comments': 'list[CreatePullReviewComment]',
        'commit_id': 'str',
        'event': 'ReviewStateType'
    }

    attribute_map = {
        'body': 'body',
        'comments': 'comments',
        'commit_id': 'commit_id',
        'event': 'event'
    }

    def __init__(self, body=None, comments=None, commit_id=None, event=None, _configuration=None):  # noqa: E501
        """CreatePullReviewOptions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._body = None
        self._comments = None
        self._commit_id = None
        self._event = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if comments is not None:
            self.comments = comments
        if commit_id is not None:
            self.commit_id = commit_id
        if event is not None:
            self.event = event

    @property
    def body(self):
        """Gets the body of this CreatePullReviewOptions.  # noqa: E501


        :return: The body of this CreatePullReviewOptions.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreatePullReviewOptions.


        :param body: The body of this CreatePullReviewOptions.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def comments(self):
        """Gets the comments of this CreatePullReviewOptions.  # noqa: E501


        :return: The comments of this CreatePullReviewOptions.  # noqa: E501
        :rtype: list[CreatePullReviewComment]
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this CreatePullReviewOptions.


        :param comments: The comments of this CreatePullReviewOptions.  # noqa: E501
        :type: list[CreatePullReviewComment]
        """

        self._comments = comments

    @property
    def commit_id(self):
        """Gets the commit_id of this CreatePullReviewOptions.  # noqa: E501


        :return: The commit_id of this CreatePullReviewOptions.  # noqa: E501
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """Sets the commit_id of this CreatePullReviewOptions.


        :param commit_id: The commit_id of this CreatePullReviewOptions.  # noqa: E501
        :type: str
        """

        self._commit_id = commit_id

    @property
    def event(self):
        """Gets the event of this CreatePullReviewOptions.  # noqa: E501


        :return: The event of this CreatePullReviewOptions.  # noqa: E501
        :rtype: ReviewStateType
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this CreatePullReviewOptions.


        :param event: The event of this CreatePullReviewOptions.  # noqa: E501
        :type: ReviewStateType
        """

        self._event = event

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
        if issubclass(CreatePullReviewOptions, dict):
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
        if not isinstance(other, CreatePullReviewOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreatePullReviewOptions):
            return True

        return self.to_dict() != other.to_dict()
