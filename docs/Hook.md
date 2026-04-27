# Hook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether the webhook is active and will be triggered | [optional] 
**authorization_header** | **str** | Authorization header to include in webhook requests | [optional] 
**branch_filter** | **str** | Branch filter pattern to determine which branches trigger the webhook | [optional] 
**config** | **dict(str, str)** | Configuration settings for the webhook | [optional] 
**created_at** | **datetime** |  | [optional] 
**events** | **list[str]** | List of events that trigger this webhook | [optional] 
**id** | **int** | The unique identifier of the webhook | [optional] 
**name** | **str** | Optional human-readable name for the webhook | [optional] 
**type** | **str** | The type of the webhook (e.g., gitea, slack, discord) | [optional] 
**updated_at** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


