# GPGKey

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_certify** | **bool** | Whether the key can be used for certification | [optional] 
**can_encrypt_comms** | **bool** | Whether the key can be used for encrypting communications | [optional] 
**can_encrypt_storage** | **bool** | Whether the key can be used for encrypting storage | [optional] 
**can_sign** | **bool** | Whether the key can be used for signing | [optional] 
**created_at** | **datetime** |  | [optional] 
**emails** | [**list[GPGKeyEmail]**](GPGKeyEmail.md) | List of email addresses associated with this GPG key | [optional] 
**expires_at** | **datetime** |  | [optional] 
**id** | **int** | The unique identifier of the GPG key | [optional] 
**key_id** | **str** | The key ID of the GPG key | [optional] 
**primary_key_id** | **str** | The primary key ID of the GPG key | [optional] 
**public_key** | **str** | The public key content in armored format | [optional] 
**subkeys** | [**list[GPGKey]**](GPGKey.md) | List of subkeys of this GPG key | [optional] 
**verified** | **bool** | Whether the GPG key has been verified | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


