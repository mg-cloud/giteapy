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


class EditOrgOption(object):
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
        'description': 'str',
        'full_name': 'str',
        'location': 'str',
        'repo_admin_change_team_access': 'bool',
        'visibility': 'str',
        'website': 'str'
    }

    attribute_map = {
        'description': 'description',
        'full_name': 'full_name',
        'location': 'location',
        'repo_admin_change_team_access': 'repo_admin_change_team_access',
        'visibility': 'visibility',
        'website': 'website'
    }

    def __init__(self, description=None, full_name=None, location=None, repo_admin_change_team_access=None, visibility=None, website=None, _configuration=None):  # noqa: E501
        """EditOrgOption - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._full_name = None
        self._location = None
        self._repo_admin_change_team_access = None
        self._visibility = None
        self._website = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if full_name is not None:
            self.full_name = full_name
        if location is not None:
            self.location = location
        if repo_admin_change_team_access is not None:
            self.repo_admin_change_team_access = repo_admin_change_team_access
        if visibility is not None:
            self.visibility = visibility
        if website is not None:
            self.website = website

    @property
    def description(self):
        """Gets the description of this EditOrgOption.  # noqa: E501


        :return: The description of this EditOrgOption.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EditOrgOption.


        :param description: The description of this EditOrgOption.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def full_name(self):
        """Gets the full_name of this EditOrgOption.  # noqa: E501


        :return: The full_name of this EditOrgOption.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this EditOrgOption.


        :param full_name: The full_name of this EditOrgOption.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def location(self):
        """Gets the location of this EditOrgOption.  # noqa: E501


        :return: The location of this EditOrgOption.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this EditOrgOption.


        :param location: The location of this EditOrgOption.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def repo_admin_change_team_access(self):
        """Gets the repo_admin_change_team_access of this EditOrgOption.  # noqa: E501


        :return: The repo_admin_change_team_access of this EditOrgOption.  # noqa: E501
        :rtype: bool
        """
        return self._repo_admin_change_team_access

    @repo_admin_change_team_access.setter
    def repo_admin_change_team_access(self, repo_admin_change_team_access):
        """Sets the repo_admin_change_team_access of this EditOrgOption.


        :param repo_admin_change_team_access: The repo_admin_change_team_access of this EditOrgOption.  # noqa: E501
        :type: bool
        """

        self._repo_admin_change_team_access = repo_admin_change_team_access

    @property
    def visibility(self):
        """Gets the visibility of this EditOrgOption.  # noqa: E501

        possible values are `public`, `limited` or `private`  # noqa: E501

        :return: The visibility of this EditOrgOption.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this EditOrgOption.

        possible values are `public`, `limited` or `private`  # noqa: E501

        :param visibility: The visibility of this EditOrgOption.  # noqa: E501
        :type: str
        """
        allowed_values = ["public", "limited", "private"]  # noqa: E501
        if (self._configuration.client_side_validation and
                visibility not in allowed_values):
            raise ValueError(
                "Invalid value for `visibility` ({0}), must be one of {1}"  # noqa: E501
                .format(visibility, allowed_values)
            )

        self._visibility = visibility

    @property
    def website(self):
        """Gets the website of this EditOrgOption.  # noqa: E501


        :return: The website of this EditOrgOption.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this EditOrgOption.


        :param website: The website of this EditOrgOption.  # noqa: E501
        :type: str
        """

        self._website = website

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
        if issubclass(EditOrgOption, dict):
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
        if not isinstance(other, EditOrgOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EditOrgOption):
            return True

        return self.to_dict() != other.to_dict()
