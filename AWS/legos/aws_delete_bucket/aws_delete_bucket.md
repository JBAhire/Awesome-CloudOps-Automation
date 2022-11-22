{
"action_title": "Delete AWS Bucket",
"action_description": "Delete an AWS S3 Bucket",
"action_type": "LEGO_TYPE_AWS",
"action_entry_function": "aws_delete_bucket",
"action_needs_credential": true,
"action_supports_poll": true,
"action_output_type": "ACTION_OUTPUT_TYPE_DICT",
"action_supports_iteration": true,
"action_verbs": ["delete"],
"action_nouns": [
"aws",
"bucket"
]
}