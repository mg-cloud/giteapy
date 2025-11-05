# GitTreeResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | Page is the current page number for pagination | [optional] 
**sha** | **str** | SHA is the tree object SHA | [optional] 
**total_count** | **int** | TotalCount is the total number of entries in the tree | [optional] 
**tree** | [**list[GitEntry]**](GitEntry.md) | Entries contains the tree entries (files and directories) | [optional] 
**truncated** | **bool** | Truncated indicates if the response was truncated due to size | [optional] 
**url** | **str** | URL is the API URL for this tree | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


