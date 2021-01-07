# Circular-Dependency-Solutions

## Resolutions

* Define the S3 bucket name prior to create lambda permission and hardcode the S3 ARN in lambda permission, thus !Ref or !GetAtt is not required.

* Create the S3 bucket without notification configuration, and then add notification configuration for the bucket in the next stack update.

* Create a less-constrained Lambda permission. For example, allow invocations for a specific AWS account by omitting SourceArn.

* Create a custom resource to run at the end of the stack workflow. This resource adds the notification configuration to the S3 bucket after all other resources are created.


https://aws.amazon.com/blogs/infrastructure-and-automation/handling-circular-dependency-errors-in-aws-cloudformation/
https://aws.amazon.com/premiumsupport/knowledge-center/cloudformation-s3-notification-lambda/
