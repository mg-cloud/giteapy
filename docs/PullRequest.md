# PullRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additions** | **int** | The number of lines added in the pull request | [optional] 
**allow_maintainer_edit** | **bool** | Whether maintainers can edit the pull request | [optional] 
**assignee** | [**User**](User.md) |  | [optional] 
**assignees** | [**list[User]**](User.md) | The list of users assigned to the pull request | [optional] 
**base** | [**PRBranchInfo**](PRBranchInfo.md) |  | [optional] 
**body** | **str** | The description body of the pull request | [optional] 
**changed_files** | **int** | The number of files changed in the pull request | [optional] 
**closed_at** | **datetime** |  | [optional] 
**comments** | **int** | The number of comments on the pull request | [optional] 
**created_at** | **datetime** |  | [optional] 
**deletions** | **int** | The number of lines deleted in the pull request | [optional] 
**diff_url** | **str** | The URL to download the diff patch | [optional] 
**draft** | **bool** | Whether the pull request is a draft | [optional] 
**due_date** | **datetime** |  | [optional] 
**head** | [**PRBranchInfo**](PRBranchInfo.md) |  | [optional] 
**html_url** | **str** | The HTML URL to view the pull request | [optional] 
**id** | **int** | The unique identifier of the pull request | [optional] 
**is_locked** | **bool** | Whether the pull request conversation is locked | [optional] 
**labels** | [**list[Label]**](Label.md) | The labels attached to the pull request | [optional] 
**merge_base** | **str** | The merge base commit SHA | [optional] 
**merge_commit_sha** | **str** | The SHA of the merge commit | [optional] 
**mergeable** | **bool** | Whether the pull request can be merged | [optional] 
**merged** | **bool** | Whether the pull request has been merged | [optional] 
**merged_at** | **datetime** |  | [optional] 
**merged_by** | [**User**](User.md) |  | [optional] 
**milestone** | [**Milestone**](Milestone.md) |  | [optional] 
**number** | **int** | The pull request number | [optional] 
**patch_url** | **str** | The URL to download the patch file | [optional] 
**pin_order** | **int** | The pin order for the pull request | [optional] 
**requested_reviewers** | [**list[User]**](User.md) | The users requested to review the pull request | [optional] 
**requested_reviewers_teams** | [**list[Team]**](Team.md) | The teams requested to review the pull request | [optional] 
**review_comments** | **int** | number of review comments made on the diff of a PR review (not including comments on commits or issues in a PR) | [optional] 
**state** | [**StateType**](StateType.md) |  | [optional] 
**title** | **str** | The title of the pull request | [optional] 
**updated_at** | **datetime** |  | [optional] 
**url** | **str** | The API URL of the pull request | [optional] 
**user** | [**User**](User.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


