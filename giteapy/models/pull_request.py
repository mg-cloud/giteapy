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


class PullRequest(object):
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
        'allow_maintainer_edit': 'bool',
        'assignee': 'User',
        'assignees': 'list[User]',
        'base': 'PRBranchInfo',
        'body': 'str',
        'closed_at': 'datetime',
        'comments': 'int',
        'created_at': 'datetime',
        'diff_url': 'str',
        'due_date': 'datetime',
        'head': 'PRBranchInfo',
        'html_url': 'str',
        'id': 'int',
        'is_locked': 'bool',
        'labels': 'list[Label]',
        'merge_base': 'str',
        'merge_commit_sha': 'str',
        'mergeable': 'bool',
        'merged': 'bool',
        'merged_at': 'datetime',
        'merged_by': 'User',
        'milestone': 'Milestone',
        'number': 'int',
        'patch_url': 'str',
        'pin_order': 'int',
        'requested_reviewers': 'list[User]',
        'state': 'StateType',
        'title': 'str',
        'updated_at': 'datetime',
        'url': 'str',
        'user': 'User'
    }

    attribute_map = {
        'allow_maintainer_edit': 'allow_maintainer_edit',
        'assignee': 'assignee',
        'assignees': 'assignees',
        'base': 'base',
        'body': 'body',
        'closed_at': 'closed_at',
        'comments': 'comments',
        'created_at': 'created_at',
        'diff_url': 'diff_url',
        'due_date': 'due_date',
        'head': 'head',
        'html_url': 'html_url',
        'id': 'id',
        'is_locked': 'is_locked',
        'labels': 'labels',
        'merge_base': 'merge_base',
        'merge_commit_sha': 'merge_commit_sha',
        'mergeable': 'mergeable',
        'merged': 'merged',
        'merged_at': 'merged_at',
        'merged_by': 'merged_by',
        'milestone': 'milestone',
        'number': 'number',
        'patch_url': 'patch_url',
        'pin_order': 'pin_order',
        'requested_reviewers': 'requested_reviewers',
        'state': 'state',
        'title': 'title',
        'updated_at': 'updated_at',
        'url': 'url',
        'user': 'user'
    }

    def __init__(self, allow_maintainer_edit=None, assignee=None, assignees=None, base=None, body=None, closed_at=None, comments=None, created_at=None, diff_url=None, due_date=None, head=None, html_url=None, id=None, is_locked=None, labels=None, merge_base=None, merge_commit_sha=None, mergeable=None, merged=None, merged_at=None, merged_by=None, milestone=None, number=None, patch_url=None, pin_order=None, requested_reviewers=None, state=None, title=None, updated_at=None, url=None, user=None, _configuration=None):  # noqa: E501
        """PullRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow_maintainer_edit = None
        self._assignee = None
        self._assignees = None
        self._base = None
        self._body = None
        self._closed_at = None
        self._comments = None
        self._created_at = None
        self._diff_url = None
        self._due_date = None
        self._head = None
        self._html_url = None
        self._id = None
        self._is_locked = None
        self._labels = None
        self._merge_base = None
        self._merge_commit_sha = None
        self._mergeable = None
        self._merged = None
        self._merged_at = None
        self._merged_by = None
        self._milestone = None
        self._number = None
        self._patch_url = None
        self._pin_order = None
        self._requested_reviewers = None
        self._state = None
        self._title = None
        self._updated_at = None
        self._url = None
        self._user = None
        self.discriminator = None

        if allow_maintainer_edit is not None:
            self.allow_maintainer_edit = allow_maintainer_edit
        if assignee is not None:
            self.assignee = assignee
        if assignees is not None:
            self.assignees = assignees
        if base is not None:
            self.base = base
        if body is not None:
            self.body = body
        if closed_at is not None:
            self.closed_at = closed_at
        if comments is not None:
            self.comments = comments
        if created_at is not None:
            self.created_at = created_at
        if diff_url is not None:
            self.diff_url = diff_url
        if due_date is not None:
            self.due_date = due_date
        if head is not None:
            self.head = head
        if html_url is not None:
            self.html_url = html_url
        if id is not None:
            self.id = id
        if is_locked is not None:
            self.is_locked = is_locked
        if labels is not None:
            self.labels = labels
        if merge_base is not None:
            self.merge_base = merge_base
        if merge_commit_sha is not None:
            self.merge_commit_sha = merge_commit_sha
        if mergeable is not None:
            self.mergeable = mergeable
        if merged is not None:
            self.merged = merged
        if merged_at is not None:
            self.merged_at = merged_at
        if merged_by is not None:
            self.merged_by = merged_by
        if milestone is not None:
            self.milestone = milestone
        if number is not None:
            self.number = number
        if patch_url is not None:
            self.patch_url = patch_url
        if pin_order is not None:
            self.pin_order = pin_order
        if requested_reviewers is not None:
            self.requested_reviewers = requested_reviewers
        if state is not None:
            self.state = state
        if title is not None:
            self.title = title
        if updated_at is not None:
            self.updated_at = updated_at
        if url is not None:
            self.url = url
        if user is not None:
            self.user = user

    @property
    def allow_maintainer_edit(self):
        """Gets the allow_maintainer_edit of this PullRequest.  # noqa: E501


        :return: The allow_maintainer_edit of this PullRequest.  # noqa: E501
        :rtype: bool
        """
        return self._allow_maintainer_edit

    @allow_maintainer_edit.setter
    def allow_maintainer_edit(self, allow_maintainer_edit):
        """Sets the allow_maintainer_edit of this PullRequest.


        :param allow_maintainer_edit: The allow_maintainer_edit of this PullRequest.  # noqa: E501
        :type: bool
        """

        self._allow_maintainer_edit = allow_maintainer_edit

    @property
    def assignee(self):
        """Gets the assignee of this PullRequest.  # noqa: E501


        :return: The assignee of this PullRequest.  # noqa: E501
        :rtype: User
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        """Sets the assignee of this PullRequest.


        :param assignee: The assignee of this PullRequest.  # noqa: E501
        :type: User
        """

        self._assignee = assignee

    @property
    def assignees(self):
        """Gets the assignees of this PullRequest.  # noqa: E501


        :return: The assignees of this PullRequest.  # noqa: E501
        :rtype: list[User]
        """
        return self._assignees

    @assignees.setter
    def assignees(self, assignees):
        """Sets the assignees of this PullRequest.


        :param assignees: The assignees of this PullRequest.  # noqa: E501
        :type: list[User]
        """

        self._assignees = assignees

    @property
    def base(self):
        """Gets the base of this PullRequest.  # noqa: E501


        :return: The base of this PullRequest.  # noqa: E501
        :rtype: PRBranchInfo
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this PullRequest.


        :param base: The base of this PullRequest.  # noqa: E501
        :type: PRBranchInfo
        """

        self._base = base

    @property
    def body(self):
        """Gets the body of this PullRequest.  # noqa: E501


        :return: The body of this PullRequest.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this PullRequest.


        :param body: The body of this PullRequest.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def closed_at(self):
        """Gets the closed_at of this PullRequest.  # noqa: E501


        :return: The closed_at of this PullRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._closed_at

    @closed_at.setter
    def closed_at(self, closed_at):
        """Sets the closed_at of this PullRequest.


        :param closed_at: The closed_at of this PullRequest.  # noqa: E501
        :type: datetime
        """

        self._closed_at = closed_at

    @property
    def comments(self):
        """Gets the comments of this PullRequest.  # noqa: E501


        :return: The comments of this PullRequest.  # noqa: E501
        :rtype: int
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this PullRequest.


        :param comments: The comments of this PullRequest.  # noqa: E501
        :type: int
        """

        self._comments = comments

    @property
    def created_at(self):
        """Gets the created_at of this PullRequest.  # noqa: E501


        :return: The created_at of this PullRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PullRequest.


        :param created_at: The created_at of this PullRequest.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def diff_url(self):
        """Gets the diff_url of this PullRequest.  # noqa: E501


        :return: The diff_url of this PullRequest.  # noqa: E501
        :rtype: str
        """
        return self._diff_url

    @diff_url.setter
    def diff_url(self, diff_url):
        """Sets the diff_url of this PullRequest.


        :param diff_url: The diff_url of this PullRequest.  # noqa: E501
        :type: str
        """

        self._diff_url = diff_url

    @property
    def due_date(self):
        """Gets the due_date of this PullRequest.  # noqa: E501


        :return: The due_date of this PullRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this PullRequest.


        :param due_date: The due_date of this PullRequest.  # noqa: E501
        :type: datetime
        """

        self._due_date = due_date

    @property
    def head(self):
        """Gets the head of this PullRequest.  # noqa: E501


        :return: The head of this PullRequest.  # noqa: E501
        :rtype: PRBranchInfo
        """
        return self._head

    @head.setter
    def head(self, head):
        """Sets the head of this PullRequest.


        :param head: The head of this PullRequest.  # noqa: E501
        :type: PRBranchInfo
        """

        self._head = head

    @property
    def html_url(self):
        """Gets the html_url of this PullRequest.  # noqa: E501


        :return: The html_url of this PullRequest.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this PullRequest.


        :param html_url: The html_url of this PullRequest.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def id(self):
        """Gets the id of this PullRequest.  # noqa: E501


        :return: The id of this PullRequest.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PullRequest.


        :param id: The id of this PullRequest.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_locked(self):
        """Gets the is_locked of this PullRequest.  # noqa: E501


        :return: The is_locked of this PullRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_locked

    @is_locked.setter
    def is_locked(self, is_locked):
        """Sets the is_locked of this PullRequest.


        :param is_locked: The is_locked of this PullRequest.  # noqa: E501
        :type: bool
        """

        self._is_locked = is_locked

    @property
    def labels(self):
        """Gets the labels of this PullRequest.  # noqa: E501


        :return: The labels of this PullRequest.  # noqa: E501
        :rtype: list[Label]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this PullRequest.


        :param labels: The labels of this PullRequest.  # noqa: E501
        :type: list[Label]
        """

        self._labels = labels

    @property
    def merge_base(self):
        """Gets the merge_base of this PullRequest.  # noqa: E501


        :return: The merge_base of this PullRequest.  # noqa: E501
        :rtype: str
        """
        return self._merge_base

    @merge_base.setter
    def merge_base(self, merge_base):
        """Sets the merge_base of this PullRequest.


        :param merge_base: The merge_base of this PullRequest.  # noqa: E501
        :type: str
        """

        self._merge_base = merge_base

    @property
    def merge_commit_sha(self):
        """Gets the merge_commit_sha of this PullRequest.  # noqa: E501


        :return: The merge_commit_sha of this PullRequest.  # noqa: E501
        :rtype: str
        """
        return self._merge_commit_sha

    @merge_commit_sha.setter
    def merge_commit_sha(self, merge_commit_sha):
        """Sets the merge_commit_sha of this PullRequest.


        :param merge_commit_sha: The merge_commit_sha of this PullRequest.  # noqa: E501
        :type: str
        """

        self._merge_commit_sha = merge_commit_sha

    @property
    def mergeable(self):
        """Gets the mergeable of this PullRequest.  # noqa: E501


        :return: The mergeable of this PullRequest.  # noqa: E501
        :rtype: bool
        """
        return self._mergeable

    @mergeable.setter
    def mergeable(self, mergeable):
        """Sets the mergeable of this PullRequest.


        :param mergeable: The mergeable of this PullRequest.  # noqa: E501
        :type: bool
        """

        self._mergeable = mergeable

    @property
    def merged(self):
        """Gets the merged of this PullRequest.  # noqa: E501


        :return: The merged of this PullRequest.  # noqa: E501
        :rtype: bool
        """
        return self._merged

    @merged.setter
    def merged(self, merged):
        """Sets the merged of this PullRequest.


        :param merged: The merged of this PullRequest.  # noqa: E501
        :type: bool
        """

        self._merged = merged

    @property
    def merged_at(self):
        """Gets the merged_at of this PullRequest.  # noqa: E501


        :return: The merged_at of this PullRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._merged_at

    @merged_at.setter
    def merged_at(self, merged_at):
        """Sets the merged_at of this PullRequest.


        :param merged_at: The merged_at of this PullRequest.  # noqa: E501
        :type: datetime
        """

        self._merged_at = merged_at

    @property
    def merged_by(self):
        """Gets the merged_by of this PullRequest.  # noqa: E501


        :return: The merged_by of this PullRequest.  # noqa: E501
        :rtype: User
        """
        return self._merged_by

    @merged_by.setter
    def merged_by(self, merged_by):
        """Sets the merged_by of this PullRequest.


        :param merged_by: The merged_by of this PullRequest.  # noqa: E501
        :type: User
        """

        self._merged_by = merged_by

    @property
    def milestone(self):
        """Gets the milestone of this PullRequest.  # noqa: E501


        :return: The milestone of this PullRequest.  # noqa: E501
        :rtype: Milestone
        """
        return self._milestone

    @milestone.setter
    def milestone(self, milestone):
        """Sets the milestone of this PullRequest.


        :param milestone: The milestone of this PullRequest.  # noqa: E501
        :type: Milestone
        """

        self._milestone = milestone

    @property
    def number(self):
        """Gets the number of this PullRequest.  # noqa: E501


        :return: The number of this PullRequest.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this PullRequest.


        :param number: The number of this PullRequest.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def patch_url(self):
        """Gets the patch_url of this PullRequest.  # noqa: E501


        :return: The patch_url of this PullRequest.  # noqa: E501
        :rtype: str
        """
        return self._patch_url

    @patch_url.setter
    def patch_url(self, patch_url):
        """Sets the patch_url of this PullRequest.


        :param patch_url: The patch_url of this PullRequest.  # noqa: E501
        :type: str
        """

        self._patch_url = patch_url

    @property
    def pin_order(self):
        """Gets the pin_order of this PullRequest.  # noqa: E501


        :return: The pin_order of this PullRequest.  # noqa: E501
        :rtype: int
        """
        return self._pin_order

    @pin_order.setter
    def pin_order(self, pin_order):
        """Sets the pin_order of this PullRequest.


        :param pin_order: The pin_order of this PullRequest.  # noqa: E501
        :type: int
        """

        self._pin_order = pin_order

    @property
    def requested_reviewers(self):
        """Gets the requested_reviewers of this PullRequest.  # noqa: E501


        :return: The requested_reviewers of this PullRequest.  # noqa: E501
        :rtype: list[User]
        """
        return self._requested_reviewers

    @requested_reviewers.setter
    def requested_reviewers(self, requested_reviewers):
        """Sets the requested_reviewers of this PullRequest.


        :param requested_reviewers: The requested_reviewers of this PullRequest.  # noqa: E501
        :type: list[User]
        """

        self._requested_reviewers = requested_reviewers

    @property
    def state(self):
        """Gets the state of this PullRequest.  # noqa: E501


        :return: The state of this PullRequest.  # noqa: E501
        :rtype: StateType
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PullRequest.


        :param state: The state of this PullRequest.  # noqa: E501
        :type: StateType
        """

        self._state = state

    @property
    def title(self):
        """Gets the title of this PullRequest.  # noqa: E501


        :return: The title of this PullRequest.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PullRequest.


        :param title: The title of this PullRequest.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def updated_at(self):
        """Gets the updated_at of this PullRequest.  # noqa: E501


        :return: The updated_at of this PullRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PullRequest.


        :param updated_at: The updated_at of this PullRequest.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def url(self):
        """Gets the url of this PullRequest.  # noqa: E501


        :return: The url of this PullRequest.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PullRequest.


        :param url: The url of this PullRequest.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def user(self):
        """Gets the user of this PullRequest.  # noqa: E501


        :return: The user of this PullRequest.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PullRequest.


        :param user: The user of this PullRequest.  # noqa: E501
        :type: User
        """

        self._user = user

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
        if issubclass(PullRequest, dict):
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
        if not isinstance(other, PullRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PullRequest):
            return True

        return self.to_dict() != other.to_dict()
