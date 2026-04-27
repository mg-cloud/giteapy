# EditPullRequestOption

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_maintainer_edit** | **bool** | Whether to allow maintainer edits | [optional] 
**assignee** | **str** | The new primary assignee username | [optional] 
**assignees** | **list[str]** | The new list of assignee usernames | [optional] 
**base** | **str** | The new base branch for the pull request | [optional] 
**body** | **str** | The new description body for the pull request | [optional] 
**content_version** | **int** | The current version of the pull request content to detect conflicts during editing | [optional] 
**due_date** | **datetime** |  | [optional] 
**labels** | **list[int]** | The new list of label IDs for the pull request | [optional] 
**milestone** | **int** | The new milestone ID for the pull request | [optional] 
**state** | **str** | The new state for the pull request | [optional] 
**title** | **str** | The new title for the pull request | [optional] 
**unset_due_date** | **bool** | Whether to remove the current deadline | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


