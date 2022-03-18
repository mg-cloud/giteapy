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


class CreateIssueOption(object):
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
        'assignee': 'str',
        'assignees': 'list[str]',
        'body': 'str',
        'closed': 'bool',
        'due_date': 'datetime',
        'labels': 'list[int]',
        'milestone': 'int',
        'ref': 'str',
        'title': 'str'
    }

    attribute_map = {
        'assignee': 'assignee',
        'assignees': 'assignees',
        'body': 'body',
        'closed': 'closed',
        'due_date': 'due_date',
        'labels': 'labels',
        'milestone': 'milestone',
        'ref': 'ref',
        'title': 'title'
    }

    def __init__(self, assignee=None, assignees=None, body=None, closed=None, due_date=None, labels=None, milestone=None, ref=None, title=None, _configuration=None):  # noqa: E501
        """CreateIssueOption - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._assignee = None
        self._assignees = None
        self._body = None
        self._closed = None
        self._due_date = None
        self._labels = None
        self._milestone = None
        self._ref = None
        self._title = None
        self.discriminator = None

        if assignee is not None:
            self.assignee = assignee
        if assignees is not None:
            self.assignees = assignees
        if body is not None:
            self.body = body
        if closed is not None:
            self.closed = closed
        if due_date is not None:
            self.due_date = due_date
        if labels is not None:
            self.labels = labels
        if milestone is not None:
            self.milestone = milestone
        if ref is not None:
            self.ref = ref
        self.title = title

    @property
    def assignee(self):
        """Gets the assignee of this CreateIssueOption.  # noqa: E501

        deprecated  # noqa: E501

        :return: The assignee of this CreateIssueOption.  # noqa: E501
        :rtype: str
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        """Sets the assignee of this CreateIssueOption.

        deprecated  # noqa: E501

        :param assignee: The assignee of this CreateIssueOption.  # noqa: E501
        :type: str
        """

        self._assignee = assignee

    @property
    def assignees(self):
        """Gets the assignees of this CreateIssueOption.  # noqa: E501


        :return: The assignees of this CreateIssueOption.  # noqa: E501
        :rtype: list[str]
        """
        return self._assignees

    @assignees.setter
    def assignees(self, assignees):
        """Sets the assignees of this CreateIssueOption.


        :param assignees: The assignees of this CreateIssueOption.  # noqa: E501
        :type: list[str]
        """

        self._assignees = assignees

    @property
    def body(self):
        """Gets the body of this CreateIssueOption.  # noqa: E501


        :return: The body of this CreateIssueOption.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateIssueOption.


        :param body: The body of this CreateIssueOption.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def closed(self):
        """Gets the closed of this CreateIssueOption.  # noqa: E501


        :return: The closed of this CreateIssueOption.  # noqa: E501
        :rtype: bool
        """
        return self._closed

    @closed.setter
    def closed(self, closed):
        """Sets the closed of this CreateIssueOption.


        :param closed: The closed of this CreateIssueOption.  # noqa: E501
        :type: bool
        """

        self._closed = closed

    @property
    def due_date(self):
        """Gets the due_date of this CreateIssueOption.  # noqa: E501


        :return: The due_date of this CreateIssueOption.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this CreateIssueOption.


        :param due_date: The due_date of this CreateIssueOption.  # noqa: E501
        :type: datetime
        """

        self._due_date = due_date

    @property
    def labels(self):
        """Gets the labels of this CreateIssueOption.  # noqa: E501

        list of label ids  # noqa: E501

        :return: The labels of this CreateIssueOption.  # noqa: E501
        :rtype: list[int]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this CreateIssueOption.

        list of label ids  # noqa: E501

        :param labels: The labels of this CreateIssueOption.  # noqa: E501
        :type: list[int]
        """

        self._labels = labels

    @property
    def milestone(self):
        """Gets the milestone of this CreateIssueOption.  # noqa: E501

        milestone id  # noqa: E501

        :return: The milestone of this CreateIssueOption.  # noqa: E501
        :rtype: int
        """
        return self._milestone

    @milestone.setter
    def milestone(self, milestone):
        """Sets the milestone of this CreateIssueOption.

        milestone id  # noqa: E501

        :param milestone: The milestone of this CreateIssueOption.  # noqa: E501
        :type: int
        """

        self._milestone = milestone

    @property
    def ref(self):
        """Gets the ref of this CreateIssueOption.  # noqa: E501


        :return: The ref of this CreateIssueOption.  # noqa: E501
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this CreateIssueOption.


        :param ref: The ref of this CreateIssueOption.  # noqa: E501
        :type: str
        """

        self._ref = ref

    @property
    def title(self):
        """Gets the title of this CreateIssueOption.  # noqa: E501


        :return: The title of this CreateIssueOption.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CreateIssueOption.


        :param title: The title of this CreateIssueOption.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

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
        if issubclass(CreateIssueOption, dict):
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
        if not isinstance(other, CreateIssueOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateIssueOption):
            return True

        return self.to_dict() != other.to_dict()
