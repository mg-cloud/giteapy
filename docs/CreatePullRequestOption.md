# CreatePullRequestOption

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee** | **str** | The primary assignee username | [optional] 
**assignees** | **list[str]** | The list of assignee usernames | [optional] 
**base** | **str** | The base branch for the pull request | [optional] 
**body** | **str** | The description body of the pull request | [optional] 
**due_date** | **datetime** |  | [optional] 
**head** | **str** | The head branch for the pull request, it could be a branch name on the base repository or a form like &#x60;&lt;username&gt;:&lt;branch&gt;&#x60; which refers to the user&#39;s fork repository&#39;s branch. | [optional] 
**labels** | **list[int]** | The list of label IDs to assign to the pull request | [optional] 
**milestone** | **int** | The milestone ID to assign to the pull request | [optional] 
**reviewers** | **list[str]** | The list of reviewer usernames | [optional] 
**team_reviewers** | **list[str]** | The list of team reviewer names | [optional] 
**title** | **str** | The title of the pull request | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


