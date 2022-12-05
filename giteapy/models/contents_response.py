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


class ContentsResponse(object):
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
        'links': 'FileLinksResponse',
        'content': 'str',
        'download_url': 'str',
        'encoding': 'str',
        'git_url': 'str',
        'html_url': 'str',
        'name': 'str',
        'path': 'str',
        'sha': 'str',
        'size': 'int',
        'submodule_git_url': 'str',
        'target': 'str',
        'type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'links': '_links',
        'content': 'content',
        'download_url': 'download_url',
        'encoding': 'encoding',
        'git_url': 'git_url',
        'html_url': 'html_url',
        'name': 'name',
        'path': 'path',
        'sha': 'sha',
        'size': 'size',
        'submodule_git_url': 'submodule_git_url',
        'target': 'target',
        'type': 'type',
        'url': 'url'
    }

    def __init__(self, links=None, content=None, download_url=None, encoding=None, git_url=None, html_url=None, name=None, path=None, sha=None, size=None, submodule_git_url=None, target=None, type=None, url=None, _configuration=None):  # noqa: E501
        """ContentsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._links = None
        self._content = None
        self._download_url = None
        self._encoding = None
        self._git_url = None
        self._html_url = None
        self._name = None
        self._path = None
        self._sha = None
        self._size = None
        self._submodule_git_url = None
        self._target = None
        self._type = None
        self._url = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if content is not None:
            self.content = content
        if download_url is not None:
            self.download_url = download_url
        if encoding is not None:
            self.encoding = encoding
        if git_url is not None:
            self.git_url = git_url
        if html_url is not None:
            self.html_url = html_url
        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if sha is not None:
            self.sha = sha
        if size is not None:
            self.size = size
        if submodule_git_url is not None:
            self.submodule_git_url = submodule_git_url
        if target is not None:
            self.target = target
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url

    @property
    def links(self):
        """Gets the links of this ContentsResponse.  # noqa: E501


        :return: The links of this ContentsResponse.  # noqa: E501
        :rtype: FileLinksResponse
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ContentsResponse.


        :param links: The links of this ContentsResponse.  # noqa: E501
        :type: FileLinksResponse
        """

        self._links = links

    @property
    def content(self):
        """Gets the content of this ContentsResponse.  # noqa: E501

        `content` is populated when `type` is `file`, otherwise null  # noqa: E501

        :return: The content of this ContentsResponse.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ContentsResponse.

        `content` is populated when `type` is `file`, otherwise null  # noqa: E501

        :param content: The content of this ContentsResponse.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def download_url(self):
        """Gets the download_url of this ContentsResponse.  # noqa: E501


        :return: The download_url of this ContentsResponse.  # noqa: E501
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """Sets the download_url of this ContentsResponse.


        :param download_url: The download_url of this ContentsResponse.  # noqa: E501
        :type: str
        """

        self._download_url = download_url

    @property
    def encoding(self):
        """Gets the encoding of this ContentsResponse.  # noqa: E501

        `encoding` is populated when `type` is `file`, otherwise null  # noqa: E501

        :return: The encoding of this ContentsResponse.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this ContentsResponse.

        `encoding` is populated when `type` is `file`, otherwise null  # noqa: E501

        :param encoding: The encoding of this ContentsResponse.  # noqa: E501
        :type: str
        """

        self._encoding = encoding

    @property
    def git_url(self):
        """Gets the git_url of this ContentsResponse.  # noqa: E501


        :return: The git_url of this ContentsResponse.  # noqa: E501
        :rtype: str
        """
        return self._git_url

    @git_url.setter
    def git_url(self, git_url):
        """Sets the git_url of this ContentsResponse.


        :param git_url: The git_url of this ContentsResponse.  # noqa: E501
        :type: str
        """

        self._git_url = git_url

    @property
    def html_url(self):
        """Gets the html_url of this ContentsResponse.  # noqa: E501


        :return: The html_url of this ContentsResponse.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this ContentsResponse.


        :param html_url: The html_url of this ContentsResponse.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def name(self):
        """Gets the name of this ContentsResponse.  # noqa: E501


        :return: The name of this ContentsResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ContentsResponse.


        :param name: The name of this ContentsResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def path(self):
        """Gets the path of this ContentsResponse.  # noqa: E501


        :return: The path of this ContentsResponse.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ContentsResponse.


        :param path: The path of this ContentsResponse.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def sha(self):
        """Gets the sha of this ContentsResponse.  # noqa: E501


        :return: The sha of this ContentsResponse.  # noqa: E501
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this ContentsResponse.


        :param sha: The sha of this ContentsResponse.  # noqa: E501
        :type: str
        """

        self._sha = sha

    @property
    def size(self):
        """Gets the size of this ContentsResponse.  # noqa: E501


        :return: The size of this ContentsResponse.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ContentsResponse.


        :param size: The size of this ContentsResponse.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def submodule_git_url(self):
        """Gets the submodule_git_url of this ContentsResponse.  # noqa: E501

        `submodule_git_url` is populated when `type` is `submodule`, otherwise null  # noqa: E501

        :return: The submodule_git_url of this ContentsResponse.  # noqa: E501
        :rtype: str
        """
        return self._submodule_git_url

    @submodule_git_url.setter
    def submodule_git_url(self, submodule_git_url):
        """Sets the submodule_git_url of this ContentsResponse.

        `submodule_git_url` is populated when `type` is `submodule`, otherwise null  # noqa: E501

        :param submodule_git_url: The submodule_git_url of this ContentsResponse.  # noqa: E501
        :type: str
        """

        self._submodule_git_url = submodule_git_url

    @property
    def target(self):
        """Gets the target of this ContentsResponse.  # noqa: E501

        `target` is populated when `type` is `symlink`, otherwise null  # noqa: E501

        :return: The target of this ContentsResponse.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this ContentsResponse.

        `target` is populated when `type` is `symlink`, otherwise null  # noqa: E501

        :param target: The target of this ContentsResponse.  # noqa: E501
        :type: str
        """

        self._target = target

    @property
    def type(self):
        """Gets the type of this ContentsResponse.  # noqa: E501

        `type` will be `file`, `dir`, `symlink`, or `submodule`  # noqa: E501

        :return: The type of this ContentsResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ContentsResponse.

        `type` will be `file`, `dir`, `symlink`, or `submodule`  # noqa: E501

        :param type: The type of this ContentsResponse.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this ContentsResponse.  # noqa: E501


        :return: The url of this ContentsResponse.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ContentsResponse.


        :param url: The url of this ContentsResponse.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(ContentsResponse, dict):
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
        if not isinstance(other, ContentsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContentsResponse):
            return True

        return self.to_dict() != other.to_dict()
