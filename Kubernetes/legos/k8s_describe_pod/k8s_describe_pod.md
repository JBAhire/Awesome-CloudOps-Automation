{
"action_title": "Describe a Kubernetes POD in a given Namespace",
"action_description": "Describe a Kubernetes POD in a given Namespace",
"action_type": "LEGO_TYPE_K8S",
"action_entry_function": "k8s_describe_pod",
"action_needs_credential": true,
"action_supports_poll": true,
"action_supports_iteration": true,
"action_output_type": "ACTION_OUTPUT_TYPE_DICT",
"action_verbs": [
"describe"
],
"action_nouns": [
"pod",
"kubernetes",
"namespace"
]
}