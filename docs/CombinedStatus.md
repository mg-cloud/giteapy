# CombinedStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_url** | **str** | CommitURL is the API URL for the commit | [optional] 
**repository** | [**Repository**](Repository.md) |  | [optional] 
**sha** | **str** | SHA is the commit SHA this status applies to | [optional] 
**state** | **str** | State is the overall combined status state pending CommitStatusPending  CommitStatusPending is for when the CommitStatus is Pending success CommitStatusSuccess  CommitStatusSuccess is for when the CommitStatus is Success error CommitStatusError  CommitStatusError is for when the CommitStatus is Error failure CommitStatusFailure  CommitStatusFailure is for when the CommitStatus is Failure warning CommitStatusWarning  CommitStatusWarning is for when the CommitStatus is Warning skipped CommitStatusSkipped  CommitStatusSkipped is for when CommitStatus is Skipped | [optional] 
**statuses** | [**list[CommitStatus]**](CommitStatus.md) | Statuses contains all individual commit statuses | [optional] 
**total_count** | **int** | TotalCount is the total number of statuses | [optional] 
**url** | **str** | URL is the API URL for this combined status | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


