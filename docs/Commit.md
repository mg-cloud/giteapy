# Commit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**User**](User.md) |  | [optional] 
**commit** | [**RepoCommit**](RepoCommit.md) |  | [optional] 
**committer** | [**User**](User.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**files** | [**list[CommitAffectedFiles]**](CommitAffectedFiles.md) | Files contains information about files affected by the commit | [optional] 
**html_url** | **str** | HTMLURL is the web URL for viewing the commit | [optional] 
**parents** | [**list[CommitMeta]**](CommitMeta.md) | Parents contains the parent commit information | [optional] 
**sha** | **str** | SHA is the commit SHA hash | [optional] 
**stats** | [**CommitStats**](CommitStats.md) |  | [optional] 
**url** | **str** | URL is the API URL for the commit | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


