{
  "action_title": "Get AWS EC2 Metrics from Cloudwatch",
  "action_description": "Get AWS CloudWatch Metrics for EC2 instances. These could be CPU, Network, Disk based measurements",
  "action_type": "LEGO_TYPE_AWS",
  "action_entry_function": "aws_get_cloudwatch_ec2",
  "action_needs_credential": true,
  "action_supports_poll": true,
  "action_output_type": "ACTION_OUTPUT_TYPE_STR",
  "action_supports_iteration": true,
  "action_verbs": [
    "get"
  ],
  "action_nouns": [
    "aws",
    "cloudwatch",
    "metrics"
  ]
}