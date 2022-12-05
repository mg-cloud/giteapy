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


class PRBranchInfo(object):
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
        'label': 'str',
        'ref': 'str',
        'repo': 'Repository',
        'repo_id': 'int',
        'sha': 'str'
    }

    attribute_map = {
        'label': 'label',
        'ref': 'ref',
        'repo': 'repo',
        'repo_id': 'repo_id',
        'sha': 'sha'
    }

    def __init__(self, label=None, ref=None, repo=None, repo_id=None, sha=None, _configuration=None):  # noqa: E501
        """PRBranchInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._label = None
        self._ref = None
        self._repo = None
        self._repo_id = None
        self._sha = None
        self.discriminator = None

        if label is not None:
            self.label = label
        if ref is not None:
            self.ref = ref
        if repo is not None:
            self.repo = repo
        if repo_id is not None:
            self.repo_id = repo_id
        if sha is not None:
            self.sha = sha

    @property
    def label(self):
        """Gets the label of this PRBranchInfo.  # noqa: E501


        :return: The label of this PRBranchInfo.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this PRBranchInfo.


        :param label: The label of this PRBranchInfo.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def ref(self):
        """Gets the ref of this PRBranchInfo.  # noqa: E501


        :return: The ref of this PRBranchInfo.  # noqa: E501
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this PRBranchInfo.


        :param ref: The ref of this PRBranchInfo.  # noqa: E501
        :type: str
        """

        self._ref = ref

    @property
    def repo(self):
        """Gets the repo of this PRBranchInfo.  # noqa: E501


        :return: The repo of this PRBranchInfo.  # noqa: E501
        :rtype: Repository
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """Sets the repo of this PRBranchInfo.


        :param repo: The repo of this PRBranchInfo.  # noqa: E501
        :type: Repository
        """

        self._repo = repo

    @property
    def repo_id(self):
        """Gets the repo_id of this PRBranchInfo.  # noqa: E501


        :return: The repo_id of this PRBranchInfo.  # noqa: E501
        :rtype: int
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        """Sets the repo_id of this PRBranchInfo.


        :param repo_id: The repo_id of this PRBranchInfo.  # noqa: E501
        :type: int
        """

        self._repo_id = repo_id

    @property
    def sha(self):
        """Gets the sha of this PRBranchInfo.  # noqa: E501


        :return: The sha of this PRBranchInfo.  # noqa: E501
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this PRBranchInfo.


        :param sha: The sha of this PRBranchInfo.  # noqa: E501
        :type: str
        """

        self._sha = sha

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
        if issubclass(PRBranchInfo, dict):
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
        if not isinstance(other, PRBranchInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PRBranchInfo):
            return True

        return self.to_dict() != other.to_dict()
