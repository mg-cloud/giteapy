# CommitStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | Context is the unique context identifier for the status | [optional] 
**created_at** | **datetime** |  | [optional] 
**creator** | [**User**](User.md) |  | [optional] 
**description** | **str** | Description provides a brief description of the status | [optional] 
**id** | **int** | ID is the unique identifier for the commit status | [optional] 
**status** | **str** | State represents the status state (pending, success, error, failure) pending CommitStatusPending  CommitStatusPending is for when the CommitStatus is Pending success CommitStatusSuccess  CommitStatusSuccess is for when the CommitStatus is Success error CommitStatusError  CommitStatusError is for when the CommitStatus is Error failure CommitStatusFailure  CommitStatusFailure is for when the CommitStatus is Failure warning CommitStatusWarning  CommitStatusWarning is for when the CommitStatus is Warning skipped CommitStatusSkipped  CommitStatusSkipped is for when CommitStatus is Skipped | [optional] 
**target_url** | **str** | TargetURL is the URL to link to for more details | [optional] 
**updated_at** | **datetime** |  | [optional] 
**url** | **str** | URL is the API URL for this status | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


