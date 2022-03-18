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


class GeneralUISettings(object):
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
        'allowed_reactions': 'list[str]',
        'custom_emojis': 'list[str]',
        'default_theme': 'str'
    }

    attribute_map = {
        'allowed_reactions': 'allowed_reactions',
        'custom_emojis': 'custom_emojis',
        'default_theme': 'default_theme'
    }

    def __init__(self, allowed_reactions=None, custom_emojis=None, default_theme=None, _configuration=None):  # noqa: E501
        """GeneralUISettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allowed_reactions = None
        self._custom_emojis = None
        self._default_theme = None
        self.discriminator = None

        if allowed_reactions is not None:
            self.allowed_reactions = allowed_reactions
        if custom_emojis is not None:
            self.custom_emojis = custom_emojis
        if default_theme is not None:
            self.default_theme = default_theme

    @property
    def allowed_reactions(self):
        """Gets the allowed_reactions of this GeneralUISettings.  # noqa: E501


        :return: The allowed_reactions of this GeneralUISettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_reactions

    @allowed_reactions.setter
    def allowed_reactions(self, allowed_reactions):
        """Sets the allowed_reactions of this GeneralUISettings.


        :param allowed_reactions: The allowed_reactions of this GeneralUISettings.  # noqa: E501
        :type: list[str]
        """

        self._allowed_reactions = allowed_reactions

    @property
    def custom_emojis(self):
        """Gets the custom_emojis of this GeneralUISettings.  # noqa: E501


        :return: The custom_emojis of this GeneralUISettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._custom_emojis

    @custom_emojis.setter
    def custom_emojis(self, custom_emojis):
        """Sets the custom_emojis of this GeneralUISettings.


        :param custom_emojis: The custom_emojis of this GeneralUISettings.  # noqa: E501
        :type: list[str]
        """

        self._custom_emojis = custom_emojis

    @property
    def default_theme(self):
        """Gets the default_theme of this GeneralUISettings.  # noqa: E501


        :return: The default_theme of this GeneralUISettings.  # noqa: E501
        :rtype: str
        """
        return self._default_theme

    @default_theme.setter
    def default_theme(self, default_theme):
        """Sets the default_theme of this GeneralUISettings.


        :param default_theme: The default_theme of this GeneralUISettings.  # noqa: E501
        :type: str
        """

        self._default_theme = default_theme

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
        if issubclass(GeneralUISettings, dict):
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
        if not isinstance(other, GeneralUISettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GeneralUISettings):
            return True

        return self.to_dict() != other.to_dict()
