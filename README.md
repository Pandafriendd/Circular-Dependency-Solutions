# Circular-Dependency-Solutions

## Resolutions

* Define the S3 bucket name prior to create lambda permission.

* Create the S3 bucket without notification configuration, and then add the bucket in the next stack update.

* Create a less-constrained Lambda permission. For example, allow invocations for a specific AWS account by omitting SourceArn.

* Create a custom resource to run at the end of the stack workflow. This resource adds the notification configuration to the S3 bucket after all other resources are created.
