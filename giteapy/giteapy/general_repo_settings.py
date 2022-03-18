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


class GeneralRepoSettings(object):
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
        'http_git_disabled': 'bool',
        'lfs_disabled': 'bool',
        'migrations_disabled': 'bool',
        'mirrors_disabled': 'bool',
        'stars_disabled': 'bool',
        'time_tracking_disabled': 'bool'
    }

    attribute_map = {
        'http_git_disabled': 'http_git_disabled',
        'lfs_disabled': 'lfs_disabled',
        'migrations_disabled': 'migrations_disabled',
        'mirrors_disabled': 'mirrors_disabled',
        'stars_disabled': 'stars_disabled',
        'time_tracking_disabled': 'time_tracking_disabled'
    }

    def __init__(self, http_git_disabled=None, lfs_disabled=None, migrations_disabled=None, mirrors_disabled=None, stars_disabled=None, time_tracking_disabled=None, _configuration=None):  # noqa: E501
        """GeneralRepoSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._http_git_disabled = None
        self._lfs_disabled = None
        self._migrations_disabled = None
        self._mirrors_disabled = None
        self._stars_disabled = None
        self._time_tracking_disabled = None
        self.discriminator = None

        if http_git_disabled is not None:
            self.http_git_disabled = http_git_disabled
        if lfs_disabled is not None:
            self.lfs_disabled = lfs_disabled
        if migrations_disabled is not None:
            self.migrations_disabled = migrations_disabled
        if mirrors_disabled is not None:
            self.mirrors_disabled = mirrors_disabled
        if stars_disabled is not None:
            self.stars_disabled = stars_disabled
        if time_tracking_disabled is not None:
            self.time_tracking_disabled = time_tracking_disabled

    @property
    def http_git_disabled(self):
        """Gets the http_git_disabled of this GeneralRepoSettings.  # noqa: E501


        :return: The http_git_disabled of this GeneralRepoSettings.  # noqa: E501
        :rtype: bool
        """
        return self._http_git_disabled

    @http_git_disabled.setter
    def http_git_disabled(self, http_git_disabled):
        """Sets the http_git_disabled of this GeneralRepoSettings.


        :param http_git_disabled: The http_git_disabled of this GeneralRepoSettings.  # noqa: E501
        :type: bool
        """

        self._http_git_disabled = http_git_disabled

    @property
    def lfs_disabled(self):
        """Gets the lfs_disabled of this GeneralRepoSettings.  # noqa: E501


        :return: The lfs_disabled of this GeneralRepoSettings.  # noqa: E501
        :rtype: bool
        """
        return self._lfs_disabled

    @lfs_disabled.setter
    def lfs_disabled(self, lfs_disabled):
        """Sets the lfs_disabled of this GeneralRepoSettings.


        :param lfs_disabled: The lfs_disabled of this GeneralRepoSettings.  # noqa: E501
        :type: bool
        """

        self._lfs_disabled = lfs_disabled

    @property
    def migrations_disabled(self):
        """Gets the migrations_disabled of this GeneralRepoSettings.  # noqa: E501


        :return: The migrations_disabled of this GeneralRepoSettings.  # noqa: E501
        :rtype: bool
        """
        return self._migrations_disabled

    @migrations_disabled.setter
    def migrations_disabled(self, migrations_disabled):
        """Sets the migrations_disabled of this GeneralRepoSettings.


        :param migrations_disabled: The migrations_disabled of this GeneralRepoSettings.  # noqa: E501
        :type: bool
        """

        self._migrations_disabled = migrations_disabled

    @property
    def mirrors_disabled(self):
        """Gets the mirrors_disabled of this GeneralRepoSettings.  # noqa: E501


        :return: The mirrors_disabled of this GeneralRepoSettings.  # noqa: E501
        :rtype: bool
        """
        return self._mirrors_disabled

    @mirrors_disabled.setter
    def mirrors_disabled(self, mirrors_disabled):
        """Sets the mirrors_disabled of this GeneralRepoSettings.


        :param mirrors_disabled: The mirrors_disabled of this GeneralRepoSettings.  # noqa: E501
        :type: bool
        """

        self._mirrors_disabled = mirrors_disabled

    @property
    def stars_disabled(self):
        """Gets the stars_disabled of this GeneralRepoSettings.  # noqa: E501


        :return: The stars_disabled of this GeneralRepoSettings.  # noqa: E501
        :rtype: bool
        """
        return self._stars_disabled

    @stars_disabled.setter
    def stars_disabled(self, stars_disabled):
        """Sets the stars_disabled of this GeneralRepoSettings.


        :param stars_disabled: The stars_disabled of this GeneralRepoSettings.  # noqa: E501
        :type: bool
        """

        self._stars_disabled = stars_disabled

    @property
    def time_tracking_disabled(self):
        """Gets the time_tracking_disabled of this GeneralRepoSettings.  # noqa: E501


        :return: The time_tracking_disabled of this GeneralRepoSettings.  # noqa: E501
        :rtype: bool
        """
        return self._time_tracking_disabled

    @time_tracking_disabled.setter
    def time_tracking_disabled(self, time_tracking_disabled):
        """Sets the time_tracking_disabled of this GeneralRepoSettings.


        :param time_tracking_disabled: The time_tracking_disabled of this GeneralRepoSettings.  # noqa: E501
        :type: bool
        """

        self._time_tracking_disabled = time_tracking_disabled

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
        if issubclass(GeneralRepoSettings, dict):
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
        if not isinstance(other, GeneralRepoSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GeneralRepoSettings):
            return True

        return self.to_dict() != other.to_dict()
