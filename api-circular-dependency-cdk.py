# https://stackoverflow.com/questions/59324529/how-to-create-api-gateway-resource-policy-that-references-itself-in-the-python-c

delete_trigger_integration = aws_apigateway.LambdaIntegration(
    trigger_step_lambda, proxy=False, integration_responses=[])

api_policy_document = aws_iam.PolicyDocument()

api = aws_apigateway.RestApi(
    self,
    "GithubWebhookApi",
    rest_api_name=PROJECT_NAME + "-apigateway-trigger-delete",
    default_integration=delete_trigger_integration,
    policy=api_policy_document)

delete_execution_resource = api.root.add_resource("execution")

delete_execution_method = delete_execution_resource.add_method(
    "POST", delete_trigger_integration)
delete_execution_resource.add_cors_preflight(allow_origins=["*"])

create_repo_lambda.add_environment("API_URL",
                                   delete_execution_resource.url)

api_policy_document.add_statements(
    aws_iam.PolicyStatement(
        effect=aws_iam.Effect.ALLOW,
        principals=[aws_iam.AnyPrincipal()],
        actions=["execute-api:Invoke"],
        #resources=[api.arn_for_execute_api()],   # non-worked
        resources=[core.Fn.Join('', ['execute-api:/', '*'])]  # worked
        ))

api_policy_document.add_statements(
    aws_iam.PolicyStatement(
        effect=aws_iam.Effect.DENY,
        actions=["execute-api:Invoke"],
        conditions={
            "NotIpAddress": {
                "aws:SourceIp": [
                    "192.30.252.0/22", "185.199.108.0/22",
                    "140.82.112.0/20"
                ]
            }
        },
        principals=[aws_iam.AnyPrincipal()],
        #resources=[api.arn_for_execute_api()],   # non-worked
        resources=[core.Fn.Join('', ['execute-api:/', '*'])]  # worked
        ))