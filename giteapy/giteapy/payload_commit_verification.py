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


class PayloadCommitVerification(object):
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
        'payload': 'str',
        'reason': 'str',
        'signature': 'str',
        'signer': 'PayloadUser',
        'verified': 'bool'
    }

    attribute_map = {
        'payload': 'payload',
        'reason': 'reason',
        'signature': 'signature',
        'signer': 'signer',
        'verified': 'verified'
    }

    def __init__(self, payload=None, reason=None, signature=None, signer=None, verified=None, _configuration=None):  # noqa: E501
        """PayloadCommitVerification - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._payload = None
        self._reason = None
        self._signature = None
        self._signer = None
        self._verified = None
        self.discriminator = None

        if payload is not None:
            self.payload = payload
        if reason is not None:
            self.reason = reason
        if signature is not None:
            self.signature = signature
        if signer is not None:
            self.signer = signer
        if verified is not None:
            self.verified = verified

    @property
    def payload(self):
        """Gets the payload of this PayloadCommitVerification.  # noqa: E501


        :return: The payload of this PayloadCommitVerification.  # noqa: E501
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this PayloadCommitVerification.


        :param payload: The payload of this PayloadCommitVerification.  # noqa: E501
        :type: str
        """

        self._payload = payload

    @property
    def reason(self):
        """Gets the reason of this PayloadCommitVerification.  # noqa: E501


        :return: The reason of this PayloadCommitVerification.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this PayloadCommitVerification.


        :param reason: The reason of this PayloadCommitVerification.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def signature(self):
        """Gets the signature of this PayloadCommitVerification.  # noqa: E501


        :return: The signature of this PayloadCommitVerification.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this PayloadCommitVerification.


        :param signature: The signature of this PayloadCommitVerification.  # noqa: E501
        :type: str
        """

        self._signature = signature

    @property
    def signer(self):
        """Gets the signer of this PayloadCommitVerification.  # noqa: E501


        :return: The signer of this PayloadCommitVerification.  # noqa: E501
        :rtype: PayloadUser
        """
        return self._signer

    @signer.setter
    def signer(self, signer):
        """Sets the signer of this PayloadCommitVerification.


        :param signer: The signer of this PayloadCommitVerification.  # noqa: E501
        :type: PayloadUser
        """

        self._signer = signer

    @property
    def verified(self):
        """Gets the verified of this PayloadCommitVerification.  # noqa: E501


        :return: The verified of this PayloadCommitVerification.  # noqa: E501
        :rtype: bool
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """Sets the verified of this PayloadCommitVerification.


        :param verified: The verified of this PayloadCommitVerification.  # noqa: E501
        :type: bool
        """

        self._verified = verified

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
        if issubclass(PayloadCommitVerification, dict):
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
        if not isinstance(other, PayloadCommitVerification):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PayloadCommitVerification):
            return True

        return self.to_dict() != other.to_dict()
