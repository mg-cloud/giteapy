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


class IssueFormField(object):
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
        'attributes': 'dict(str, object)',
        'id': 'str',
        'type': 'IssueFormFieldType',
        'validations': 'dict(str, object)'
    }

    attribute_map = {
        'attributes': 'attributes',
        'id': 'id',
        'type': 'type',
        'validations': 'validations'
    }

    def __init__(self, attributes=None, id=None, type=None, validations=None, _configuration=None):  # noqa: E501
        """IssueFormField - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._attributes = None
        self._id = None
        self._type = None
        self._validations = None
        self.discriminator = None

        if attributes is not None:
            self.attributes = attributes
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if validations is not None:
            self.validations = validations

    @property
    def attributes(self):
        """Gets the attributes of this IssueFormField.  # noqa: E501


        :return: The attributes of this IssueFormField.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this IssueFormField.


        :param attributes: The attributes of this IssueFormField.  # noqa: E501
        :type: dict(str, object)
        """

        self._attributes = attributes

    @property
    def id(self):
        """Gets the id of this IssueFormField.  # noqa: E501


        :return: The id of this IssueFormField.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IssueFormField.


        :param id: The id of this IssueFormField.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this IssueFormField.  # noqa: E501


        :return: The type of this IssueFormField.  # noqa: E501
        :rtype: IssueFormFieldType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IssueFormField.


        :param type: The type of this IssueFormField.  # noqa: E501
        :type: IssueFormFieldType
        """

        self._type = type

    @property
    def validations(self):
        """Gets the validations of this IssueFormField.  # noqa: E501


        :return: The validations of this IssueFormField.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._validations

    @validations.setter
    def validations(self, validations):
        """Sets the validations of this IssueFormField.


        :param validations: The validations of this IssueFormField.  # noqa: E501
        :type: dict(str, object)
        """

        self._validations = validations

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
        if issubclass(IssueFormField, dict):
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
        if not isinstance(other, IssueFormField):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IssueFormField):
            return True

        return self.to_dict() != other.to_dict()
