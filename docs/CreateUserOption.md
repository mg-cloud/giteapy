# CreateUserOption

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | For explicitly setting the user creation timestamp. Useful when users are migrated from other systems. When omitted, the user&#39;s creation timestamp will be set to \&quot;now\&quot;. | [optional] 
**email** | **str** |  | 
**full_name** | **str** | The full display name of the user | [optional] 
**login_name** | **str** | identifier of the user, provided by the external authenticator (if configured) | [optional] [default to 'empty']
**must_change_password** | **bool** | Whether the user must change password on first login | [optional] 
**password** | **str** | The plain text password for the user | [optional] 
**restricted** | **bool** | Whether the user has restricted access privileges | [optional] 
**send_notify** | **bool** | Whether to send welcome notification email to the user | [optional] 
**source_id** | **int** | The authentication source ID to associate with the user | [optional] 
**username** | **str** | username of the user | 
**visibility** | **str** | User visibility level: public, limited, or private | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


