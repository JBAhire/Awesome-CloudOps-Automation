{
"action_title": "Upload file to S3",
"action_description": "Upload a local file to S3",
"action_type": "LEGO_TYPE_AWS",
"action_entry_function": "aws_upload_file_to_s3",
"action_needs_credential": true,
"action_supports_poll": true,
"action_output_type": "ACTION_OUTPUT_TYPE_STR",
"action_supports_iteration": true,
"action_verbs": [
"put",
"upload"
],
"action_nouns": [
"aws",
"bucket",
"file"
]
}